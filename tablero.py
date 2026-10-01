import streamlit as st
from streamlit_drawable_canvas import st_canvas

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Mi espacio creativo",
    page_icon="🎨",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS DE LA PÁGINA
# --------------------------------------------------

st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background-color: #FFF9F2;
    }

    /* Contenedor principal */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Título */
    .titulo {
        font-size: 42px;
        font-weight: 800;
        color: #3D405B;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }

    .subtitulo {
        font-size: 17px;
        color: #77727E;
        margin-top: 5px;
        margin-bottom: 25px;
    }

    /* Tarjetas */
    .tarjeta {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #F0E7DD;
        box-shadow: 0px 5px 15px rgba(80, 65, 55, 0.06);
        margin-bottom: 20px;
    }

    .tarjeta-titulo {
        color: #3D405B;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Texto pequeño */
    .ayuda {
        color: #8C858F;
        font-size: 14px;
    }

    /* Línea decorativa */
    .decoracion {
        height: 5px;
        width: 90px;
        background-color: #F2B5D4;
        border-radius: 10px;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    /* Separadores */
    hr {
        border: none;
        height: 1px;
        background-color: #EEE3D8;
    }

    /* Sliders */
    div[data-baseweb="slider"] > div > div > div {
        background-color: #E8AFC7;
    }

    /* Selectbox */
    div[data-baseweb="select"] > div {
        border-radius: 12px;
        border: 1px solid #E7D8CE;
        background-color: #FFFDFC;
    }

    /* Color picker */
    button[data-testid="stColorPickerButton"] {
        border-radius: 10px;
        border: 1px solid #E7D8CE;
    }

    /* Texto inferior */
    .footer {
        text-align: center;
        color: #A39AA4;
        font-size: 13px;
        margin-top: 25px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.markdown(
    '<div class="titulo">🎨 Mi espacio creativo</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Un pequeño rincón para dibujar, experimentar y dejar que las ideas tomen forma.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="decoracion"></div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

canvas_width = 700
canvas_height = 450


# --------------------------------------------------
# PANEL DE HERRAMIENTAS
# --------------------------------------------------

st.markdown(
    '<div class="tarjeta">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tarjeta-titulo">🖌️ Herramientas de dibujo</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    drawing_mode = st.selectbox(
        "Herramienta",
        (
            "freedraw",
            "line",
            "rect",
            "circle",
            "transform",
            "polygon",
            "point"
        ),
        format_func=lambda herramienta: {
            "freedraw": "✏️ Dibujo libre",
            "line": "📏 Línea",
            "rect": "⬜ Rectángulo",
            "circle": "⭕ Círculo",
            "transform": "🔄 Transformar",
            "polygon": "🔷 Polígono",
            "point": "📍 Punto"
        }[herramienta]
    )

with col2:

    stroke_width = st.slider(
        "Grosor del trazo",
        min_value=1,
        max_value=30,
        value=5,
        step=1
    )

with col3:

    stroke_color = st.color_picker(
        "Color del trazo",
        "#3D405B"
    )

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# COLOR DE FONDO
# --------------------------------------------------

col1, col2 = st.columns([1, 2])

with col1:

    st.markdown(
        '<div class="tarjeta">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="tarjeta-titulo">🖼️ Fondo del tablero</div>',
        unsafe_allow_html=True
    )

    bg_color = st.color_picker(
        "Elige un color",
        "#FFFDF8"
    )

    st.markdown(
        '<div class="ayuda">Puedes crear un fondo claro, oscuro o de cualquier color.</div>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# TABLERO
# --------------------------------------------------

st.markdown(
    '<div class="tarjeta">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tarjeta-titulo">✨ Tu lienzo</div>',
    unsafe_allow_html=True
)

canvas_result = st_canvas(
    fill_color="rgba(242, 181, 211, 0.35)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key="canvas"
)

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# PIE DE PÁGINA
# --------------------------------------------------

st.markdown(
    '<div class="footer">Hecho para experimentar, crear y dibujar ✦</div>',
    unsafe_allow_html=True
)
