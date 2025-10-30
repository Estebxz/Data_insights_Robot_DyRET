import streamlit as st

def Boton_flotante():
    st.divider()
    with st.container(border=True, horizontal_alignment="right"):
        st.page_link(
            "pages/Glosario.py",
            label="**Glosario**",
            icon="📖",
            help="Redirigir al glosario",
            width="content"
        )