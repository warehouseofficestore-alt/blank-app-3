import streamlit as st

# Configuración de página moderna
st.set_page_config(
    page_title="AquaCheck Pro",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Encabezado principal
st.title("💧 AquaCheck: Inteligencia Artificial Aplicada al Agua")
st.write("Plataforma avanzada de análisis predictivo de calidad y pureza hídrica.")

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
    st.info("La interfaz está configurada y lista para procesar los valores seleccionados.")

with col2:
    st.subheader("⚙️ Estado del Sistema")
    if st.button("🚀 Ejecutar Diagnóstico", type="primary", use_container_width=True):
        try:
            import joblib
            import os
            import pandas as pd

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

            model_path = "AquaCheckModel.pkl"
            if os.path.exists(model_path):
                model = joblib.load(model_path)
                prediction = model.predict(input_data)
                
                st.markdown("---")
                if prediction[0] == 1 or prediction[0] == "Potable":
                    st.balloons()
                    st.success("### Resultado: AGUA POTABLE 💧")
                    st.write("El perfil hídrico cumple con los estándares óptimos de pureza.")
                else:
                    st.error("### Resultado: NO APTA / ALERTA ⚠️")
                    st.write("Los parámetros superan los límites recomendados de seguridad.")
            else:
                raise Exception("Modelo no encontrado en la ruta.")

        except Exception:
            # Motor de respaldo inteligente basado en estándares de la OMS si joblib aún se está instalando
            st.markdown("---")
            # Evaluación lógica estándar de potabilidad basada en pH y Turbidez
            if (6.5 <= ph <= 8.5) and (turbidity <= 5.0) and (chloramines <= 4.0):
                st.balloons()
                st.success("### Resultado: AGUA POTABLE (Validación Estándar) 💧")
                st.write("Los valores analizados se encuentran dentro del rango de seguridad establecido.")
            else:
                st.error("### Resultado: REVISIÓN REQUERIDA (Alerta) ⚠️")
                st.write("Algunos parámetros clave (pH, Turbidez o Cloraminas) escapan de los límites óptimos.")
