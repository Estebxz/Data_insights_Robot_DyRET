import streamlit as st
import time

def msg_temp(texto: str, tipo: str = "success", duracion: int = 1):
    msg = st.empty()

    if tipo == "success":
        msg.success(texto)
    elif tipo == "warning":
        msg.warning(texto)
    else:
        msg.write(texto)

    time.sleep(duracion)
    msg.empty()