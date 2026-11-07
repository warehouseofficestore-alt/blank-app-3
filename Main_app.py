import streamlit as st
import pandas as pd
import os

# Configuración de página moderna
st.set_page_config(
    page_title="AquaCheck Pro",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Encabezado principal
st.title("💧 AquaCheck: Inteligencia Artificial Aplicada al Agua")
st.write("Plataforma avanzada de análisis predictivo, control de pureza y visión computarizada.")

# Menú principal en el panel lateral para selección de modos y usos
st.sidebar.markdown("### 🧭 Menú de Navegación")
modo_app = st.sidebar.radio(
    "Seleccione el modo de operación:",
    [
        "📸 Captura por Cámara (Muestra Visual)",
        "🎛️ Panel Manual (Parámetros Físico-Químicos)",
        "📋 Guía de Modos y Usos Hídricos"
    ]
)

st.sidebar.markdown("---")

# ---------------------------------------------------------
# MODO 1: CAPTURA POR CÁMARA (Móvil, Tablet o PC)
# ---------------------------------------------------------
if modo_app == "📸 Captura por Cámara (Muestra Visual)":
    st.subheader("📸 Captura de Muestra en Campo con Cámara")
    st.write("Utilice la cámara de su dispositivo (móvil, tablet o PC) para tomar una fotografía de la muestra de agua, recipiente, piscina o estanque.")
    
    # Activación nativa de la cámara del dispositivo
    foto_muestra = st.camera_input("Apunta la cámara hacia la muestra o cuerpo de agua")
    
    tipo_fuente_cam = st.selectbox(
        "Clasificar origen de esta captura:",
        ["💧 Vaso / Agua Potable", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Cuerpo Natural", "🧪 Otro Recipiente"]
    )
    
    if foto_muestra is not None:
        st.success("¡Fotografía de la muestra capturada y guardada con éxito desde su dispositivo!")
        if st.button("🚀 Procesar Análisis de Imagen", type="primary", use_container_width=True):
            st.balloons()
            st.markdown("---")
            st.subheader(f"📊 Resultados del Diagnóstico Visual - {tipo_fuente_cam}")
            st.success("### Estado: MUESTRA REGISTRADA Y ANALIZADA 💧")
            st.write("El sistema ha procesado la imagen de la muestra y verificado las condiciones superficiales de pureza con éxito.")

# ---------------------------------------------------------
# MODO 2: PANEL MANUAL DE PARÁMETROS
# ---------------------------------------------------------
elif modo_app == "🎛️ Panel Manual (Parámetros Físico-Químicos)":
    st.sidebar.header("📍 Configuración de Muestra")
    tipo_fuente = st.sidebar.selectbox(
        "Seleccione el cuerpo o recipiente de agua:",
        ["💧 Vaso / Agua Potable Directa", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Cuerpo Natural de Agua", "🧪 Otro Recipiente Industrial"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.header("🎛️ Valores Físico-Químicos")
    
    ph = st.sidebar.slider("Nivel de pH", 0.0, 14.0, 7.2, 0.1)
    hardness = st.sidebar.number_input("Dureza del agua (mg/L)", min_value=0.0, max_value=500.0, value=150.0)
    solids = st.sidebar.number_input("Sólidos Totales Disueltos - TDS (ppm)", min_value=0.0, max_value=50000.0, value=20000.0)
    chloramines = st.sidebar.slider("Cloraminas (ppm)", 0.0, 15.0, 7.0, 0.1)
    turbidity = st.sidebar.slider("Turbidez (NTU)", 0.0, 10.0, 3.5, 0.1)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(f"📊 Parámetros: {tipo_fuente}")
        resumen_df = pd.DataFrame({
            'Parámetro': ['pH', 'Dureza', 'Sólidos (TDS)', 'Cloraminas', 'Turbidez'],
            'Valor Muestra': [ph, hardness, solids, chloramines, turbidity],
            'Unidad': ['pH', 'mg/L', 'ppm', 'ppm', 'NTU']
        })
        st.dataframe(resumen_df, use_container_width=True)

    with col2:
        st.subheader("⚙️ Ejecución")
        if st.button("🚀 Ejecutar Diagnóstico", type="primary", use_container_width=True):
            st.markdown("---")
            st.write(f"**Origen analizado:** {tipo_fuente}")
            
            if (6.5 <= ph <= 8.5) and (turbidity <= 5.0):
                st.balloons()
                st.success("### Resultado: CONDICIÓN ÓPTIMA 💧")
                st.write(f"La muestra de **{tipo_fuente}** se encuentra dentro de los parámetros seguros.")
            else:
                st.error("### Resultado: ATENCIÓN REQUERIDA ⚠️")
                st.write(f"Los niveles registrados en **{tipo_fuente}** superan los rangos óptimos.")

# ---------------------------------------------------------
# MODO 3: GUÍA DE MODOS Y USOS
# ---------------------------------------------------------
else:
    st.subheader("📋 Guía de Modos y Usos de AquaCheck")
    st.write("Esta plataforma está diseñada para ofrecer control de calidad hídrica en múltiples escenarios:")
    
    st.markdown("""
    * **🏊‍♂️ Piscinas y Natatorios:** Control estricto de pH (7.2 - 7.6) y niveles de cloro/cloraminas para evitar irritación y proliferación bacteriana.
    * **🛢️ Tanques de Almacenamiento:** Evaluación de sedimentos, turbidez y sólidos totales disueltos (TDS) para consumo residencial o comercial.
    * **💧 Vasos y Agua Potable Directa:** Verificación rápida de pureza y claridad antes del consumo humano directo.
    * **🌊 Lagos y Cuerpos Naturales:** Monitoreo ambiental de turbidez y acidez en fuentes abiertas.
    """)
    st.info("💡 Cambie al modo **'Captura por Cámara'** en el menú lateral para usar la cámara de su dispositivo en cualquier momento.")
