import streamlit as st

def footer_component():
    st.divider()
    st.subheader("⭐ Apoya este proyecto en GitHub")
    st.markdown("Proyecto desarrollado por **Grupo de Desarrollo - TTCH(Talento Tech)**")
    st.link_button(
        icon="🔗",
        label="GitHub",
        url="https://github.com/Estebxz/Dashboard_grupo_1", 
        type="secondary", 
        help="Redirigir a GitHub",
        width="content"
    )