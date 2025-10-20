import streamlit as st

def Boton_flotante():
    with st.container(border=True, horizontal_alignment="right"):
        st.page_link(
            "pages/Glosario.py",
            label="**Glosario**",
            icon="📖",
            help="Ayudate con el glosario",
            width="content"
        )