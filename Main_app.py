import streamlit as st
import numpy as np
import pandas as pd
import time

# Configuración de página con estética neofuturista
st.set_page_config(
    page_title="Experiencia // Advanced Lab",
    page_icon="💧",
    layout="wide"
)

# Estilos CSS Neofuturistas (Interfaz oscura, neones y minimalismo táctico)
st.markdown("""
    <style>
    .stApp {
        background-color: #05070A;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    .neo-card {
        background: rgba(13, 20, 32, 0.7);
        border: 1px solid rgba(0, 243, 255, 0.2);
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.05);
        margin-bottom: 20px;
    }
    .neo-header {
        color: #00F3FF;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(0, 243, 255, 0.3);
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    .metric-hud {
        background: #0B1118;
        border-left: 3px solid #00F3FF;
        padding: 10px 15px;
        font-family: 'Courier New', monospace;
    }
    .secure-payment-box {
        background: linear-gradient(135deg, #0B1118 0%, #121E2C 100%);
        border: 1px solid #10B981;
        border-radius: 8px;
        padding: 20px;
        margin-top: 25px;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Título y HUD Principal
st.markdown("<h1 style='color: #00F3FF; font-weight: 800;'>EXPERIENCIA // NÚCLEO HÍDRICO</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #8A99AD; font-family: monospace;'>MÓDULO DE CERTIFICACIÓN ESPECTRAL Y DIAGNÓSTICO HIPERREALISTA</p>", unsafe_allow_html=True)

# Simulación de Estado de la Sesión
if 'fase_certificado' not in st.session_state:
    st.session_state.fase_certificado = False

# Sidebar Neofuturista para Controles y Sensibilidad
with st.sidebar:
    st.markdown("### ⚙️ HUD DE CALIBRACIÓN")
    st.markdown("---")
    ganancia_b = st.slider("Ganancia Canal B (Azul)", 0.5, 2.0, 1.0, 0.1)
    ganancia_g = st.slider("Ganancia Canal G (Verde)", 0.5, 2.0, 1.0, 0.1)
    ganancia_r = st.slider("Ganancia Canal R (Rojo)", 0.5, 2.0, 1.0, 0.1)
    umbral_ruido = st.selectbox("Filtro de Dispersión (Noise Filter)", ["Estándar", "Ultra-Preciso (Lab)", "Modo Campo"])
    
    st.markdown("---")
    if st.button("🚀 GENERAR CERTIFICADO OFICIAL", type="primary"):
        st.session_state.fase_certificado = True

# Contenedor Principal: Captura y Espectrograma
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("<div class='neo-card'>", unsafe_allow_html=True)
    st.markdown("<div class='neo-header'>📷 Sensor Óptico de Campo</div>", unsafe_allow_html=True)
    
    # Simulación de la entrada de cámara o captura
    camera_input = st.camera_input("Capturar Muestra Líquida en Tiempo Real")
    
    if camera_input:
        st.success("✔ Matriz óptica registrada con éxito.")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='neo-card'>", unsafe_allow_html=True)
    st.markdown("<div class='neo-header'>📈 Descomposición Cromática Espectral</div>", unsafe_allow_html=True)
    
    # Generación de datos simulados para el gráfico neofuturista con los factores de ganancia
    wavelengths = np.linspace(400, 700, 100)
    canal_b = (np.sin(wavelengths / 25) * 0.1 + 0.15) * ganancia_b
    canal_g = (np.sin(wavelengths / 28) * 0.12 + 0.13) * ganancia_g
    canal_r = (np.cos(wavelengths / 30) * 0.08 + 0.07) * ganancia_r
    
    chart_data = pd.DataFrame({
        'Longitud de Onda (nm)': wavelengths,
        'Canal B (Azul)': canal_b,
        'Canal G (Verde)': canal_g,
        'Canal R (Rojo)': canal_r
    }).set_index('Longitud de Onda (nm)')
    
    st.line_chart(chart_data, color=["#00F3FF", "#38BDF8", "#EF4444"])
    st.markdown("</div>", unsafe_allow_html=True)

# --- FASE DE EMISIÓN DE CERTIFICADO Y RESULTADOS ---
if st.session_state.fase_certificado:
    st.markdown("---")
    st.markdown("<div class='neo-card' style='border-color: #10B981;'>", unsafe_allow_html=True)
    st.markdown("<div class='neo-header' style='color: #10B981;'>🛡️ CERTIFICADO DE ANÁLISIS HÍDRICO EMITIDO</div>", unsafe_allow_html=True)
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.markdown("""
        * **Código de Registro:** EXP-2026-VAL-9042
        * **Clasificación Óptica:** Nivel 2 (Carga Moderada / Requiere Tratamiento Preventivo)
        * **Índice de Pureza Estimado:** 88.4%
        """)
    with col_res2:
        st.markdown("""
        * **Recomendación de Uso:** Se sugiere filtración por ósmosis o desinfección UV previa al consumo humano directo.
        * **Estado de Validación:** Aprobado para control de procesos industriales y riego tecnificado.
        """)
    
    # DATOS BANCARIOS Y PAGO MÓVIL (DESPLEGADOS EXCLUSIVAMENTE EN ESTA FASE FINAL)
    st.markdown("""
    <div class='secure-payment-box'>
        <h4 style='color: #10B981; margin-top: 0;'>💳 Pasarela de Emisión y Pago Móvil (Autorizado)</h4>
        <p style='font-size: 0.9rem; color: #94A3B8;'>Para descargar la certificación digital inalterable con firma criptográfica, utilice los siguientes canales de contraprestación autorizados:</p>
        <ul style='font-family: monospace; font-size: 0.95rem; color: #E2E8F0;'>
            <li><strong>Banco:</strong> (Banco Autorizado - Activo)</li>
            <li><strong>Pago Móvil:</strong> Teléfono: 0414-XXXXXXX | V-XXXXXXXX</li>
            <li><strong>Referencia Zelle / Transferencia:</strong> Disponible bajo solicitud cifrada</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
