import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Overhauling Midlife Bike | Taller Tecnológico",
    page_icon="🚲",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .hero-text {
        font-size: 50px !important;
        font-weight: 700;
        color: #1E1E1E;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-text {
        font-size: 24px !important;
        text-align: center;
        color: #5E5E5E;
        margin-bottom: 30px;
    }
    .service-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007BFF;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .disclaimer {
        font-size: 12px;
        color: #888;
        font-style: italic;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. CABECERA ---
col1, col2 = st.columns([1, 3])
with col1:
    # Aquí puedes poner tu logo una vez que lo tengas como archivo
    st.title("OMB 🚲") 
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Servicios | Paint Studio | Upgrades | Proyectos | Agendar")

st.divider()

# --- 2. SECCIÓN HERO ---
st.markdown('<p class="hero-text">Overhauling Midlife Bike</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Ingeniería y Estética para tu Pasión</p>', unsafe_allow_html=True)

# Imagen Hero de Referencia (Usamos la de laboratorio que creamos)
st.image("https://jodkxjuvwmvbg.ok.kimi.link/path-to-your-hero-image.jpg", 
         caption="Imagen de referencia: Laboratorio Tecnológico OMB", 
         use_container_width=True)

st.markdown("""
    <div style='text-align: center;'>
        <h4>Mecánica avanzada, pintura custom y upgrades tecnológicos para ciclistas de alto nivel en Chile.</h4>
        <br>
    </div>
    """, unsafe_allow_html=True)

if st.button("RESERVA TU DIAGNÓSTICO TÉCNICO PREMIUM", use_container_width=True):
    st.info("Función de reserva en desarrollo para la versión beta.")

st.markdown("<br>", unsafe_allow_html=True)

# --- 3. PROPUESTA DE VALOR ---
st.header("Por qué elegir Overhauling Midlife Bike")
cv1, cv2, cv3 = st.columns(3)

with cv1:
    st.subheader("🛡️ Precisión")
    st.write("No es solo mecánica; es ingeniería aplicada con herramientas de torque digital y estándares de fábrica.")

with cv2:
    st.subheader("🎨 Estética")
    st.write("Nuestro Paint Studio transforma marcos de carbono en piezas únicas de colección con acabados de autor.")

with cv3:
    st.subheader("🏁 ADN Competitivo")
    st.write("Especialistas en las exigencias del Triatlón, Ruta, MTB y Gravel de alta gama.")

st.divider()

# --- 4. SERVICIOS DE ESPECIALIDAD ---
st.header("Nuestros Servicios")
s1, s2, s3 = st.columns(3)

with s1:
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("Overhaul Mecánico")
    st.write("""
    - Desarme íntegro del cuadro.
    - Inspección de fatiga en carbono.
    - Limpieza con los más altos estándares técnicos.
    - Re-ensamblaje bajo normas de torque de fábrica.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with s2:
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("Paint Studio")
    st.write("""
    - Diseños personalizados únicos.
    - Recuperación de acabados originales.
    - Protección cerámica industrial.
    - Acabados mate y gloss de alta durabilidad.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with s3:
    st.markdown('<div class="service-card">', unsafe_allow_html=True)
    st.subheader("Tech Upgrades")
    st.write("""
    - Instalación de grupos electrónicos (Di2, AXS).
    - Integración y calibración de potenciómetros.
    - Optimización de rendimiento para competencia.
    - Actualización de firmware y diagnóstico.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- 5. SHOWROOM (IMÁGENES DE REFERENCIA) ---
st.header("The Lab: Proyectos de Referencia")
st.write("Nota: Las siguientes imágenes son referenciales del estándar de calidad OMB.")

g1, g2 = st.columns(2)
with g1:
    st.image("https://via.placeholder.com/600x400?text=Referencia+Pintura+Custom", caption="Diseño de Autor en Cuadro de Carbono (Referencia)")
with g2:
    st.image("https://via.placeholder.com/600x400?text=Referencia+Upgrade+Electronico", caption="Integración de Componentes Electrónicos (Referencia)")

st.markdown('<p class="disclaimer">*Galería con proyectos reales en construcción.</p>', unsafe_allow_html=True)

# --- 6, 7 y 8. PROCESO, RESERVA Y FOOTER ---
with st.expander("NUESTRO PROCESO TÉCNICO"):
    st.write("""
    1. **Recepción y Escaneo:** Evaluación profunda del estado actual.
    2. **Plan de Mejora:** Definición de upgrades y diseño de pintura.
    3. **Ejecución:** Intervención en laboratorio especializado.
    4. **Entrega Certificada:** Prueba de torque y ajuste final.
    """)

st.divider()

st.header("Agendar Servicio")
with st.form("contacto"):
    name = st.text_input("Nombre Completo")
    email = st.text_input("Correo Electrónico")
    tipo_bici = st.selectbox("Tipo de Bicicleta", ["Ruta", "MTB", "Gravel", "Triatlón"])
    servicio = st.multiselect("Servicio de Interés", ["Overhaul Mecánico", "Paint Studio", "Tech Upgrades"])
    mensaje = st.text_area("Cuéntanos sobre tu bicicleta")
    submit = st.form_submit_button("Enviar Solicitud")
    
    if submit:
        st.success(f"Gracias {name}, hemos recibido tu solicitud para tu bicicleta de {tipo_bici}.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; border-top: 1px solid #ddd; padding-top: 20px;'>
        <p><strong>Overhauling Midlife Bike</strong> - Santiago, Chile</p>
        <p>Tecnología • Artesanía • Performance</p>
    </div>
    """, unsafe_allow_html=True)