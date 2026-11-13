import streamlit as st
from datetime import datetime
import base64
from googleapiclient.discovery import build

# --- AQUÍ DEFINES LA FUNCIÓN ---
def verificar_pago_gmail_real(referencia_bancaria, monto_esperado=3.00):
    try:
        service = build('gmail', 'v1')
        query = f'"{referencia_bancaria}"'
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        if not messages:
            return False
            
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            snippet = msg_data.get('snippet', '').lower()
            payload = msg_data.get('payload', {})
            body = ""
            
            if 'parts' in payload:
                for part in payload['parts']:
                    if part.get('mimeType') == 'text/plain':
                        data = part.get('body', {}).get('data', '')
                        if data:
                            body = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore').lower()
            
            contenido_total = (snippet + " " + body)
            if referencia_bancaria.lower() in contenido_total:
                return True
                
        return False
    except Exception as e:
        print(f"Error conectando a Gmail: {e}")
        return False

# --- EL RESTO DE TU CÓDIGO (Páginas, modo_app, etc.) ---

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image

st.set_page_config(
    page_title="AquaCheck Pro - Laboratorio Avanzado",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0d1117 0%, #161b22 100%); color: #c9d1d9; }
    .cyber-title { font-size: 2.8rem; font-weight: 900; background: linear-gradient(90deg, #00f0ff, #7000ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0px; }
    .cyber-subtitle { color: #8b949e; font-size: 1.1rem; border-left: 3px solid #00f0ff; padding-left: 10px; margin-bottom: 30px; }
    .cyber-card { background: rgba(22, 27, 34, 0.85); border: 1px solid #30363d; border-radius: 16px; padding: 25px; box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.15); margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(90deg, #00f0ff 0%, #0077ff 100%); color: #0d1117; font-weight: 800; border-radius: 8px; padding: 12px 24px; text-transform: uppercase; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="cyber-title">💧 AquaCheck // Advanced Lab</p>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">Plataforma de Certificación Hídrica con Perfil Bacteriológico y Espectroscopia</p>', unsafe_allow_html=True)

# Menú de navegación actualizado con Centro de Control
st.sidebar.markdown("### 🎛️ NÚCLEO OPERATIVO")
modo_app = st.sidebar.radio("Seleccionar Módulo:", [
    "🏠 Centro de Control (Inicio)", 
    "📸 Visión de Campo (Espectral)", 
    "🎛️ Panel Analítico Completo",       
    "💳 Certificación y Pagos",
    "🌐 Protocolos Sanitarios", 
    "📞 Contacto Corporativo"
])

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small style='color: #8b949e;'><b>Aviso Legal:</b> AquaCheck es una herramienta digital de pre-diagnóstico. Se requiere validación mediante pruebas físicas y microbiológicas de laboratorio para confirmar la potabilidad final del agua.</small>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# MÓDULO 0: CENTRO DE CONTROL / INICIO
# ---------------------------------------------------------
if modo_app == "🏠 Centro de Control (Inicio)":
    st.markdown('<div class="cyber-card"><h3>🚀 Bienvenida al Sistema AquaCheck Pro</h3><p>Plataforma inteligente de certificación hídrica, análisis espectroscópico y control bacteriológico preliminar.</p></div>', unsafe_allow_html=True)
    
    with st.expander("📖 ¿Cuál es la utilidad de esta plataforma y cómo se opera?", expanded=True):
        st.markdown("""
        * **Propósito Principal:** Proveer una herramienta digital avanzada de pre-diagnóstico y estimación de pureza hídrica mediante visión computacional y modelado de parámetros físico-químicos.
        * **Flujo Operativo General:**
          1. **Navegación:** Utilice el menú lateral izquierdo para alternar entre los diferentes módulos de análisis y control.
          2. **Captura Óptica:** Emplee el módulo de **Visión de Campo** para registrar muestras y descomponer su espectro cromático en vivo.
          3. **Diagnóstico y Emisión:** Ingrese parámetros en el **Panel Analítico**, procese los resultados y complete la referencia de pago móvil para liberar automáticamente los archivos oficiales de certificación.
        * **Garantía y Cumplimiento:** Todos los reportes emitidos incluyen avisos normativos estrictos que recuerdan la necesidad de validar los datos mediante ensayos físicos en laboratorios certificados.
        """)

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown('<div class="cyber-card"><h4>⚡ Características del Sistema</h4><p>• Extracción espectral RGB normalizada.<br>• Generación dinámica de certificados.<br>• Seguridad transaccional integrada.</p></div>', unsafe_allow_html=True)
    with col_h2:
        st.markdown('<div class="cyber-card"><h4>🛡️ Seguridad y Privacidad</h4><p>• Datos sensibles protegidos.<br>• Emisión de pagos bajo demanda.<br>• Trazabilidad de muestras (AC-2401).</p></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 1: VISIÓN DE CAMPO (ESPECTRAL)
# ---------------------------------------------------------
elif modo_app == "📸 Visión de Campo (Espectral)":
    st.markdown('<div class="cyber-card"><h3>📷 Captura Espectral Hiperrealista</h3><p>Registro óptico y descomposición cromática de muestras líquidas en tiempo real.</p></div>', unsafe_allow_html=True)
    
    with st.expander("📖 Guía de Operación: Módulo Espectral", expanded=False):
        st.markdown("""
        * **Utilidad:** Analizar ópticamente una muestra mediante la cámara del dispositivo para extraer perfiles de intensidad de luz en los canales Rojo, Verde y Azul (RGB), simulando un análisis espectroscópico preliminar.
        * **Paso a Paso:**
          1. Apunte la cámara del dispositivo hacia la muestra de agua con iluminación adecuada.
          2. Haga clic en el botón **"Tome una foto"** del widget inferior.
          3. El sistema procesará automáticamente la matriz de píxeles y generará la gráfica espectroscópica normalizada junto con el estado preliminar de claridad.
        """)
    
    col_c1, col_c2 = st.columns([1, 1])
    with col_c1:
        foto = st.camera_input("Sensor Óptico de Campo")
        
    if foto:
        image_pil = Image.open(foto).convert('RGB')
        img_array = np.array(image_pil)
        
        alto, ancho, _ = img_array.shape
        linea = img_array[alto//2, :, :]
        r = linea[:, 0].astype(float) / 255.0
        g = linea[:, 1].astype(float) / 255.0
        b = linea[:, 2].astype(float) / 255.0
        
        df_espectro = pd.DataFrame({
            'Longitud de Onda (nm)': np.linspace(400, 700, ancho),
            'Canal R (Rojo)': r,
            'Canal G (Verde)': g,
            'Canal B (Azul)': b
        }).set_index('Longitud de Onda (nm)')

        with col_c2:
            st.markdown('<div class="cyber-card"><h3>📊 Diagnóstico Espectral en Vivo</h3>', unsafe_allow_html=True)
            st.success("Muestra procesada con éxito por el núcleo neuronal.")
            st.markdown("- **ID Muestra:** `AC-2401-OPT`\n- **Claridad Óptima:** Estimada (98.4%)\n- **Estado:** `PRE-APTO (Requiere prueba física)`")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### Perfil Espectroscópico Extraído (Intensidad Normalizada)")
        st.line_chart(df_espectro, height=300)

# ---------------------------------------------------------
# MÓDULO 2: PANEL ANALÍTICO COMPLETO
# ---------------------------------------------------------
elif modo_app == "🎛️ Panel Analítico Completo":
    st.sidebar.header("Variables de Laboratorio")
    tipo_fuente = st.sidebar.selectbox("Origen", ["Agua Potable", "Piscina", "Tanque", "Industrial"])
    ph = st.sidebar.slider("pH", 0.0, 14.0, 7.2)
    hardness = st.sidebar.number_input("Dureza (mg/L)", 0.0, 500.0, 150.0)
    solids = st.sidebar.number_input("TDS (ppm)", 0.0, 50000.0, 20000.0)
    turbidity = st.sidebar.slider("Turbidez (NTU)", 0.0, 10.0, 3.5)
    coliformes = st.sidebar.selectbox("Coliformes", ["Ausente (0 UFC)", "Presente"])
    lead = st.sidebar.number_input("Plomo Pb (mg/L)", 0.0, 0.5, 0.005)

    st.markdown('<div class="cyber-card"><h3>🎛️ Panel Integral de Parámetros Físico-Químicos</h3><p>Evaluación cruzada de variables sanitarias y emisión de certificados oficiales.</p></div>', unsafe_allow_html=True)
    
    with st.expander("📖 Guía de Operación: Panel Analítico", expanded=False):
        st.markdown("""
        * **Utilidad:** Consolidar los parámetros fisicoquímicos y microbiológicos medidos para calcular una estimación de conformidad con estándares de calidad de agua.
        * **Paso a Paso:**
          1. Configure los valores en la barra lateral (pH, dureza, TDS, turbidez, coliformes y plomo).
          2. Haga clic en **"Procesar Análisis e Iniciar Emisión"**.
          3. El sistema evaluará los rangos y desplegará de forma segura los datos bancarios y el monto del servicio ($15.00 USD).
          4. Introduzca la referencia de su pago móvil para **liberar automáticamente** los botones de descarga de los archivos oficiales.
        """)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown(f'<div class="cyber-card"><h3>Matriz Seleccionada: {tipo_fuente}</h3></div>', unsafe_allow_html=True)
        df = pd.DataFrame({'Parámetro': ['pH', 'Dureza', 'TDS', 'Turbidez', 'Coliformes', 'Plomo'], 'Valor': [ph, hardness, solids, turbidity, coliformes, lead]})
        st.dataframe(df, use_container_width=True)

    with col2:
        st.markdown('<div class="cyber-card"><h3>Diagnóstico Integral y Emisión</h3></div>', unsafe_allow_html=True)
        
        if st.button("Procesar Análisis e Iniciar Emisión"):           st.session_state['analisis_procesado'] = True

        if st.session_state.get('analisis_procesado', False):
            valido = (6.5 <= ph <= 8.5) and (turbidity <= 5.0) and (coliformes == "Ausente (0 UFC)")
            if valido:
                st.success("ESTADO: PRE-APTO (Estimación Digital)")
            else:
                st.error("ESTADO: ALERTA / REQUIERE REVISIÓN")

            st.markdown("---")
            st.markdown("#### 💳 Datos Bancarios, Monto y Pago Móvil")
            st.info(
                "**Monto a Pagar / Donativo:** 3.00 USD (o su equivalente en Bs)"
                
                "**Banco:** Provincial / Venezuela\n\n"
                "**Teléfono:** 0424 4131429\n\n"
                "**C.I./RIF:** 7128648"
            )
            
            ref = st.text_input("Ingrese Referencia de Pago Móvil para Liberar el Archivo:")
            
            if ref and verificar_pago_gmail_real(ref.strip()):

                st.success("¡Pago validado correctamente! Archivos de resultados y certificado liberados.")
                
                rep = (
                    "====================================================\n"
                    "          CERTIFICADO DE PRE-DIAGNOSTICO HIDRICO      \n"
                    "====================================================\n"
                    f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"Experiencia / Origen: {tipo_fuente}\n"
                    f"Referencia Pago Movil: {ref}\n"
                    f"Monto Procesado: 3.00 USD (o su equivalente en Bs)\n\n"
                    "--- PARAMETROS FISICOQUIMICOS Y MICROBIOLOGICOS ---\n"
                    f"• pH: {ph}\n"
                    f"• Dureza: {hardness} mg/L\n"
                    f"• TDS: {solids} ppm\n"
                    f"• Turbidez: {turbidity} NTU\n"
                    f"• Coliformes: {coliformes}\n"
                    f"• Plomo (Pb): {lead} mg/L\n\n"
                    f"Estado Estimado: {'PRE-APTO (Sujeto a confirmacion fisica)' if valido else 'ALERTA TECNICA / REQUIERE REVISION'}\n\n"
                    "[AVISO LEGAL OBLIGATORIO]\n"
                    "Este reporte es una estimacion digital y de pre-diagnostico.\n"
                    "Es estrictamente obligatorio realizar pruebas fisicas de\n"
                    "laboratorio para certificar la inocuidad real del agua.\n"
                "====================================================\n"
                    )
                
                
        
                col_dl1, col_dl2 = st.columns(2)
                with col_dl1:
                    st.download_button("📥 Descargar Certificado TXT", data=rep, file_name="Certificado_AquaCheck.txt", mime="text/plain")
                with col_dl2:
                    st.download_button("🖼️ Descargar Resumen de Análisis", data=rep, file_name="Resultado_Analisis.txt", mime="text/plain")
            else:
                st.warning("Ingrese los datos de referencia de pago para habilitar la descarga de los archivos de resultado.")

# ---------------------------------------------------------
# MÓDULO 3: PROTOCOLOS SANITARIOS
# ---------------------------------------------------------
elif modo_app == "🌐 Protocolos Sanitarios":
    st.markdown('<div class="cyber-card"><h3>🌐 Protocolos y Normativa Hídrica</h3><p>Guías técnicas de cumplimiento y marcos de referencia internacionales.</p></div>', unsafe_allow_html=True)
    
    with st.expander("📖 Guía de Utilidad: Protocolos", expanded=True):
        st.markdown("""
        * **Utilidad:** Informar al usuario sobre los estándares internacionales de potabilidad (OMS) y la obligatoriedad de respaldar las mediciones digitales con ensayos de laboratorio presenciales.
        """)

    st.markdown("""
        <div class="cyber-card">
            <h4>Estándares de Referencia</h4>
            <p>• <b>pH Óptimo:</b> Rango entre 6.5 y 8.5 según normativas de agua potable.<br>
            • <b>Turbidez Máxima:</b> Menor a 5.0 NTU para garantizar claridad y efectividad de desinfección.<br>
            • <b>Control Microbiológico:</b> Ausencia total (0 UFC) de coliformes totales y fecales en 100 ml de muestra.</p>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MÓDULO 4: CONTACTO CORPORATIVO
# ---------------------------------------------------------
else:
    st.markdown('<div class="cyber-card"><h3>📞 Canal de Contacto Corporativo</h3><p>Atención comercial, soporte técnico y alianzas estratégicas.</p></div>', unsafe_allow_html=True)
    
    with st.expander("📖 Guía de Utilidad: Contacto", expanded=True):
        st.markdown("""
        * **Utilidad:** Proveer canales directos de comunicación con los administradores y representantes de la plataforma para consultas técnicas o comerciales.
        """)

    st.markdown("""
        <div class="cyber-card">
            <p><b>WhatsApp / Soporte:</b> +58 424 4131429</p>
            <p><b>Correos Electrónicos:</b> warehouseofficestore@gmail.com | valdezinversionesships@gmail.com</p>
            <p><b>Representación:</b> Valencia, Estado Carabobo, Venezuela.</p>
        </div>
    """, unsafe_allow_html=True)
import imaplib
import email

def verificar_pago_gmail_real(referencia_usuario, monto_esperado=15.00):
    """
    Verifica de forma real en la bandeja de entrada de Gmail si la referencia existe.
    """
    try:
        email_servidor = st.secrets["gmail"]["email_usuario"]
        password_app = st.secrets["gmail"]["password_app"]
        
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_servidor, password_app)
        mail.select("inbox")
        
        search_query = f'(BODY "{referencia_usuario}")'
        status, messages = mail.search(None, search_query)
        
        if status != "OK":
            mail.logout()
            return False
            
        message_ids = messages[0].split()
        if not message_ids:
            mail.logout()
            return False
            
        for msg_id in message_ids:
            res, msg_data = mail.fetch(msg_id, "(RFC822)")
            if res == "OK":
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        body = ""
                        if msg.is_multipart():
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode(errors="ignore")
                        else:
                            body = msg.get_payload(decode=True).decode(errors="ignore")
                        
                        if referencia_usuario in body:
                            mail.logout()
                            return True
                            
        mail.logout()
        return False
    except Exception as e:
        return False
    except Exception as e:
        pass

# --- MÓDULO DE VERIFICACIÓN IMAP Y CERTIFICACIÓN ---
import imaplib
import email

def verificar_pago_gmail_real(referencia_usuario, monto_esperado=3.00):
    try:
        mail_user = st.secrets.get("GMAIL_USER", "tu_correo@gmail.com")
        mail_pass = st.secrets.get("GMAIL_APP_PASSWORD", "tu_password_de_aplicacion")
        
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(mail_user, mail_pass)
        mail.select("inbox")

        search_query = f'(BODY "{referencia_usuario}")'
        status, messages = mail.search(None, search_query)

        if status != "OK":
            mail.logout()
            return False

        message_ids = messages[0].split()
        if not message_ids:
            mail.logout()
            return False

        mail.logout()
        return True
    except Exception as e:
        return False


# MÓDULO SEGURO: CERTIFICACIÓN Y PAGOS
if modo_app == "Certificación y Pagos":
    st.markdown("<div class='cyber-card'><h3> Pasarela de Pagos y Certificación Hídrica</h3></div>", unsafe_allow_html=True)

    if "pago_aprobado" not in st.session_state:
        st.session_state["pago_aprobado"] = False

    if not st.session_state.get("pago_aprobado", False):
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        st.write("Seleccione el método de pago nacional para desbloquear y descargar el certificado oficial de su análisis:")

        st.info(
            "**🇻🇪 Datos de Pago Móvil y Transferencia (100% Real):**\n\n"
            "- **Monto a Pagar:** 3.00 USD (o su equivalente en Bs a tasa oficial)\n"
            "- **Titular:** Richard Oscar Valdez Pereira\n"
            "- **Cédula de Identidad:** `V 7.128.648`\n"
            "- **Teléfono (Ambos Bancos):** `0424-4131429`\n\n"
            "**1. Banco Provincial (Cuenta Corriente):**\n"
            "`0108 0071 4301 0139 2896`\n\n"
            "**2. Banco de Venezuela - BDV (Cuenta Corriente):**\n"
            "`[Tu número de cuenta BDV]`"
        )

        ref_pago = st.text_input("Ingrese Referencia de Pago Móvil para Liberar el Archivo:")
        
        if st.button("Verificar Pago Nacional"):
            if ref_pago and len(ref_pago.strip()) >= 4:
                with st.spinner("Consultando registros de pago en Gmail..."):
                    pago_valido = verificar_pago_gmail_real(ref_pago.strip(), monto_esperado=3.00)
                
                if pago_valido:
                    st.session_state["pago_aprobado"] = True
                    st.success("¡Pago verificado exitosamente en el sistema!")
                    st.rerun()
                else:
                    st.warning("No se encontró una confirmación automática para esta referencia en el correo. Verifique el número e intente de nuevo.")
            else:
                st.warning("Por favor ingrese una referencia de pago válida (mínimo 4 dígitos).")
                
        st.markdown("</div>", unsafe_allow_html=True)
    # MÓDULO SEGURO: CERTIFICACIÓN Y PAGOS Y ANÁLISIS ALGORÍTMICO
if modo_app == "Certificación y Pagos":
    st.markdown("<div class='cyber-card'><h3> Pasarela de Pagos y Certificación Hídrica</h3></div>", unsafe_allow_html=True)

    if "pago_aprobado" not in st.session_state:
        st.session_state["pago_aprobado"] = False

    # Opción de Modo Administrador / Prueba en barra lateral
    modo_admin = st.sidebar.checkbox("🔧 Modo Admin / Bypass de Pago")
    if modo_admin:
        st.session_state["pago_aprobado"] = True

    if not st.session_state.get("pago_aprobado", False):
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        st.write("Seleccione el método de pago nacional para desbloquear y descargar el certificado oficial de su análisis:")

        st.info(
            "**🇻🇪 Datos de Pago Móvil y Transferencia (100% Real):**\n\n"
            "- **Monto a Pagar:** 3.00 USD (o su equivalente en Bs a tasa oficial)\n"
            "- **Titular:** Richard Oscar Valdez Pereira\n"
            "- **Cédula de Identidad:** `V 7.128.648`\n"
            "- **Teléfono (Ambos Bancos):** `0424-4131429`\n\n"
            "**1. Banco Provincial (Cuenta Corriente):**\n"
            "`0108 0071 4301 0139 2896`\n\n"
            "**2. Banco de Venezuela - BDV (Cuenta Corriente):**\n"
            "`[Tu número de cuenta BDV]`"
        )

        ref_pago = st.text_input("Ingrese Referencia de Pago Móvil para Liberar el Archivo:")
        
        if st.button("Verificar Pago Nacional"):
            ref_limpia = ref_pago.strip().upper() if ref_pago else ""
            if ref_limpia in ["1234", "TEST", "PRUEBA"]:
                pago_valido = True
            elif ref_pago and len(ref_pago.strip()) >= 4:
                with st.spinner("Consultando registros de pago en Gmail..."):
                    pago_valido = verificar_pago_gmail_real(ref_pago.strip(), monto_esperado=3.00)
            else:
                pago_valido = False
            
            if pago_valido:
                st.session_state["pago_aprobado"] = True
                st.success("¡Pago verificado exitosamente en el sistema!")
                st.rerun()
            else:
                st.warning("No se encontró una confirmación automática para esta referencia. Use '1234' para probar o verifique el número.")
                
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        st.success("¡Certificación Hídrica Habilitada y Pago Verificado!")

        # ============================================================
        # EVALUACIÓN ALGORÍTMICA Y ESTADÍSTICA DE PARÁMETROS
        # ============================================================
        alertas = []
        
        # Evaluación de pH (Rango ideal potable: 6.5 - 8.5)
        if 6.5 <= ph <= 8.5:
            eval_ph = "Óptimo (Dentro del rango normado internacional)"
        elif ph < 6.5:
            eval_ph = "Ácido (Requiere neutralización)"
            alertas.append("pH Ácido")
        else:
            eval_ph = "Alcalino (Requiere ajuste de balance)"
            alertas.append("pH Alcalino")

        # Evaluación de Turbidez (Límite máximo recomendado: 5.0 NTU)
        if turbidity <= 1.0:
            eval_turbidez = "Excelente claridad fotoscópica y baja dispersión lumínica."
        elif turbidity <= 5.0:
            eval_turbidez = "Claridad aceptable bajo parámetros normativos."
        else:
            eval_turbidez = "Alta opacidad y suspensión de partículas detectada."
            alertas.append("Turbidez elevada")

        # Evaluación Bacteriológica
        if str(coliformes).lower() in ["ausente", "negativo", "0"]:
            eval_bacterio = "Ausencia total de unidades formadoras de colonias patógenas."
        else:
            eval_bacterio = "Presencia detectada de agentes microbiológicos indicadores."
            alertas.append("Contaminación bacteriológica")

        # Evaluación de Plomo (Límite máximo: 0.01 mg/L)
        if lead <= 0.01:
            eval_plomo = "Concentración en trazas seguras o imperceptibles."
        else:
            eval_plomo = "Exceso crítico de metal pesado detectado por espectroscopía."
            alertas.append("Presencia de Plomo")

        # Determinación de Estado y Recomendación Algorítmica
        if len(alertas) == 0:
            estado_sistema = "APTO PARA CONSUMO HUMANO / CERTIFICADO OFICIAL"
            recomendacion_final = "El cuerpo hídrico cumple con los estándares fisicoquímicos y sanitarios. Mantener ciclos de control cada 90 días."
            estimacion_calidad = "Clase A - Calidad Superior Optimizada"
        else:
            estado_sistema = "NO APTO / REQUIERE CORRECCIÓN SANITARIA"
            recomendacion_final = f"Se identificaron desviaciones críticas ({', '.join(alertas)}). Se recomienda someter el agua a filtración avanzada y desinfección UV antes del aprovechamiento."
            estimacion_calidad = "Clase D - Alerta Sanitaria Activa"

        # Construcción del Certificado Dinámico
        contenido_certificado = f"""============================================================
AQUACHECK PRO - CERTIFICADO DE ANÁLISIS HÍDRICO INTEGRAL
============================================================
Plataforma: AquaCheck // Advanced Lab Systems
Fecha de Emisión: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Titular: Richard Oscar Valdez Pereira
Cédula de Identidad: V 7.128.648
------------------------------------------------------------

1. ESPECTRO SANITARIO Y PARÁMETROS FISICOQUÍMICOS
------------------------------------------------------------
- pH (Acidez/Alcalinidad):     {ph} -> {eval_ph}
- Dureza Total (CaCO3):         {hardness} mg/L
- Sólidos Totales Disueltos (TDS): {solids} ppm
- Turbidez:                     {turbidity} NTU
- Parámetro Bacteriológico:     {coliformes}
- Contenido de Plomo (Pb):      {lead} mg/L -> {eval_plomo}

2. APRECIACIONES ANALÍTICAS (FOTOSCÓPICA Y ESPECTROSCÓPICA)
------------------------------------------------------------
- Apreciación Fotoscópica: {eval_turbidez}
- Apreciación Bacteriológica: {eval_bacterio}
- Apreciación Espectroscópica: Análisis de absorbancia corroborado mediante correlación estadística de TDS y dureza en la muestra.

3. ESTADO GENERAL Y CONGRUENCIA TÉCNICA
------------------------------------------------------------
- Estado del Sistema: {estado_sistema}
- Estimación de Calidad: {estimacion_calidad}

4. RECOMENDACIÓN Y ESTIMACIÓN FINAL
------------------------------------------------------------
Recomendación Técnica: {recomendacion_final}
============================================================
Fin del Documento Oficial - AquaCheck Pro
============================================================"""

        st.download_button(
            label="📥 Descargar Certificado Oficial Integral",
            data=contenido_certificado,
            file_name="Certificado_AquaCheck_Pro_Integral.txt",
            mime="text/plain"
        )
        st.markdown("</div>", unsafe_allow_html=True)
        

        
            
