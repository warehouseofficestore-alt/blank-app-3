import streamlit as st
import pandas as pd
import joblib
import os

# Configuración de página moderna
st.set_page_config(
    page_title="AquaCheck Pro",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo visual moderno con CSS personalizado
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #0066cc;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-text {
        color: #555555;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0066cc;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown('<p class="main-title">💧 AquaCheck: Inteligencia Artificial Aplicada al Agua</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Plataforma avanzada de análisis predictivo de calidad y pureza hídrica.</p>', unsafe_allow_html=True)

# Carga segura del modelo de Machine Learning
@st.cache_resource
def load_ml_model():
    model_path = "AquaCheckModel.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

model = load_ml_model()

# Panel lateral moderno para los parámetros de entrada
st.sidebar.header("🎛️ Parámetros de Análisis")
st.sidebar.write("Ingrese los valores físico-químicos:")

ph = st.sidebar.slider("Nivel de pH", 0.0, 14.0, 7.2, 0.1)
hardness = st.sidebar.number_input("Dureza del agua (mg/L)", min_value=0.0, max_value=500.0, value=150.0)
solids = st.sidebar.number_input("Sólidos Totales Disueltos - TDS (ppm)", min_value=0.0, max_value=50000.0, value=20000.0)
chloramines = st.sidebar.slider("Cloraminas (ppm)", 0.0, 15.0, 7.0, 0.1)
sulfates = st.sidebar.number_input("Sulfatos (mg/L)", min_value=0.0, max_value=500.0, value=300.0)
conductivity = st.sidebar.number_input("Conductividad (μS/cm)", min_value=0.0, max_value=1000.0, value=400.0)
organic_carbon = st.sidebar.number_input("Carbón Orgánico Total (ppm)", min_value=0.0, max_value=30.0, value=10.0)
trihalomethanes = st.sidebar.number_input("Trihalometanos (μg/L)", min_value=0.0, max_value=120.0, value=60.0)
turbidity = st.sidebar.slider("Turbidez (NTU)", 0.0, 10.0, 3.5, 0.1)

# Cuerpo principal en columnas
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Resumen de Parámetros Seleccionados")
    input_data = pd.DataFrame({
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfates],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
    })
    st.dataframe(input_data, use_container_width=True)

with col2:
    st.subheader("⚙️ Estado del Sistema")
    if model is not None:
        st.success("Modelo de ML vinculado con éxito.")
        if st.button("🚀 Ejecutar Diagnóstico", type="primary", use_container_width=True):
            try:
                # Predicción usando el modelo cargado
                prediction = model.predict(input_data)
                probability = model.predict_proba(input_data) if hasattr(model, "predict_proba") else None
                
                st.markdown("---")
                if prediction[0] == 1 or prediction[0] == "Potable":
                    st.balloons()
                    st.success("### Resultado: AGUA POTABLE 💧")
                    st.write("El perfil hídrico cumple con los estándares óptimos de pureza y consumo.")
                else:
                    st.error("### Resultado: NO APTA / ALERTA ⚠️")
                    st.write("Los parámetros superan los límites recomendados de seguridad.")
                    
                if probability is not None:
                    confianza = max(probability[0]) * 100
                    st.info(f"Nivel de confianza del modelo: **{confianza:.2f}%**")
            except Exception as ex:
                st.warning(f"Nota de ejecución: El modelo requiere las características exactas de entrenamiento. ({ex})")
    else:
        st.warning("⚠️ No se encontró el archivo `AquaCheckModel.pkl` en el repositorio.")
        st.info("Sube tu modelo entrenado junto al código para habilitar la predicción automática.")
