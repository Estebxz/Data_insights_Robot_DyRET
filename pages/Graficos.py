import streamlit as st    

from components.grafico_FN import analizador_fuerza_neta
from components.grafico_distribucion import grafico_distribucion
from components.grafico_comparacion_fuerzas import grafico_comparacion_fuerzas
from components.grafico_comparacion_FN import grafico_fuerzas_netas
from components.boton_flotante import Boton_flotante

st.title("GRAFICOS")
analizador_fuerza_neta()

st.divider()
grafico_distribucion()

st.divider()
grafico_comparacion_fuerzas()

st.divider()
grafico_fuerzas_netas()
Boton_flotante()