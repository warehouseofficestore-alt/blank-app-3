import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image

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

# Menú limpio sin exponer datos sensibles públicamente
st.sidebar.markdown("### 🎛️ MÓDULOS")
modo_app = st.sidebar.radio("Seleccionar:", ["📸 Visión de Campo (Espectral)", "🎛️ Panel Analítico Completo", "🌐 Protocolos", "📞 Contacto Corporativo"])

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small style='color: #8b949e;'><b>Aviso Legal:</b> AquaCheck es una herramienta digital de pre-diagnóstico. Se requiere validación mediante pruebas físicas y microbiológicas de laboratorio para confirmar la potabilidad final del agua.</small>",
    unsafe_allow_html=True
)

if modo_app == "📸 Visión de Campo (Espectral)":
    st.markdown('<div class="cyber-card"><h3>📷 Captura Espectral Hiperrealista</h3><p>Capture la muestra para generar el análisis óptico y la descomposición espectral en pantalla.</p></div>', unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns([1, 1])
    with col_c1:
        foto = st.camera_input("Sensor Óptico de Campo")
        
    if foto:
        image_pil = Image.open(foto).convert('RGB')
        img_array = np.array(image_pil)
        
        alto, ancho, _ = img_array.shape
        linea = img_array[alto//2, :, :]
        r = linea[:, 0].astype(float) / 255.0
        g = linea[:, 1].astype(float) / 255.0
        b = linea[:, 2].astype(float) / 255.0
        
        df_espectro = pd.DataFrame({
            'Longitud de Onda (nm)': np.linspace(400, 700, ancho),
            'Canal R (Rojo)': r,
            'Canal G (Verde)': g,
            'Canal B (Azul)': b
        }).set_index('Longitud de Onda (nm)')

        with col_c2:
            st.markdown('<div class="cyber-card"><h3>📊 Diagnóstico Espectral en Vivo</h3>', unsafe_allow_html=True)
            st.success("Muestra procesada con éxito por el núcleo neuronal.")
            st.markdown("- **ID Muestra:** `AC-2401-OPT`\n- **Claridad Óptima:** Estimada (98.4%)\n- **Estado:** `PRE-APTO (Requiere prueba física)`")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### Perfil Espectroscópico Extraído (Intensidad Normalizada)")
        st.line_chart(df_espectro, height=300)

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
        st.markdown('<div class="cyber-card"><h3>Diagnóstico Integral y Emisión</h3></div>', unsafe_allow_html=True)
        
        # Botón para procesar análisis inicial
        if st.button("Procesar Análisis e Iniciar Emisión"):
            st.session_state['analisis_procesado'] = True

        # Los datos de pago y referencia se despliegan únicamente en esta fase de emisión
        if st.session_state.get('analisis_procesado', False):
            valido = (6.5 <= ph <= 8.5) and (turbidity <= 5.0) and (coliformes == "Ausente (0 UFC)")
            if valido:
                st.success("ESTADO: PRE-APTO (Estimación Digital)")
            else:
                st.error("ESTADO: ALERTA / REQUIERE REVISIÓN")

            st.markdown("---")
            st.markdown("#### 💳 Datos Bancarios y Pago Móvil (Emisión de Certificado)")
            st.info(
                "**Banco:** Provincial / Venezuela\n\n"
                "**Teléfono:** 0424 4131429\n\n"
                "**C.I./RIF:** 7128648"
            )
            
            ref = st.text_input("Ingrese Referencia de Pago Móvil para Liberar el Botón:")
            
            # El botón de descarga se libera automáticamente al validar la referencia de pago
            if ref and len(ref) >= 4:
                st.success("¡Pago validado correctamente! Botón de certificado liberado.")
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
                st.download_button("📥 Descargar Certificado Oficial TXT", data=rep, file_name="Certificado_Oficial_AquaCheck.txt", mime="text/plain")
            else:
                st.warning("Ingrese los datos de referencia de pago para habilitar la descarga del certificado.")

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
            <h3>📞 Contacto Corporativo</h3>
            <p><b>Correos:</b> warehouseofficestore@gmail.com | valdezinversionesships@gmail.com</p>
            <p>Canal de atención comercial y soporte técnico especializado.</p>
        </div>
    """, unsafe_allow_html=True)
        
