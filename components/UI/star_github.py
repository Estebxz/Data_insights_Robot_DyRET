import streamlit as st
import webbrowser
import time

def footer_component():
    st.divider()
    st.subheader("⭐ Apoya este proyecto en GitHub")
    st.markdown("Proyecto desarrollado por **Grupo de Desarrollo - TTCH(Talento Tech)**")

    if st.button("GitHub", icon="🔗"):
        st.toast("Redirigiendo a GitHub...", icon="🔗")
        time.sleep(1)
        webbrowser.open_new_tab("https://github.com/Estebxz/Dashboard_grupo_1")
        st.toast("¡Gracias por tu apoyo!", icon="❤️")