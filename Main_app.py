import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="AquaCheck // Advanced Lab", page_icon="💧", layout="centered"
)

# Estilos CSS personalizados para la interfaz y contraste adaptativo
st.markdown(
    """
    <style>
        .main-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: inherit;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 0px;
        }
        .sub-title {
            font-size: 0.85rem;
            color: #64748b;
            margin-bottom: 20px;
        }
        .stButton>button {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- CABECERA PRINCIPAL ---
st.markdown(
    '<div class="main-title">💧 AQUACHECK // ADVANCED LAB</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">Plataforma de Certificación Hídrica con Perfil'
    " Bacteriológico y Trazas</div>",
    unsafe_allow_html=True,
)

# Inicializar estados si no existen
if "etapa" not in st.session_state:
    st.session_state.etapa = "captura"

# --- MÓDULO 1: CAPTURA ESPECTRAL ---
st.markdown("### 📷 Captura Espectral")
st.caption("Registre ópticamente la muestra.")

# Componente de cámara o carga de imagen
imagen_muestra = st.camera_input("Tome una foto de la muestra o sensor óptico")

if imagen_muestra is not None:
    st.success("Muestra registrada correctamente.")
    if st.button("Procesar Análisis Espectral"):
        st.session_state.etapa = "resultados"

# --- MÓDULO 2 Y 3: RESULTADOS Y EMISIÓN DE CERTIFICADO (Con datos bancarios seguros solo aquí) ---
if st.session_state.etapa == "resultados":
    st.markdown("---")
    st.markdown("### 📊 Resultados del Análisis")
    st.info(
        "Perfil bacteriológico y trazas procesadas con éxito. Generando"
        " certificado hídrica."
    )

    # Simulación de visualización de resultados
    st.write("**Parámetros evaluados:** pH, Turbidez, Conectividad, Coliformes.")

    st.markdown("---")
    st.markdown("### 💳 Emisión de Certificado y Datos de Pago")
    st.warning(
        "Para proceder con la emisión y descarga oficial del certificado,"
        " realice el pago mediante los siguientes datos bancarios:"
    )

    # Datos bancarios protegidos y desplegados únicamente en esta fase
    st.markdown(
        """
        - **Banco:** Banco Nacional / Pago Móvil
        - **Teléfono:** 0412-XXXXXXX
        - **C.I. / R.I.F.:** V-XXXXXXXX
        - **Monto:** Correspondiente a la certificación
        """
    )

    comprobante = st.file_uploader(
        "Subir capture o comprobante de pago móvil",
        type=["png", "jpg", "jpeg"],
    )

    if comprobante is not None:
        st.success(
            "¡Comprobante recibido! Su certificado digital está listo para"
            " descarga."
        )
        if st.button("📥 Descargar Certificado Oficial"):
            st.balloons()
            st.download_button(
                label="Descargar PDF de Certificación",
                data=b"Certificado digital AquaCheck",
                file_name="Certificado_Hidrico_AquaCheck.pdf",
                mime="application/pdf",
            )

# Botón para reiniciar proceso si es necesario
if st.session_state.etapa == "resultados":
    if st.button("🔄 Nueva Muestra"):
        st.session_state.etapa = "captura"
        st.rerun()
        
