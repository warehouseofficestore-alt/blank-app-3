import sqlite3
import imaplib
import email
from datetime import datetime

# ==========================================
# 1. GESTIÓN DE BASE DE DATOS Y REGISTRO (AUDITORÍA)
# ==========================================

def inicializar_base_datos():
    """Crea la base de datos local de manera segura si no existe."""
    conn = sqlite3.connect('aquacheck_audit.db')
    cursor = conn.cursor()
    
    # Tabla para registrar cada análisis y uso de la app
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros_uso (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            muestra_id TEXT,
            tipo_fuente TEXT,
            ph REAL,
            turbidez REAL,
            estado TEXT,
            referencia_pago TEXT,
            pago_verificado INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def registrar_actividad(muestra_id, tipo_fuente, ph, turbidity, estado, referencia_pago, verificado=0):
    """Inserta una nueva traza de actividad en el sistema de auditoría."""
    inicializar_base_datos()
    conn = sqlite3.connect('aquacheck_audit.db')
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO registros_uso (timestamp, muestra_id, tipo_fuente, ph, turbidez, estado, referencia_pago, pago_verificado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (timestamp, muestra_id, tipo_fuente, ph, turbidity, estado, referencia_pago, verificado))
    
    conn.commit()
    conn.close()


# ==========================================
# 2. VALIDADOR AUTOMÁTICO DE CORREOS BANCARIOS (IMAP)
# ==========================================

def verificar_pago_en_correo(referencia_buscada, correo_usuario, password_app):
    """
    Conecta de forma segura a la bandeja de entrada (ej. Gmail) para buscar 
    el correo de notificación del banco con la referencia de pago exacta.
    """
    try:
        # Conexión IMAP segura a Gmail (donde llegan las alertas del Banco Provincial / Venezuela)
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(correo_usuario, password_app)
        mail.select('inbox')
        
        # Buscar correos recientes que contengan la referencia bancaria
        status, messages = mail.search(None, f'(BODY "{referencia_buscada}")')
        
        if status != 'OK':
            mail.logout()
            return False

        for num in messages[0].split():
            res, msg_data = mail.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    # Extraer el cuerpo del correo
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                cuerpo = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                                if referencia_buscada in cuerpo:
                                    mail.logout()
                                    return True
                    else:
                        cuerpo = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                        if referencia_buscada in cuerpo:
                            mail.logout()
                            return True
                            
        mail.logout()
        return False
    except Exception as e:
        print(f"Error en la verificación de correo: {e}")
        return False
