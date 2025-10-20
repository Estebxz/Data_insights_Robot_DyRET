import streamlit as st
from components.boton_flotante import Boton_flotante

st.title("METODOLOGIA")
st.subheader("Diseño de la investigación")
st.markdown("""
El presente proyecto se desarrolló bajo un **diseño de investigación aplicada y descriptiva**, con **enfoque cuantitativo**, orientado al análisis, interpretación y visualización de datos provenientes de un conjunto de información (*dataset*) seleccionado de acuerdo con la temática del curso.  

El propósito principal fue **extraer conocimientos relevantes a partir de datos reales** mediante técnicas de análisis y minería de datos. El proceso metodológico se estructuró en las siguientes etapas:  
""")

st.divider()

etapas = [
    ("Búsqueda y selección del dataset", 
     "Se identificó y seleccionó una fuente de datos pertinente al tema de estudio, asegurando su calidad y disponibilidad para el análisis."),
    ("Análisis inicial del tema y exploración de los datos", 
     "Se realizó una comprensión general y una exploración preliminar de las variables contenidas en el dataset, con el fin de reconocer patrones, valores faltantes y posibles relaciones."),
    ("Organización y limpieza de los datos", 
     "Se aplicaron procesos de depuración, transformación y normalización de la información, eliminando registros duplicados, corrigiendo inconsistencias y estandarizando formatos de fechas, textos y valores numéricos."),
    ("Minería y análisis de datos", 
     "Se implementaron técnicas estadísticas y de análisis para identificar tendencias, correlaciones y comportamientos significativos dentro del conjunto de datos."),
    ("Visualización y graficación", 
     "A través de herramientas de análisis de datos se generaron gráficos e indicadores visuales que facilitaron la interpretación de los resultados obtenidos."),
    ("Conclusiones y recomendaciones", 
     "Con base en el análisis realizado, se establecieron conclusiones que resumen los hallazgos más relevantes y se formularon recomendaciones.")
]

for titulo, descripcion in etapas:
    col1, col2 = st.columns([1.3, 2.7])
    with col1:
        st.markdown(f"<h4 style='margin-top:5px; color:#58A6FF';>{titulo}</h4>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style='text-align: justify; margin-top:10px;'>{descripcion}</p>", unsafe_allow_html=True)
    st.divider()

st.markdown("""
En conjunto, este diseño permitió desarrollar un proceso integral de análisis de datos, desde la adquisición hasta la interpretación final, aplicando las buenas prácticas de la analítica y fortaleciendo las competencias en el uso de herramientas tecnológicas y metodológicas del análisis de información.  

### Fuentes de datos  
Los datos utilizados en este proyecto provienen del conjunto de datos público *“DyRET Hexapod Locomotion Data”*, disponible en el portal de acceso abierto del **Commonwealth Scientific and Industrial Research Organisation (CSIRO)** de Australia.  

Este dataset recopila información experimental obtenida a partir de las pruebas realizadas al robot DyRET (*Dynamic Robot for Embodied Testing*).  

### Técnicas de análisis utilizadas  
Se utilizaron técnicas estadísticas descriptivas, análisis de correlación, comparación de variables y visualización de datos para identificar patrones, tendencias y relaciones significativas en el conjunto de datos.
""")

st.subheader("Herramientas tecnológicas")
st.markdown("""
- Python  
- Seaborn  
- Pandas  
- Matplotlib.pyplot  
- Streamlit  
- Folium  
- Streamlit.components.v1  
""")
Boton_flotante()
