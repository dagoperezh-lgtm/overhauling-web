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
    
    /* Títulos Principales */
    .main-title {
        font-size: 64px !important;
        font-weight: 800 !important;
        color: #1E1E1E;
        text-align: center;
        margin-bottom: 10px;
        line-height: 1.1;
    }
    
    .main-subtitle {
        font-size: 28px !important;
        color: #007BFF;
        text-align: center;
        font-weight: 400;
        margin-bottom: 40px;
    }

    /* Sección de Manifiesto Industrial */
    .manifesto-container {
        background-color: #F8F9FA;
        padding: 60px;
        border-radius: 20px;
        margin: 40px 0;
        border-left: 8px solid #007BFF;
    }
    
    .manifesto-title {
        font-size: 36px;
        font-weight: 700;
        color: #1E1E1E;
        margin-bottom: 25px;
    }

    .manifesto-body {
        font-size: 19px;
        line-height: 1.6;
        color: #333333;
        text-align: justify;
    }

    .highlight-blue {
        color: #007BFF;
        font-weight: 700;
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
nombre_foto_principal = "fuji_mate_final.png"
if os.path.exists(nombre_foto_principal):
    st.image(nombre_foto_principal, use_container_width=True)

# --- 3. MENSAJE DESTACADO ---
st.markdown('<div class="main-title">La Reconstrucción de tu Pasión</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Mecánica avanzada, pintura custom y upgrades tecnológicos para ciclistas de alto nivel en Chile</div>', unsafe_allow_html=True)

st.divider()

# --- 4. SECCIÓN INDUSTRIAL (EL MANIFIESTO) ---
st.markdown(f"""
    <div class="manifesto-container">
        <div class="manifesto-title">Recuperamos el valor de tu bicicleta. Como lo hacen las grandes industrias.</div>
        <div class="manifesto-body">
            Trajimos las mejores prácticas de las grandes compañías intensivas en activos y alta tecnología a una escala más cercana: <b>la del ciclista.</b><br><br>
            Porque para un ciclista de ruta, MTB, gravel o triatlón, su bicicleta no es solo un medio de transporte: <span class="highlight-blue">es su principal activo deportivo.</span> Y como todo activo valioso, pierde valor con el tiempo si no se mantiene, se actualiza y se gestiona correctamente.<br><br>
            En la gran industria, los activos de alto valor no se desechan. Se reacondicionan, se optimizan y se someten a procesos rigurosos de mantenimiento y mejora para devolverles su rendimiento original… o incluso superarlo. Todo esto con un costo significativamente menor que adquirir un activo nuevo y evitando el riesgo de invertir en algo que no cumpla las prestaciones esperadas.<br><br>
            <b>Esa misma lógica aplica para tu bicicleta.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 5. DETALLES TÉCNICOS ---
col_desc1, col_desc2 = st.columns(2)

with col_desc1:
    st.markdown("### Procesos Profesionales")
    st.write("""
    * **Pintura premium** con terminaciones de nivel fábrica.
    * **Ajustes mecánicos finos** y calibración completa.
    * **Mantenciones profundas** y reacondicionamiento integral.
    * **Reemplazo de componentes** de desgaste (cables, rodamientos, transmisión).
    * **Upgrades tecnológicos** (ruedas, frenos, transmisiones electrónicas).
    """)

with col_desc2:
    st.markdown("### El Valor de Renovar")
    st.write("""
    * **Mantienes tu cuadro y geometría**, sin periodos de adaptación.
    * **Recuperas confianza** y rendimiento en competencias.
    * **Revalorizas tu activo** para el mercado de segunda mano.
    * **Alternativa inteligente** frente a los precios de bicicletas nuevas.
    """)

st.markdown("""
    <div style="text-align: center; padding: 30px; font-style: italic; font-size: 20px;">
        "Una decisión racional. Y también emocional. Porque renovar tu bicicleta es devolverle vida a una máquina que todavía tiene mucho por entregar."
    </div>
    """, unsafe_allow_html=True)

# --- 6. ANTES Y DESPUÉS ---
st.markdown('<div class="section-header">Caso de Éxito: Transformación Fuji</div>', unsafe_allow_html=True)
col_a, col_b = st.columns(2)
with col_a:
    if os.path.exists("fuji_antes.png"):
        st.image("fuji_antes.png", caption="Antes", use_container_width=True)
with col_b:
    if os.path.exists("fuji_mate_final.png"):
        st.image("fuji_mate_final.png", caption="Después (Negro Mate & Yellow Stickers)", use_container_width=True)

# --- 7. AGENDAR ---
st.markdown('<div class="section-header">Agenda tu Diagnóstico Técnico</div>', unsafe_allow_html=True)
with st.form("contacto_form"):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Nombre")
        correo = st.text_input("Email")
    with col_f2:
        tipo_bici = st.selectbox("Disciplina", ["Ruta", "Triatlón", "MTB", "Gravel"])
        interes = st.multiselect("Servicio", ["Overhaul", "Pintura", "Upgrades"])
    
    if st.form_submit_button("SOLICITAR EVALUACIÓN"):
        st.success("Mensaje enviado con éxito.")

st.markdown("<br><hr><center>Overhauling Midlife Bike - Lampa, Chile</center>", unsafe_allow_html=True)
