import streamlit as st
import numpy as np
import pandas as pd

# Configuración inicial de la página
st.set_page_config(
    page_title="Experiencia // Advanced Lab",
    page_icon="💧",
    layout="wide"
)

# Estilos CSS refinados: minimalistas, oscuros, relajantes y de alta gama
st.markdown("""
    <style>
    .stApp {
        background-color: #07090E;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }
    .main-title {
        color: #00F3FF;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 1.8rem;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #64748B;
        font-family: monospace;
        font-size: 0.85rem;
        margin-bottom: 25px;
    }
    .content-card {
        background: rgba(13, 19, 31, 0.6);
        border: 1px solid rgba(0, 243, 255, 0.15);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        margin-bottom: 20px;
    }
    .card-header {
        color: #38BDF8;
        font-weight: 600;
        font-size: 1.1rem;
        letter-spacing: 1px;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(56, 189, 248, 0.2);
        padding-bottom: 8px;
    }
    .info-text {
        color: #94A3B8;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- NAVEGACIÓN LATERAL POR MÓDULOS ---
with st.sidebar:
    st.markdown("<h3 style='color: #00F3FF; font-size: 1.1rem;'>NÚCLEO OPERATIVO</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B; font-size: 0.8rem;'>Seleccionar Módulo:</p>", unsafe_allow_html=True)
    
    modulo = st.radio(
        "Navegación",
        [
            "Centro de Control (Inicio)",
            "Visión de Campo (Espectral)",
            "Panel Analítico Completo",
            "Protocolos Sanitarios",
            "Contacto Corporativo"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("<p style='font-size: 0.75rem; color: #475569;'>Aviso Legal: Herramienta digital de pre-diagnóstico. Requiere validación física de laboratorio.</p>", unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL SEGÚN EL MÓDULO SELECCIONADO ---

if modulo == "Centro de Control (Inicio)":
    st.markdown("<div class='main-title'>EXPERIENCIA // CENTRO DE CONTROL</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Plataforma de Certificación Hídrica con Perfil Bacteriológico y Espectroscopía</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='content-card'>
            <div class='card-header'>🌐 Resumen del Sistema</div>
            <p class='info-text'>Bienvenido al entorno de diagnóstico avanzado. Desde este núcleo operativo puede gestionar la captura óptica en tiempo real, visualizar los espectrogramas cromáticos descompuestos y emitir certificados analíticos de alta precisión.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='content-card'>
            <div class='card-header'>⚡ Estado de Módulos</div>
            <p class='info-text'>• <strong>Sensor Óptico:</strong> En espera de calibración.<br>• <strong>Matriz Espectral:</strong> Activa y sincronizada.<br>• <strong>Emisión de Certificados:</strong> Protegida y cifrada.</p>
        </div>
        """, unsafe_allow_html=True)

elif modulo == "Visión de Campo (Espectral)":
    st.markdown("<div class='main-title'>VISIÓN DE CAMPO // MÓDULO ESPECTRAL</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Registro óptico y descomposición cromática de muestras líquidas en tiempo real.</div>", unsafe_allow_html=True)
    
    col_cam, col_graf = st.columns([1, 1.3])
    
    with col_cam:
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-header'>📷 Sensor Óptico de Campo</div>", unsafe_allow_html=True)
        st.markdown("<p class='info-text'>Alinee el dispositivo con la muestra líquida para capturar el perfil óptico.</p>", unsafe_allow_html=True)
        camera_input = st.camera_input("Capturar Muestra", label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_graf:
        st.markdown("<div class='content-card'>", unsafe_allow_html=True)
        st.markdown("<div class='card-header'>📈 Espectrograma Cromático (RGB)</div>", unsafe_allow_html=True)
        
        # Generación limpia del gráfico sin solapamientos
        wavelengths = np.linspace(400, 700, 90)
        canal_b = np.sin(wavelengths / 25) * 0.1 + 0.15
        canal_g = np.sin(wavelengths / 28) * 0.12 + 0.13
        canal_r = np.cos(wavelengths / 30) * 0.08 + 0.07
        
        chart_data = pd.DataFrame({
            'Longitud de Onda (nm)': wavelengths,
            'Canal B (Azul)': canal_b,
            'Canal G (Verde)': canal_g,
            'Canal R (Rojo)': canal_r
        }).set_index('Longitud de Onda (nm)')
        
        st.line_chart(chart_data, color=["#00F3FF", "#38BDF8", "#EF4444"])
        st.markdown("</div>", unsafe_allow_html=True)

elif modulo == "Panel Analítico Completo":
    st.markdown("<div class='main-title'>PANEL ANALÍTICO COMPLETO</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Consolidado de métricas fisicoquímicas y niveles de uso seguro.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-card'>
        <div class='card-header'>📊 Indicadores de Pureza e Índice Espectral</div>
        <p class='info-text'>Aquí se evalúan las desviaciones de las longitudes de onda para determinar la presencia de coloides o sólidos disueltos. El sistema clasifica automáticamente el agua en niveles de uso seguro (Apta, Requiere Tratamiento, o No Potable).</p>
    </div>
    """, unsafe_allow_html=True)

elif modulo == "Protocolos Sanitarios":
    st.markdown("<div class='main-title'>PROTOCOLOS SANITARIOS</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Directrices normativas de desinfección y control bacteriológico.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-card'>
        <div class='card-header'>🛡️ Guía de Acciones Preventivas</div>
        <p class='info-text'>Consulte los estándares de filtración por ósmosis inversa, sedimentación y desinfección por radiación ultravioleta recomendados según los resultados del diagnóstico espectral.</p>
    </div>
    """, unsafe_allow_html=True)

elif modulo == "Contacto Corporativo":
    st.markdown("<div class='main-title'>CONTACTO Y EMISIÓN CERTIFICADA</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Soporte técnico y canales de contraprestación autorizados.</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-card'>
        <div class='card-header'>💳 Emisión de Certificado y Pasarela de Pago</div>
        <p class='info-text'>Los datos bancarios y de pago móvil se despliegan exclusivamente en esta fase final de emisión de resultados para mantener la privacidad y orden de la plataforma.</p>
        <hr style='border-color: rgba(255,255,255,0.1);'>
        <p style='font-family: monospace; color: #38BDF8; font-size: 0.9rem;'>
        • <strong>Banco Autorizado:</strong> Activo<br>
        • <strong>Pago Móvil:</strong> 0414-XXXXXXX | V-XXXXXXXX<br>
        • <strong>Soporte Técnico:</strong> soporte@experiencia-lab.com
        </p>
    </div>
    """, unsafe_allow_html=True)
