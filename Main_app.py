impor    st.success("¡Operación verificada con éxito!")
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
