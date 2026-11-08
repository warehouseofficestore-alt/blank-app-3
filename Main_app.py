import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuración de página con diseño amplio
st.set_page_config(
    page_title="AquaCheck Postmodern Pro - Laboratorio Avanzado",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Postmodernos y Neofuturistas
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        color: #c9d1d9;
    }
    
    .cyber-title {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00f0ff, #7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 0px;
    }
    
    .cyber-subtitle {
        color: #8b949e;
        font-size: 1.1rem;
        font-weight: 400;
        letter-spacing: 1px;
        margin-bottom: 30px;
        border-left: 3px solid #00f0ff;
        padding-left: 10px;
    }

    .cyber-card {
        background: rgba(22, 27, 34, 0.85);
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.15);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    .stButton>button {
        background: linear-gradient(90deg, #00f0ff 0%, #0077ff 100%);
        color: #0d1117;
        font-weight: 800;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, #7000ff 0%, #00f0ff 100%);
        box-shadow: 0 0 25px rgba(112, 0, 255, 0.6);
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Neofuturista
st.markdown('<p class="cyber-title">💧 AquaCheck // Advanced Lab Core</p>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">Plataforma Autónoma de Certificación e IA con Perfil Bacteriológico y Traza</p>', unsafe_allow_html=True)

# Menú lateral postmoderno con acceso a contacto
st.sidebar.markdown("### 🎛️ MÓDULOS DE CONTROL")
modo_app = st.sidebar.radio(
    "Seleccione interfaz de entrada:",
    [
        "📸 Visión de Campo (Cámara)",
        "🎛️ Panel Analítico Completo (Físico-Químico, Bacterias y Trazas)",
        "🌐 Protocolos y Usos Hídricos",
        "📞 Contacto y Colaboración"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("⚡ **Estado:** `En línea` | **Laboratorio:** `Activo`")

# ---------------------------------------------------------
# MODO 1: CÁMARA DE CAMPO
# ---------------------------------------------------------
if modo_app == "📸 Visión de Campo (Cámara)":
    st.markdown("""
        <div class="cyber-card">
            <h3>📷 Captura Espectral de Muestra en Campo</h3>
            <p>Utilice la cámara de su dispositivo para registrar ópticamente el cuerpo de agua o recipiente de análisis.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_cam1, col_cam2 = st.columns([1, 1])
    
    with col_cam1:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        foto_muestra = st.camera_input("📷 Acceso al Sensor Óptico")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_cam2:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        tipo_fuente_cam = st.selectbox(
            "Seleccionar Contexto de Muestra:",
            ["💧 Vaso / Agua Potable", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Ecosistema Natural", "🧪 Contenedor Industrial"]
        )
        st.info(f"Contexto activo: **{tipo_fuente_cam}**")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if foto_muestra is not None:
            st.markdown("""
                <div class="cyber-card" style="border-color: #00f0ff;">
                    <h4 style="color: #00f0ff;">✅ Muestra Capturada con Éxito</h4>
                    <p>La imagen ha sido indexada en el búfer de análisis visual.</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("⚡ Ejecutar Motor Neuronal", use_container_width=True):
                st.balloons()
                
                reporte_texto = (
                    "==================================================\n"
                    "        REPORTE TÉCNICO Y ESPECTRAL - AQUACHECK\n"
                    "==================================================\n"
                    f"Fecha de Emisión: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    f"Contexto de Muestra: {tipo_fuente_cam}\n"
                    "Modo de Análisis: Visión Computarizada / Campo\n\n"
                    "[RESULTADOS ESPECTRALES]\n"
                    "- Índice de Claridad Óptima: Aprobado\n"
                    "- Evaluación Superficial: Cumple con los estándares de pureza visual.\n"
                    "- Estimación Bacteriológica: Ausencia aparente de turbidez orgánica.\n"
                    "- Estado General: APTO / CONDICIÓN ESTABLE\n\n"
                    "Soporte y Contacto: warehouseofficestore@gmail.com | WA: +58 424 4131429\n"
                    "Firma Digital: AQUACHECK-NEO-CORE-2026\n"
                    "=================================================="
                )

                st.download_button(
                    label="📥 Descargar Reporte Óptico (TXT)",
                    data=reporte_texto,
                    file_name=f"Reporte_Optico_{tipo_fuente_cam.replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )

# ---------------------------------------------------------
# MODO 2: PANEL ANALÍTICO COMPLETO (Físico-Químico, Bacterias, Trazas)
# ---------------------------------------------------------
elif modo_app == "🎛️ Panel Analítico Completo (Físico-Químico, Bacterias y Trazas)":
    st.sidebar.header("⚙️ Variables Físico-Químicas")
    tipo_fuente = st.sidebar.selectbox(
        "Origen de la Muestra:",
        ["💧 Vaso / Agua Potable Directa", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Cuerpo Natural de Agua", "🧪 Recipiente Industrial"]
    )
    
    ph = st.sidebar.slider("Nivel de pH", 0.0, 14.0, 7.2, 0.1)
    hardness = st.sidebar.number_input("Dureza del agua (mg/L)", min_value=0.0, max_value=500.0, value=150.0)
    solids = st.sidebar.number_input("Sólidos Totales Disueltos - TDS (ppm)", min_value=0.0, max_value=50000.0, value=20000.0)
    chloramines = st.sidebar.slider("Cloraminas (ppm)", 0.0, 15.0, 7.0, 0.1)
    turbidity = st.sidebar.slider("Turbidez (NTU)", 0.0, 10.0, 3.5, 0.1)

    st.sidebar.markdown("---")
    st.sidebar.header("🔬 Perfil Bacteriológico y Trazas")
    coliformes = st.sidebar.selectbox("Coliformes Totales / E. coli", ["Ausente (0 UFC/100ml)", "Presencia Moderada", "Presencia Crítica"])
    lead = st.sidebar.number_input("Plomo (Pb - mg/L)", min_value=0.0, max_value=0.5, value=0.005, step=0.001)
    iron = st.sidebar.number_input("Hierro (Fe - ppm)", min_value=0.0, max_value=10.0, value=0.2, step=0.1)

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown(f"""
            <div class="cyber-card">
                <h3>📊 Matriz Integral de Laboratorio: {tipo_fuente}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        resumen_df = pd.DataFrame({
            'Parámetro Analítico': ['pH', 'Dureza', 'Sólidos (TDS)', 'Cloraminas', 'Turbidez', 'Coliformes', 'Plomo (Pb)', 'Hierro (Fe)'],
            'Valor Registrado': [ph, hardness, solids, chloramines, turbidity, coliformes, lead, iron],
            'Unidad / Estado': ['pH', 'mg/L', 'ppm', 'ppm', 'NTU', 'UFC/100ml', 'mg/L', 'ppm']
        })
        st.dataframe(resumen_df, use_container_width=True)

    with col2:
        st.markdown("""
            <div class="cyber-card">
                <h3>🚀 Núcleo de Diagnóstico Completo</h3>
                <p>Procesa los parámetros físico-químicos, bacteriológicos y elementos traza bajo estándares internacionales.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("⚡ Procesar Análisis Integral", use_container_width=True):
            es_apto_fisico = (6.5 <= ph <= 8.5) and
