import streamlit as st
import os

# Configuración de la página (Pestaña del navegador)
st.set_page_config(
    page_title="Overhauling Midlife Bike | Taller Tecnológico",
    page_icon="🚲",
    layout="wide"
)

# --- ESTILOS VISUALES ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .hero-title { font-size: 45px; font-weight: 700; text-align: center; color: #1E1E1E; margin-top: -20px; }
    .sub-title { font-size: 20px; text-align: center; color: #5E5E5E; margin-bottom: 30px; }
    .stButton>button { width: 100%; background-color: #007BFF; color: white; border-radius: 5px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. CABECERA ---
col_logo, col_nav = st.columns([1, 2])
with col_logo:
    st.markdown("### Overhauling Midlife Bike 🚲")
with col_nav:
    st.markdown("<p style='text-align: right; padding-top: 10px;'>Servicios | Paint Studio | Upgrades | Proyectos | Agendar</p>", unsafe_allow_html=True)

st.divider()

# --- 2. SECCIÓN HERO (BANNER PRINCIPAL) ---
# Usamos el nombre de archivo que definiste: fuji_mate_final.png
nombre_foto_principal = "fuji_mate_final.png"

if os.path.exists(nombre_foto_principal):
    st.image(nombre_foto_principal, use_container_width=True)
else:
    st.error(f"Archivo '{nombre_foto_principal}' no encontrado en GitHub. Por favor verifica que el nombre sea exacto.")
    st.info("Sube la imagen a GitHub con el nombre: fuji_mate_final.png")

st.markdown('<p class="hero-title">La Reconstrucción de tu Pasión</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Mecánica avanzada, pintura custom y upgrades tecnológicos para ciclistas de alto nivel en Chile.</p>', unsafe_allow_html=True)

if st.button("RESERVA TU DIAGNÓSTICO TÉCNICO PREMIUM"):
    st.balloons()
    st.success("¡Pronto habilitaremos la agenda en línea!")

st.markdown("<br>", unsafe_allow_html=True)

# --- 3. PROPUESTA DE VALOR ---
st.header("Por qué elegir OMB")
cv1, cv2, cv3 = st.columns(3)
with cv1:
    st.subheader("🛡️ Precisión")
    st.write("Ingeniería aplicada con herramientas de torque digital y los más altos estándares técnicos de fábrica.")
with cv2:
    st.subheader("🎨 Estética")
    st.write("Transformamos marcos de carbono en piezas únicas de colección con acabados de autor en nuestro Paint Studio.")
with cv3:
    st.subheader("🏁 ADN Competitivo")
    st.write("Especialistas en las exigencias técnicas del Triatlón, Ruta, MTB y Gravel de alta gama.")

st.divider()

# --- 4. SERVICIOS ---
st.header("Nuestros Servicios Especializados")
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("### Overhaul Mecánico")
    st.write("- Desarme íntegro del cuadro\n- Inspección de fatiga en carbono\n- Limpieza técnica profesional\n- Re-ensamblaje bajo normas de fábrica")
with s2:
    st.markdown("### Paint Studio")
    st.write("- Diseños personalizados únicos\n- Recuperación de acabados originales\n- Protección cerámica industrial\n- Acabados mate y gloss de alta durabilidad")
with s3:
    st.markdown("### Tech Upgrades")
    st.write("- Instalación de grupos electrónicos\n- Calibración de potenciómetros\n- Optimización de rendimiento\n- Diagnóstico de firmware")

st.divider()

# --- 5. SECCIÓN ANTES Y DESPUÉS ---
st.header("Caso de Éxito: Transformación Fuji")
st.write("Visualiza el nivel de detalle de nuestro trabajo (Imágenes de referencia OMB)")

col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Antes")
    # Puedes subir tu foto original como 'fuji_antes.png'
    if os.path.exists("fuji_antes.png"):
        st.image("fuji_antes.png", use_container_width=True)
    else:
        st.caption("Esperando archivo: fuji_antes.png")

with col_b:
    st.subheader("Después")
    # Aquí mostramos de nuevo el resultado final para el comparativo
    if os.path.exists("fuji_mate_final.png"):
        st.image("fuji_mate_final.png", use_container_width=True)
    else:
        st.caption("Esperando archivo: fuji_mate_final.png")

st.divider()

# --- 7. FORMULARIO DE CONTACTO ---
st.header("Agenda tu Diagnóstico")
with st.form("contacto_form"):
    nombre = st.text_input("Nombre y Apellido")
    correo = st.text_input("Email")
    tipo_bici = st.selectbox("Tipo de Bicicleta", ["Ruta", "MTB", "Gravel", "Triatlón"])
    interes = st.multiselect("Servicio de Interés", ["Overhaul Mecánico", "Pintura Custom", "Upgrades Electrónicos"])
    comentario = st.text_area("Detalles de tu bicicleta (Marca, modelo, año)")
    
    enviado = st.form_submit_button("Enviar Solicitud")
    if enviado:
        st.success(f"Gracias {nombre}, hemos recibido la información de tu {tipo_bici}. Nos contactaremos a {correo}.")

# --- 8. FOOTER ---
st.markdown("<br><hr><center>Overhauling Midlife Bike - Tecnología • Artesanía • Performance<br>Santiago, Chile</center>", unsafe_allow_html=True)
