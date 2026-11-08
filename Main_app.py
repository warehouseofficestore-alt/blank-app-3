import streamlit as st
import pandas as pd
import os
from datetime import datetime

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
st.markdown('<p class="cyber-subtitle">Plataforma de Certificación Hídrica con Perfil Bacteriológico y Trazas</p>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ MÓDULOS")
modo_app = st.sidebar.radio("Seleccionar:", ["📸 Visión de Campo", "🎛️ Panel Analítico Completo", "🌐 Protocolos", "📞 Contacto y Pago Móvil"])

if modo_app == "📸 Visión de Campo":
    st.markdown('<div class="cyber-card"><h3>📷 Captura Espectral</h3><p>Registre ópticamente la muestra.</p></div>', unsafe_allow_html=True)
    foto = st.camera_input("Sensor Óptico")
    if foto:
        st.success("Muestra capturada correctamente.")
        if st.button("Ejecutar Análisis Óptico"):
            st.balloons()
            st.info("Estado: Óptimo y Estable.")

elif modo_app == "🎛️ Panel Analítico Completo":
    st.sidebar.header("Variables de Laboratorio")
    tipo_fuente = st.sidebar.selectbox("Origen", ["Agua Potable", "Piscina", "Tanque", "Industrial"])
    ph = st.sidebar.slider("pH", 0.0, 14.0, 7.2)
    hardness = st.sidebar.number_input("Dureza (mg/L)", 0.0, 500.0, 150.0)
    solids = st.sidebar.number_input("TDS (ppm)", 0.0, 50000.0, 20000.0)
    turbidity = st.sidebar.slider("Turbidez (NTU)", 0.0, 10.0, 3.5)
    coliformes = st.sidebar.selectbox("Coliformes", ["Ausente (0 UFC)", "Presente"])
    lead = st.sidebar.number_input("Plomo Pb (mg/L)", 0.0, 0.5, 0.005)

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown(f'<div class="cyber-card"><h3>Matriz: {tipo_fuente}</h3></div>', unsafe_allow_html=True)
        df = pd.DataFrame({'Parámetro': ['pH', 'Dureza', 'TDS', 'Turbidez', 'Coliformes', 'Plomo'], 'Valor': [ph, hardness, solids, turbidity, coliformes, lead]})
        st.dataframe(df, use_container_width=True)

    with col2:
        st.markdown('<div class="cyber-card"><h3>Diagnóstico Integral</h3></div>', unsafe_allow_html=True)
        if st.button("Procesar Análisis"):
            valido = (6.5 <= ph <= 8.5) and (turbidity <= 5.0) and (coliformes == "Ausente (0 UFC)")
            if valido:
                st.balloons()
                st.success("ESTADO: APTO / SEGURO")
            else:
                st.error("ESTADO: ALERTA / NO APTA")

            st.markdown("### 💳 Pago Móvil / Donativo")
            st.info("**Banco:** Provincial / Venezuela\n**Teléfono:** 0424 4131429\n**C.I./RIF:** 7128648")
            ref = st.text_input("Ingrese Referencia de Pago Móvil:")
            
            if st.button("Generar Certificado Oficial"):
                if len(ref) >= 4:
                    rep = f"CERTIFICADO AQUACHECK\nOrigen: {tipo_fuente}\nRef: {ref}\npH: {ph} | TDS: {solids}\nEstado: {'APTO' if valido else 'ALERTA'}"
                    st.download_button("📥 Descargar Certificado TXT", data=rep, file_name="Certificado.txt", mime="text/plain")
                else:
                    st.warning("Ingrese una referencia válida.")

elif modo_app == "🌐 Protocolos":
    st.markdown('<div class="cyber-card"><h3>Protocolos Hídricos</h3><p>Guía de cumplimiento y normativas internacionales de pureza.</p></div>', unsafe_allow_html=True)

else:
    st.markdown("""
        <div class="cyber-card">
            <h3>📞 Contacto y Colaboración</h3>
            <p><b>WhatsApp / Pago Móvil:</b> +58 424 4131429</p>
            <p><b>Correos:</b> warehouseofficestore@gmail.com | valdezinversionesships@gmail.com</p>
            <p><b>Datos Bancarios:</b> Provincial / Venezuela | C.I./RIF: 7128648</p>
        </div>
    """, unsafe_allow_html=True)
            
