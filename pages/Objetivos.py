import streamlit as st
from components.boton_flotante import Boton_flotante

st.title("OBJETIVOS")
st.subheader("Objetivo General")
st.markdown("""
Analizar la relación existente entre la fuerza ejercida por las patas del robot y las características de la superficie sobre la que se desplaza, considerando las variaciones de velocidad y tipo de terreno.  """)
st.subheader("Objetivos Específicos")
st.markdown("""
- Comparar las fuerzas realizadas por cada pata y la relación que hay entre ellas durante la marcha.  
- Examinar el comportamiento de los componentes de la fuerza (Fx, Fy, Fz) en distintas muestras del sensor *raw*.  
- Definir una hipótesis respecto a la existencia de datos atípicos.  
""")

Boton_flotante()