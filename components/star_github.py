import streamlit as st
import webbrowser
import time

def footer_component():
    st.divider()
    st.subheader("⭐ Apoya este proyecto en GitHub")
    st.markdown("Proyecto desarrollado por **Grupo 1 - TTCH**")

    if st.button("GitHub", icon="🔗"):
        st.toast("Redirigiendo a GitHub...", icon="🔗")
        time.sleep(1)
        webbrowser.open_new_tab("https://github.com/kevin69Angel/Pagina-web-DyRed.git")
        st.toast("¡Gracias por tu apoyo!", icon="❤️")