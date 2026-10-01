import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(
    page_title="Mi espacio creativo",
    page_icon="🎨",
    layout="wide"
)

# Título
st.title("🎨 Mi espacio creativo")
st.write("Dibuja, experimenta y crea usando diferentes herramientas, colores y grosores.")

# -----------------------------
# CONFIGURACIÓN DEL TABLERO
# -----------------------------

canvas_width = 600
canvas_height = 400

# -----------------------------
# HERRAMIENTAS
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    drawing_mode = st.selectbox(
        "🖌️ Herramienta",
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
        "📏 Grosor del trazo",
        min_value=1,
        max_value=30,
        value=5,
        step=1
    )

with col3:
    stroke_color = st.color_picker(
        "🎨 Color del trazo",
        "#FFFFFF"
    )

# -----------------------------
# COLOR DEL FONDO
# -----------------------------

bg_color = st.color_picker(
    "🖼️ Color del fondo",
    "#000000"
)

# -----------------------------
# TABLERO
# -----------------------------

st.subheader("✏️ Tablero")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key="canvas"
)

# -----------------------------
# INFORMACIÓN DEL DIBUJO
# -----------------------------

if canvas_result.image_data is not None:
    st.write("✨ ¡Sigue creando!")

