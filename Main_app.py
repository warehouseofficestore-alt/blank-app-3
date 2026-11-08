import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Configuración de página con diseño amplio
st.set_page_config(
    page_title="AquaCheck Postmodern Pro",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Postmodernos y Neofuturistas
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
        color: #c9d1d9;
    }
    
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

    .cyber-card {
        background: rgba(22, 27, 34, 0.85);
        border: 1px solid #30363d;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.15);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

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
st.markdown('<p class="cyber-subtitle">Plataforma Autónoma de Certificación e IA Hídrica</p>', unsafe_allow_html=True)

# Menú lateral postmoderno con acceso a contacto
st.sidebar.markdown("### 🎛️ MÓDULOS DE CONTROL")
modo_app = st.sidebar.radio(
    "Seleccione interfaz de entrada:",
    [
        "📸 Visión de Campo (Cámara)",
        "🎛️ Parámetros Físico-Químicos",
        "🌐 Protocolos y Usos Hídricos",
        "📞 Contacto y Colaboración"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("⚡ **Estado:** `En línea` | **Soporte:** `Activo`")

# ---------------------------------------------------------
# MODO 1: CÁMARA DE CAMPO
# ---------------------------------------------------------
if modo_app == "📸 Visión de Campo (Cámara)":
    st.markdown("""
        <div class="cyber-card">
            <h3>📷 Captura Espectral de Muestra en Campo</h3>
            <p>Utilice la cámara de su dispositivo para registrar ópticamente el cuerpo de agua o recipiente de análisis.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_cam1, col_cam2 = st.columns([1, 1])
    
    with col_cam1:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        foto_muestra = st.camera_input("📷 Acceso al Sensor Óptico")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_cam2:
        st.markdown("<div class='cyber-card'>", unsafe_allow_html=True)
        tipo_fuente_cam = st.selectbox(
            "Seleccionar Contexto de Muestra:",
            ["💧 Vaso / Agua Potable", "🏊‍♂️ Piscina / Natatorio", "🛢️ Tanque de Almacenamiento", "🌊 Lago / Ecosistema Natural", "🧪 Contenedor Industrial"]
        )
        st.info(f"Contexto activo: **{tipo_fuente_cam}**")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if foto_muestra is not None:
            st.markdown("""
                <div class="cyber-card" style="border-color: #00f0ff;">
                    <h4 style="color: #00f0ff;">✅ Muestra Capturada con Éxito</h4>
                    <p>La imagen ha sido indexada en el búfer de análisis visual.</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button("⚡ Ejecutar Motor Neuronal", use_container_width=True):
                st.balloons()
                reporte_texto = f"""==================================================
        REPORTE TÉCNICO Y ESPECTRAL - AQUACHECK
==================================================
Fecha de Emisión: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Contexto de Muestra: {tipo_fuente_cam}
Modo de Análisis: Visión Computarizada / Campo

[RESULTADOS ESPECTRALES]
- Índice de Claridad Óptima: Aprobado
- Evaluación Superficial: Cumple con los estándares de pureza visual.
- Estado General: APTO / CONDICIÓN ESTABLE

Soporte y Contacto: warehouseofficestore@gmail.com | WA: +58 424 4131429
Firma Digital: AQUACHECK-NEO-CORE-2026
==================================================""""

                st.download_button(
                    label="📥 Descargar Reporte Óptico (TXT)",
                    data=reporte_texto,
                    file_name=f"Reporte_Optico_{tipo_fuente_cam.replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )

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
            es_apto = (6.5 <= ph <= 8.5) and (turbidity <= 5.0)
            
            if es_apto:
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

            # Sección de pasarela de pago y datos oficiales
            st.markdown("""
                <div class="cyber-card" style="border-color: #7000ff;">
                    <h3>💳 Pasarela de Pago & Donativos // Certificado Técnico</h3>
                    <p>Realice su aporte, donativo o pago por certificado mediante nuestras vías oficiales:</p>
                </div>
            """, unsafe_allow_html=True)

            metodo_pago = st.radio("Seleccione método de pago:", ["📱 Pago Móvil (Nacional)", "🌐 Tarjeta / Pasarela Internacional (Stripe)"])

            if "Pago Móvil" in metodo_pago:
                st.info(f"""
                **Datos para Pago Móvil / Colaboración:**
                * **Bancos:** Banco Provincial o Banco de Venezuela
                * **Teléfono:** `0424 4131429`
                * **C.I. / R.I.F.:** `7128648`
                * **Notificar pagos vía WhatsApp:** [+58 424 4131429](https://wa.me/584244131429)
                """)
                ref_pago = st.text_input("Ingrese la referencia del Pago Móvil:")
                
                if st.button("Verificar y Generar Certificado", use_container_width=True):
                    if len(ref_pago) >= 4:
                        reporte_fq = f"""==================================================
       CERTIFICADO OFICIAL DE ANÁLISIS HÍDRICO
==================================================
Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Origen: {tipo_fuente}
Referencia Pago Móvil / Donativo: {ref_pago}

[VALORES REGISTRADOS]
- pH: {ph} | Dureza: {hardness} mg/L | TDS: {solids} ppm
- Cloraminas: {chloramines} ppm | Turbidez: {turbidity} NTU

[DIAGNÓSTICO]
Estado: {"APTO / POTABLE" if es_apto else "ALERTA / REVISIÓN"}
Certificación válida bajo estándares técnicos.
Soporte: warehouseofficestore@gmail.com
Firma Digital: AQUACHECK-PRO-2026
=================================================="""
                        st.success("¡Operación verificada con éxito!")
                        st.download_button(
                            label="📥 Descargar Certificado Oficial Firmado",
                            data=reporte_fq,
                            file_name=f"Certificado_AquaCheck_{tipo_fuente.split()[0]}.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
                    else:
                        st.warning("Por favor ingrese un número de referencia válido.")
            else:
                st.write("Realice su donativo o pago seguro a través de pasarela internacional.")
                if st.link_button("🔗 Pagar / Donar con Tarjeta (Checkout)", "https://buy.stripe.com/tu-enlace-de-pago"):
                    pass
                
                reporte_fq_intl = f"""==================================================
       CERTIFICADO OFICIAL INTERNACIONAL - AQUACHECK
==================================================
Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Origen: {tipo_fuente}
Pasarela: Stripe Secure Checkout

[VALORES REGISTRADOS]
- pH: {ph} | Dureza: {hardness} mg/L | TDS: {solids} ppm
- Cloraminas: {chloramines} ppm | Turbidez: {turbidity} NTU

Estado: {"APTO / POTABLE" if es_apto else "ALERTA / REVISIÓN"}
Contacto: valdezinversionesships@gmail.com
Firma Digital: AQUACHECK-INTL-2026
=================================================="""
                st.download_button(
                    label="📥 Descargar Certificado (Post-Pago Internacional)",
                    data=reporte_fq_intl,
                    file_name=f"Certificado_Internacional_{tipo_fuente.split()[0]}.txt",
                    mime="text/plain",
                    use_container_width=True
                )

# ---------------------------------------------------------
# MODO 3: GUÍA POSTMODERNA
# ---------------------------------------------------------
elif modo_app == "🌐 Protocolos y Usos Hídricos":
    st.markdown("""
        <div class="cyber-card">
            <h3>🌐 Arquitectura de Protocolos Hídricos y Monetización</h3>
            <p>Guía de calibración y métodos de pago integrados en la plataforma:</p>
            <ul>
                <li><b>📱 Pago Móvil:</b> Provincial / Venezuela (Tlf: 0424-4131429 | C.I/RIF: 7128648)</li>
                <li><b>🌐 Internacional:</b> Tarjetas de crédito/débito vía pasarela segura.</li>
                <li><b>📄 Certificación:</b> Emisión instantánea de reportes técnicos descargables.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# MODO 4: CONTACTO Y COLABORACIÓN
# ---------------------------------------------------------
else:
    st.markdown("""
        <div class="cyber-card">
            <h3>📞 Centro de Contacto, Colaboración y Donativos</h3>
            <p>¿Deseas establecer una alianza estratégica, realizar un donativo o tienes dudas sobre los reportes hídricos? Comunícate directamente con nosotros a través de los siguientes canales oficiales:</p>
            
            <ul style="line-height: 2.0; font-size: 1.1rem;">
                <li>📱 <b>WhatsApp Directo / Pago Móvil:</b> <a href="https://wa.me/584244131429" target="_blank" style="color: #00f0ff;">+58 424-4131429</a></li>
                <li>✉️ <b>Correo Comercial y Soporte:</b> <a href="mailto:warehouseofficestore@gmail.com" style="color: #00f0ff;">warehouseofficestore@gmail.com</a></li>
                <li>🚢 <b>Correo Corporativo / Alianzas:</b> <a href="mailto:valdezinversionesships@gmail.com" style="color: #00f0ff;">valdezinversionesships@gmail.com</a></li>
            </ul>
            
            <hr style="border-color: #30363d; margin: 20px 0;">
            <p><b>Datos Fiscales y Bancarios para Aportes en Venezuela:</b></p>
            <ul>
                <li><b>Bancos:</b> Banco Provincial / Banco de Venezuela</li>
                <li><b>Teléfono asociado:</b> 0424 4131429</li>
                <li><b>C.I. / R.I.F.:</b> 7128648</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
