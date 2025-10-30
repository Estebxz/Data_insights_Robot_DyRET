import os
import streamlit as st
from components.UI.boton_flotante import Boton_flotante

st.title("INTRODUCCIÓN Y PLANTEAMIENTO DEL PROBLEMA")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("public/DyRET.jpg", caption="Ilustracion grafica del robot DyRET", width="content", output_format="auto")

st.subheader("Contexto")
st.markdown("""
Los **robots cuadrúpedos bioinspirados** representan un campo de rápido desarrollo en la robótica, destacando por su capacidad para adaptarse a terrenos complejos y realizar tareas en ambientes desafiantes.
""")

st.divider()

st.subheader("Sensores Integrados")
st.markdown("""
Para lograr una interacción precisa con su entorno, el robot está equipado con dos tipos de sensores avanzados:

* **Sensores de Fuerza (RAW):** En el extremo de cada una de las cuatro patas se encuentra un sensor de fuerza de tres ejes (*Optoforce OMD-20-SH-80N*). Este dispositivo es crucial para registrar las fuerzas de contacto con el suelo en los ejes X, Y y Z.

* **Unidad de Medición Inercial (IMU):** Se incorpora una IMU (*Xsens MTI-30*) que integra:
    * Un **giroscopio** de tres ejes para medir velocidades de rotación.
    * Un **acelerómetro** de tres ejes para registrar aceleraciones lineales.
    * Un **magnetómetro** de tres ejes que proporciona la orientación absoluta del robot con respecto al campo magnético terrestre.
""")
Boton_flotante()