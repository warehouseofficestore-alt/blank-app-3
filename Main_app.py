import subprocess
import sys

try:
    import joblib
    import sklearn
    import pandas
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "joblib", "scikit-learn", "pandas"])
    import joblib
    import sklearn
    import pandas

import streamlit as st

st.set_page_config(page_title="AquaCheck")
st.title("💧 AquaCheck: Sistema Inteligente de Calidad de Agua")
st.write("Bienvenida a la plataforma de análisis")

# Cargar el modelo entrenado de forma eficiente
@st.cache_resource
def load_model():
    return joblib.load("AquaCheckModel.pkl")

try:
    model = load_model()
    st.success("¡Modelo cargado correctamente!")
except Exception as e:
    st.error(f"No se pudo cargar el modelo: {e}")
    
