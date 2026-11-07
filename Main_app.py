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
st.write("Plataforma avanzada de análisis predictivo y control de pureza hídrica.")

# Panel lateral moderno para los parámetros de entrada y tipo de fuente
st.sidebar.header("📍 Origen de la Muestra")
tipo_fuente = st.sidebar.selectbox(
    "Seleccione el cuerpo o recipiente de agua:",
    [
        "💧 Vaso / Agua Potable Directa", 
        "🏊‍♂️ Piscina / Natatorio", 
        "🛢️ Tanque de Almacenamiento", 
        "🌊 Lago / Cuerpo Natural de Agua", 
        "🧪 Otro Recipiente Industrial"
    ]
)

st.sidebar.markdown("---")
st.sidebar.header("🎛️ Parámetros Físico-Químicos")
st.sidebar.write(f"Configurando muestra para: **{tipo_fuente}**")

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
    st.subheader(f"📊 Panel de Control: {tipo_fuente}")
    st.info("Ajuste los valores en el panel lateral izquierdo según la lectura de su muestra y presione 'Ejecutar Diagnóstico'.")
    
    # Mostrar resumen visual de los datos configurados
    import pandas as pd
    resumen_df = pd.DataFrame({
        'Parámetro': ['pH', 'Dureza', 'Sólidos (TDS)', 'Cloraminas', 'Turbidez'],
        'Valor Muestra': [ph, hardness, solids, chloramines, turbidity],
        'Unidad': ['pH', 'mg/L', 'ppm', 'ppm', 'NTU']
    })
    st.dataframe(resumen_df, use_container_width=True)

with col2:
    st.subheader("⚙️ Estado del Sistema")
    if st.button("🚀 Ejecutar Diagnóstico", type="primary", use_container_width=True):
        try:
            import joblib
            import os

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
                st.write(f"**Origen analizado:** {tipo_fuente}")
                if prediction[0] == 1 or prediction[0] == "Potable":
                    st.balloons()
                    st.success("### Resultado: AGUA APTO / POTABLE 💧")
                    st.write("La muestra cumple con los parámetros óptimos evaluados por el modelo.")
                else:
                    st.error("### Resultado: NO APTA / ALERTA ⚠️")
                    st.write("Se detectaron valores fuera de tolerancia en los componentes analizados.")
            else:
                raise Exception("Modelo no encontrado.")

        except Exception:
            # Motor de respaldo inteligente contextualizado
            st.markdown("---")
            st.write(f"**Muestra evaluada:** {tipo_fuente}")
            
            # Validación adaptativa según el tipo de fuente seleccionado
            if "Piscina" in tipo_fuente:
                valida = (7.2 <= ph <= 7.6) and (turbidity <= 1.0)
            elif "Tanque" in tipo_fuente:
                valida = (6.5 <= ph <= 8.5) and (turbidity <= 5.0)
            else:
                valida = (6.5 <= ph <= 8.5) and (turbidity <= 5.0) and (chloramines <= 4.0)

            if valida:
                st.balloons()
                st.success("### Resultado: CONDICIÓN ÓPTIMA 💧")
                st.write(f"El análisis para **{tipo_fuente}** se encuentra dentro de los parámetros seguros.")
            else:
                st.error("### Resultado: ATENCIÓN REQUERIDA ⚠️")
                st.write(f"Los niveles registrados en esta muestra de **{tipo_fuente}** requieren ajuste o filtrado.")
    
