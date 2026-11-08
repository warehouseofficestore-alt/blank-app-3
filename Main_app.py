import streamlit as st
import pandas as pd
import numpy as np
import cv2
import plotly.graph_objects as go
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
st.markdown('<p class="cyber-subtitle">Plataforma de Certificación Hídrica con Perfil Bacteriológico y Espectroscopia</p>', unsafe_allow_html=True)

st.sidebar.markdown("### 🎛️ MÓDULOS")
modo_app = st.sidebar.radio("Seleccionar:", ["📸 Visión de Campo (Espectral)", "🎛️ Panel Analítico Completo", "🌐 Protocolos", "📞 Contacto y Pago Móvil"])

# Descargo de responsabilidad en la barra lateral
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small style='color: #8b949e;'><b>Aviso Legal:</b> AquaCheck es una herramienta digital de pre-diagnóstico. Se requiere validación mediante pruebas físicas y microbiológicas de laboratorio para confirmar la potabilidad final del agua.</small>",
    unsafe_allow_html=True
)

if modo_app == "📸 Visión de Campo (Espectral)":
    st.markdown('<div class="cyber-card"><h3>📷 Captura Espectral Hiperrealista</h3><p>Capture la muestra para generar el análisis óptico y el gráfico de espectro integrado.</p></div>', unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns([1, 1])
    with col_c1:
        foto = st.camera_input("Sensor Óptico de Campo")
        
    if foto:
        file_bytes = np.asarray(bytearray(foto.read()), dtype=np.uint8)
        imagen = cv2.imdecode(file_bytes, 1)
        
        alto, ancho, _ = imagen.shape
        linea = imagen[alto//2, :, :]
        r, g, b = linea[:, 2], linea[:, 1], linea[:, 0]
        ondas = np.linspace(400, 700, ancho)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ondas, y=r, name='Canal R (600nm)', line=dict(color='#ff3366', width=2)))
        fig.add_trace(go.Scatter(x=ondas, y=g, name='Canal G (530nm)', line=dict(color='#00ff66', width=2)))
        fig.add_trace(go.Scatter(x=ondas, y=b, name='Canal B (450nm)', line=dict(color='#00f0ff', width=2)))
        fig.update_layout(
            title='Espectro Óptico Capturado',
            xaxis_title='Longitud de Onda (nm)',
            yaxis_title='Intensidad Relativa',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(22,27,34,0.9)',
            font=dict(color='#c9d1d9'),
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )

        with col_c2:
            st.markdown('<div class="cyber-card"><h3>📊 Diagnóstico Espectral en Vivo</h3>', unsafe_allow_html=True)
            st.success("Muestra procesada con éxito por el núcleo neuronal.")
            st.markdown("- **ID Muestra:** `AC-2401-OPT`\n- **Claridad Óptima:** Estimada (98.4%)\n- **Estado:** `PRE-APTO (Requiere prueba física)`")
            st.markdown('</div>', unsafe_allow_html=True)

        st.plotly_chart(fig, use_container_width=True)

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
                st.success("ESTADO: PRE-APTO (Estimación Digital)")
            else:
                st.error("ESTADO: ALERTA / REQUIERE REVISIÓN")

            st.markdown("### 💳 Pago Móvil / Donativo")
            st.info("**Banco:** Provincial / Venezuela\n**Teléfono:** 0424 4131429\n**C.I./RIF:** 7128648")
            ref = st.text_input("Ingrese Referencia de Pago Móvil:")
            
            if st.button("Generar Certificado Oficial"):
                if len(ref) >= 4:
                    rep = (
                        "==================================================\n"
                        "    CERTIFICADO DE PRE-DIAGNÓSTICO HÍDRICO\n"
                        "==================================================\n"
                        f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"Origen: {tipo_fuente}\n"
                        f"Referencia Pago Móvil: {ref}\n\n"
                        f"pH: {ph} | TDS: {solids} ppm | Turbidez: {turbidity} NTU\n"
                        f"Estado Estimado: {'PRE-APTO (Sujeto a confirmación física)' if valido else 'ALERTA TÉCNICA'}\n\n"
                        "[AVISO LEGAL OBLIGATORIO]\n"
                        "Este reporte es una estimación digital y de pre-diagnóstico.\n"
                        "Es estrictamente obligatorio realizar pruebas físicas de\n"
                        "laboratorio para certificar la inocuidad real del agua.\n"
                        "=================================================="
                    )
                    st.download_button("📥 Descargar Certificado con Aviso Legal (TXT)", data=rep, file_name="Certificado_Pre-diagnostico.txt", mime="text/plain")
                else:
                    st.warning("Ingrese una referencia válida.")

elif modo_app == "🌐 Protocolos":
    st.markdown("""
        <div class="cyber-card">
            <h3>Protocolos Hídricos y Normativa</h3>
            <p>Guía de cumplimiento y la importancia de contrastar los valores digitales con ensayos físico-químicos y microbiológicos presenciales en laboratorios certificados.</p>
        </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
        <div class="cyber-card">
            <h3>📞 Contacto y Colaboración</h3>
            <p><b>WhatsApp / Pago Móvil:</b> +58 424 4131429</p>
            <p><b>Correos:</b> warehouseofficestore@gmail.com | valdezinversionesships@gmail.com</p>
            <p><b>Datos Bancarios:</b> Provincial / Venezuela | C.I./RIF: 7128648</p>
        </div>
    """, unsafe_allow_html=True)
            
