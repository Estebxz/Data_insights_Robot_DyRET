import streamlit as st
from components.star_github import footer_component

equipo = [
    {
        "nombre": "Kevin Ángel",
        "cargo": "Fundadora y CEO",
        "color": "#5865F2",
        "descripcion": "Ex cofundadora de Opendoor. Trabajó en Spotify y Clearbit.",
        "imagen": "public/default.webp",
    },
    {
        "nombre": "Maria Paula Iglesias",
        "cargo": "Director de Ingeniería",
        "color": "#5865F2",
        "descripcion": "Dirige equipos de ingeniería en Figma, Pitch y Protocol Labs.",
        "imagen": "public/default.webp",
    },
    {
        "nombre": "Maria Cristina Hernández",
        "cargo": "Jefa de Producto",
        "color": "#5865F2",
        "descripcion": "Ex PM de Linear, Lambda School y On Deck.",
        "imagen": "public/default.webp",
    },
    {
        "nombre": "Joan Esteban Mendez",
        "cargo": "Desarrolladora Frontend",
        "color": "#5865F2",
        "descripcion": "Antigua desarrolladora frontend para Linear, Coinbase y Postscript.",
        "imagen": "public/default.webp",
    },
]
st.title("CONTACTOS")

for i in range(0, len(equipo), 2):
    col1, col2 = st.columns(2)
    for col, miembro in zip([col1, col2], equipo[i:i+2]):
        with col:
            st.image(miembro["imagen"], width="stretch")
            st.markdown(
                f"""
                <div style="text-align:center;">
                    <h4 style="text-align: center;">{miembro['nombre']}</h4>
                    <p style="color:{miembro['color']}; font-weight:bold; margin-bottom:-5px;">{miembro['cargo']}</p>
                    <p style="font-size:15px;">{miembro['descripcion']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

footer_component()