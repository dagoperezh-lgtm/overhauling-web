import streamlit as st
import os

# Configuración de la página
st.set_page_config(
    page_title="Overhauling Midlife Bike | Taller Tecnológico",
    page_icon="🚲",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Estilo para el Mensaje Principal Destacado */
    .highlight-container {
        text-align: center;
        padding: 60px 20px;
        background-color: #ffffff;
    }
    
    .main-title {
        font-size: 72px !important;
        font-weight: 800 !important;
        color: #1E1E1E;
        margin-bottom: 20px;
        line-height: 1.1;
        letter-spacing: -1px;
    }
    
    .main-subtitle {
        font-size: 32px !important;
        color: #007BFF; /* Azul OMB */
        font-weight: 400;
        max-width: 900px;
        margin: 0 auto;
        line-height: 1.4;
    }

    .section-header {
        font-size: 28px;
        font-weight: 700;
        color: #1E1E1E;
        margin-top: 40px;
        margin-bottom: 20px;
        border-bottom: 2px solid #007BFF;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. CABECERA ---
col_logo, col_nav = st.columns([1, 2])
with col_logo:
    st.markdown("### Overhauling Midlife Bike 🚲")
with col_nav:
    st.markdown("<p style='text-align: right; padding-top: 10px; font-weight: bold;'>Servicios | Paint Studio | Upgrades | Proyectos | Agendar</p>", unsafe_allow_html=True)

# --- 2. BANNER PRINCIPAL ---
# Usamos tu foto fuji_mate_final.png que ya ajustaste manualmente
nombre_foto_principal = "fuji_mate_final.png"

if os.path.exists(nombre_foto_principal):
    st.image(nombre_foto_principal, use_container_width=True)
else:
    st.warning(f"Esperando archivo: {nombre_foto_principal}")

# --- 3. MENSAJE DESTACADO (FUENTES AGRANDADAS) ---
st.markdown(f"""
    <div class="highlight-container">
        <div class="main-title">La Reconstrucción de tu Pasión</div>
        <div class="main-subtitle">
            Mecánica avanzada, pintura custom y upgrades tecnológicos <br>
            para ciclistas de alto nivel en Chile.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- 4. PROPUESTA DE VALOR ---
st.markdown('<div class="section-header">Por qué elegir OMB</div>', unsafe_allow_html=True)
cv1, cv2, cv3 = st.columns(3)
with cv1:
    st.markdown("#### 🛡️ Precisión")
    st.write("Ingeniería aplicada con torque digital y los más altos estándares técnicos de fábrica.")
with cv2:
    st.markdown("#### 🎨 Estética")
    st.write("Transformamos marcos de carbono en piezas únicas de autor en nuestro Paint Studio.")
with cv3:
    st.markdown("#### 🏁 ADN Competitivo")
    st.write("Especialistas en las exigencias técnicas del Triatlón, Ruta y MTB de alta gama.")

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
st.markdown('<div class="section-header">Agenda tu Diagnóstico Técnico</div>', unsafe_allow_html=True)
with st.form("contacto_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Nombre y Apellido")
        correo = st.text_input("Email")
    with col_f2:
        tipo_bici = st.selectbox("Tipo de Bicicleta", ["Ruta", "MTB", "Gravel", "Triatlón"])
        interes = st.multiselect("Servicio de Interés", ["Overhaul", "Pintura", "Upgrades"])
    
    enviado = st.form_submit_button("SOLICITAR REVISIÓN PROFESIONAL")
    if enviado:
        st.success(f"Gracias {nombre}. Nos contactaremos a {correo} para coordinar la recepción.")

# --- 7. FOOTER ---
st.markdown("<br><hr><center>Overhauling Midlife Bike - Tecnología • Artesanía • Performance<br>Santiago, Chile</center>", unsafe_allow_html=True)
