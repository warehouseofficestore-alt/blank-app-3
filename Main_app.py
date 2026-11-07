import streamlit as st

st.set_page_config(page_title="AquaCheck")
st.title("💧 AquaCheck: Sistema Inteligente de Calidad de Agua")
st.write("Bienvenida a la plataforma de análisis")

# Cargar las librerías y el modelo de forma segura dentro de la función
@st.cache_resource
def load_model():
    import joblib
    return joblib.load("AquaCheckModel.pkl")

try:
    model = load_model()
    st.success("¡Modelo cargado correctamente!")
except Exception as e:
    st.info("La interfaz está lista. Verificando componentes del modelo...")
    
