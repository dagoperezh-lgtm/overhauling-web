import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Overhauling Midlife Bike",
    page_icon="🚲",
    layout="wide"
)

# --- 1. CABECERA ---
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; padding: 10px;'>
        <h2 style='color: #1E1E1E;'>Overhauling Midlife Bike 🚲</h2>
        <p>Servicios | Paint Studio | Upgrades | Proyectos | Agendar</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. SECCIÓN HERO (BANNER PRINCIPAL) ---
# Aquí usaremos la foto de la Fuji negra mate mejorada
st.image("tu_foto_fuji_mejorada.png", 
         caption="Overhauling Midlife Bike: Ingeniería y Estética", 
         use_container_width=True)

st.markdown("<h1 style='text-align: center;'>La Reconstrucción de tu Pasión</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>Mecánica avanzada, pintura custom y upgrades tecnológicos para ciclistas de alto nivel.</p>", unsafe_allow_html=True)

st.divider()

# --- 3. PROPUESTA DE VALOR ---
cv1, cv2, cv3 = st.columns(3)
with cv1:
    st.subheader("🛡️ Precisión")
    st.write("Ingeniería aplicada con herramientas de torque digital y estándares de fábrica.")
with cv2:
    st.subheader("🎨 Estética")
    st.write("Transformamos marcos de carbono en piezas únicas de colección con acabados de autor.")
with cv3:
    st.subheader("🏁 ADN Competitivo")
    st.write("Especialistas en Triatlón, Ruta, MTB y Gravel de alta gama.")

st.divider()

# --- 5. SECCIÓN ANTES Y DESPUÉS (CASO DE ÉXITO) ---
st.header("Caso de Éxito: Full Overhaul & Paint")
col_antes, col_despues = st.columns(2)

with col_antes:
    st.subheader("Antes")
    # Aquí subes la foto original de la bici
    st.image("fuji_original.png", caption="Estado Inicial", use_container_width=True)

with col_despues:
    st.subheader("Después")
    # Aquí subes la foto del comparativo que generamos
    st.image("fuji_mate_final.png", caption="Resultado: Negro Mate & Stickers Amarillos", use_container_width=True)

st.info("Nota: Estas imágenes muestran el estándar de calidad y nivel de detalle que OMB aplica en cada proyecto.")

st.divider()

# --- 7. AGENDAR DIAGNÓSTICO ---
st.header("Agenda tu Diagnóstico Técnico")
with st.form("contacto"):
    name = st.text_input("Nombre Completo")
    tipo_bici = st.selectbox("Tipo de Bicicleta", ["Ruta", "MTB", "Gravel", "Triatlón"])
    servicio = st.multiselect("Servicios", ["Overhaul", "Pintura", "Upgrades"])
    submit = st.form_submit_button("Enviar Solicitud")
    if submit:
        st.success(f"Solicitud recibida para tu {tipo_bici}. Nos contactaremos pronto.")
