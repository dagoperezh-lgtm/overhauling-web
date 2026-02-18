import streamlit as st
import os

# Configuración de la página
st.set_page_config(
    page_title="Overhauling Midlife Bike | Taller Tecnológico",
    page_icon="🚲",
    layout="wide"
)

# --- 1. ESTILOS Y PALETA DE COLORES ---
# Azul OMB: #007BFF | Negro: #1E1E1E | Gris: #F5F5F5
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Contenedor del Banner con Texto Superpuesto */
    .hero-container {
        position: relative;
        text-align: center;
        color: white;
    }
    
    .hero-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(0, 0, 0, 0.6); /* Fondo oscuro para resaltar texto */
        padding: 40px;
        border-radius: 15px;
        width: 80%;
    }
    
    .hero-title {
        font-size: 64px !important;
        font-weight: 800 !important;
        color: #ffffff;
        margin-bottom: 10px;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 28px !important;
        color: #007BFF; /* Usando nuestro Azul OMB */
        font-weight: 500;
    }

    .section-header {
        font-size: 32px;
        font-weight: 700;
        color: #1E1E1E;
        border-bottom: 3px solid #007BFF;
        margin-bottom: 25px;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CABECERA ---
col_logo, col_nav = st.columns([1, 2])
with col_logo:
    st.markdown("### Overhauling Midlife Bike 🚲")
with col_nav:
    st.markdown("<p style='text-align: right; padding-top: 10px; font-weight: bold;'>Servicios | Paint Studio | Upgrades | Proyectos | Agendar</p>", unsafe_allow_html=True)

# --- 3. SECCIÓN HERO (BANNER CON TEXTO DESTACADO) ---
nombre_foto_principal = "fuji_mate_final.png"

if os.path.exists(nombre_foto_principal):
    # Creamos el efecto de texto sobre la imagen
    st.markdown(f"""
        <div class="hero-container">
            <img src="https://raw.githubusercontent.com/tu-usuario/overhauling-web/main/{nombre_foto_principal}" style="width:100%; border-radius: 15px;">
            <div class="hero-overlay">
                <div class="hero-title">La Reconstrucción de tu Pasión</div>
                <div class="hero-subtitle">Mecánica avanzada, pintura custom y upgrades tecnológicos para ciclistas de alto nivel en Chile</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    # Si no estás en la nube aún, usamos el método estándar para que no falle localmente
    st.error("Para ver el diseño final con texto superpuesto, el archivo debe estar en GitHub. Mostrando versión local:")
    st.image(nombre_foto_principal, use_container_width=True)
    st.markdown('<div class="hero-title" style="color:#1E1E1E; text-align:center;">La Reconstrucción de tu Pasión</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle" style="text-align:center;">Mecánica avanzada, pintura custom y upgrades tecnológicos para ciclistas de alto nivel en Chile</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- 4. PROPUESTA DE VALOR ---
st.markdown('<div class="section-header">Por qué elegir OMB</div>', unsafe_allow_html=True)
cv1, cv2, cv3 = st.columns(3)
with cv1:
    st.markdown("#### 🛡️ Precisión")
    st.write("Ingeniería aplicada con torque digital y estándares de fábrica.")
with cv2:
    st.markdown("#### 🎨 Estética")
    st.write("Marcos de carbono transformados en piezas únicas de autor.")
with cv3:
    st.markdown("#### 🏁 ADN Competitivo")
    st.write("Especialistas en Triatlón y Ruta de alta gama.")

st.divider()

# --- 5. SECCIÓN ANTES Y DESPUÉS ---
st.markdown('<div class="section-header">Caso de Éxito: Transformación Fuji</div>', unsafe_allow_html=True)
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Antes")
    if os.path.exists("fuji_antes.png"):
        st.image("fuji_antes.png", use_container_width=True)
with col_b:
    st.subheader("Después")
    if os.path.exists("fuji_mate_final.png"):
        st.image("fuji_mate_final.png", use_container_width=True)

# --- 6. AGENDAR ---
st.markdown('<div class="section-header">Agenda tu Diagnóstico</div>', unsafe_allow_html=True)
with st.form("contacto_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Nombre y Apellido")
        correo = st.text_input("Email")
    with col_f2:
        tipo_bici = st.selectbox("Tipo de Bicicleta", ["Ruta", "MTB", "Gravel", "Triatlón"])
        interes = st.multiselect("Servicio", ["Overhaul", "Pintura", "Upgrades"])
    
    enviado = st.form_submit_button("ENVIAR SOLICITUD DE REVISIÓN")
    if enviado:
        st.success("Solicitud recibida. Nos contactaremos en menos de 24 horas.")

st.markdown("<br><hr><center>Overhauling Midlife Bike - Tecnología • Artesanía • Performance<br>Santiago, Chile</center>", unsafe_allow_html=True)
