import streamlit as st

# Configuración de página o estilos generales si usas custom CSS
st.markdown(
    """
    <style>
        .main-title {
            font-size: 1.4rem;
            font-weight: 700;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 0px;
        }
        .sub-title {
            font-size: 0.9rem;
            color: #94a3b8;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- CABECERA ESTILIZADA ---
st.markdown(
    '<div class="main-title">💧 AQUACHECK // ADVANCED LAB</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-title">Plataforma de Certificación Hídrica con Perfil'
    " Bacteriológico y Trazas</div>",
    unsafe_allow_html=True,
)

# --- MÓDULOS CON ICONOS ---
# Ejemplo para el módulo de Captura Espectral manteniendo tus avances funcionales
st.markdown("### 📷 Captura Espectral")
st.caption("Registre ópticamente la muestra.")

# Aquí continúa tu lógica de componentes, cámara o subida de archivos...
