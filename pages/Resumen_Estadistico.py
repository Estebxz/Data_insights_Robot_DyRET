import streamlit as st
from components.resumen_estadistico import generar_informe_dataset
from components.UI.boton_flotante import Boton_flotante

st.title("INFORME DEL DATASET")
generar_informe_dataset("data/df_qcat_filtrado.csv")
Boton_flotante()