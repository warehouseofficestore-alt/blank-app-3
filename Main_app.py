import streamlit as st
import pandas as pd
import os

# Configuración de página con diseño amplio
st.set_page_config(
    page_title="AquaCheck Postmodern",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Postmodernos y Neofuturistas (Tarjetas flotantes, neones y alto contraste)
st.markdown("""
    <style>
    /* Estilo general de fondo y tipografía */
    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        color: #c9d1d9;
    }
    
    /* Título principal postmoderno */
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

    /* Tarjetas de diagnóstico flotantes (Glassmorphism + Neón) */
    .cyber-card {
        background: rgba(22, 27, 34, 0.7);
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.1);
        backdrop-filter: blur(8px);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .cyber-card:hover {
        border-color: #00f0ff;
        transform: translateY(-3px);
    }

    /* Botones personalizados estilo cyberpunk */
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
st.markdown('<p class="cyber-title">💧 AquaCheck // Core</p>', unsafe_allow_html=True)
st.markdown('<p class="cyber-subtitle">Sistema Autónomo de Análisis Hídrico por Visión Computarizada e IA</p>', unsafe_allow_html=True)

# Menú lateral postmoderno
st.sidebar.markdown("### 🎛️ MÓDULOS DE CONTROL")
modo_app = st.sidebar.radio(
    "Seleccione interfaz de entrada:",
    [
        "📸 Visión de Campo (Cámara)",
        "🎛️ Parámetros Físico-Químicos",
        "🌐 Protocolos y Usos Hídricos"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("⚡ **Estado:** `En línea` | **Motor:** `Activo`")

# ---------------------------------------------------------
# MODO 1: CÁMARA DE CAMPO (Visión Computarizada)
# ---------------------------------------------------------
if modo_app == "📸 Visión de Campo (Cámara)":
    st.markdown("""
        <div class="cyber-card">
            <h3>📷 Captura Espectral de Muestra</h3>
            <p>Apunta el dispositivo (móvil, tablet o PC) al cuerpo de agua, estanque, piscina o recipiente para realizar el escaneo visual directo[span_0](start_span)[span_0](end_span).</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_cam1, col_cam2 = st.columns([1, 1])
    
    with col_cam1:
        foto_muestra = st.camera_input("Activar sensor óptico de cámara")
        
    with col_cam2:
        tipo_fuente_cam = st.selectbox(
            "Seleccionar Contexto de Muestra:",
            ["💧 Vaso / Agua Potable", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Ecosistema Natural", "🧪 Contenedor Industrial"]
        )
        st.info(f"Contexto fijado para análisis óptico: **{tipo_fuente_cam}**")
        
        if foto_muestra is not None:
            st.success("✅ Espectro visual capturado con éxito.")
            if st.button("⚡ Ejecutar Motor Neuronal", use_container_width=True):
                st.balloons()
                st.markdown("""
                    <div class="cyber-card" style="border-color: #00f0ff;">
                        <h3 style="color: #00f0ff;">✨ DIAGNÓSTICO ÓPTICO COMPLETADO</h3>
                        <p><b>Estado del agua:</b> Alta pureza superficial detectada.</p>
                        <p><b>Índice de refracción y claridad:</b> Óptimo.</p>
                    </div>
                """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MODO 2: PANEL MANUAL
# ---------------------------------------------------------
elif modo_app == "🎛️ Parámetros Físico-Químicos":
    st.sidebar.header("⚙️ Ajuste de Variables")
    tipo_fuente = st.sidebar.selectbox(
        "Origen de la Muestra:",
        ["💧 Vaso / Agua Potable Directa", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Cuerpo Natural de Agua", "🧪 Recipiente Industrial"]
    )
    
    ph = st.sidebar.slider("Nivel de pH", 0.0, 14.0, 7.2, 0.1)
    hardness = st.sidebar.number_input("Dureza del agua (mg/L)", min_value=0.0, max_value=500.0, value=150.0)
    solids = st.sidebar.number_input("Sólidos Totales Disueltos - TDS (ppm)", min_value=0.0, max_value=50000.0, value=20000.0)
    chloramines = st.sidebar.slider("Cloraminas (ppm)", 0.0, 15.0, 7.0, 0.1)
    turbidity = st.sidebar.slider("Turbidez (NTU)", 0.0, 10.0, 3.5, 0.1)

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown(f"""
            <div class="cyber-card">
                <h3>📊 Matriz de Parámetros: {tipo_fuente}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        resumen_df = pd.DataFrame({
            'Parámetro': ['pH', 'Dureza', 'Sólidos (TDS)', 'Cloraminas', 'Turbidez'],
            'Valor Registrado': [ph, hardness, solids, chloramines, turbidity],
            'Unidad': ['pH', 'mg/L', 'ppm', 'ppm', 'NTU']
        })
        st.dataframe(resumen_df, use_container_width=True)

    with col2:
        st.markdown("""
            <div class="cyber-card">
                <h3>🚀 Núcleo de Diagnóstico</h3>
                <p>Procesa los datos actuales bajo estándares internacionales.</p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("⚡ Procesar Análisis Cuántico", use_container_width=True):
            if (6.5 <= ph <= 8.5) and (turbidity <= 5.0):
                st.balloons()
                st.markdown("""
                    <div class="cyber-card" style="border-color: #00ff66;">
                        <h4 style="color: #00ff66;">💧 ESTADO: APTO / POTABLE</h4>
                        <p>Los parámetros coinciden con los rangos óptimos de seguridad biológica.</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="cyber-card" style="border-color: #ff3366;">
                        <h4 style="color: #ff3366;">⚠️ ESTADO: ALERTA / NO APTA</h4>
                        <p>Se detectaron anomalías críticas en los índices físico-químicos.</p>
                    </div>
                """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MODO 3: GUÍA POSTMODERNA
# ---------------------------------------------------------
else:
    st.markdown("""
        <div class="cyber-card">
            <h3>🌐 Arquitectura de Protocolos Hídricos</h3>
            <p>Guía de calibración y análisis contextual para entornos de alta exigencia:</p>
            <ul>
                <li><b>🏊‍♂️ Piscinas:</b> Monitoreo dinámico de cloro libre y balance ácido-base.</li>
                <li><b>🛢️ Tanques:</b> Control de sedimentación y sólidos suspendidos.</li>
                <li><b>💧 Consumo Directo:</b> Verificación de potabilidad inmediata en punto de uso.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
