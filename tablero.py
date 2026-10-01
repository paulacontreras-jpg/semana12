```python
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(
    page_title="Mi espacio creativo",
    page_icon="🎨",
    layout="wide"
)

# Título principal
st.title("🎨 Mi espacio creativo")
st.write("Un pequeño tablero para dibujar, experimentar y dejar volar la creatividad.")

# Panel lateral
with st.sidebar:
    st.header("⚙️ Herramientas")

    # Dimensiones
    st.subheader("📐 Tamaño del tablero")

    canvas_width = 600
    canvas_height = 400

    st.write(f"Ancho: **{canvas_width}px**")
    st.write(f"Alto: **{canvas_height}px**")

    st.divider()

    # Herramienta
    st.subheader("🖌️ Herramienta")

    drawing_mode = st.selectbox(
        "Selecciona una herramienta:",
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

    # Grosor
    stroke_width = st.slider(
        "Grosor del trazo",
        min_value=1,
        max_value=30,
        value=5
    )

    # Colores
    st.subheader("🎨 Colores")

    stroke_color = st.color_picker(
        "Color del trazo",
        "#FFFFFF"
    )

    bg_color = st.color_picker(
        "Color del fondo",
        "#000000"
    )

# Área principal del dibujo
st.subheader("Tu tablero")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}"
)

# Información debajo del tablero
if canvas_result.image_data is not None:
    st.caption("✨ Tu dibujo aparecerá aquí mientras trabajas.")
```
