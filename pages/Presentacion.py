import streamlit as st
from components.UI.star_github import footer_component

st.image("public/icons/logomark.svg", width="content")
st.image("public/outside.png", width="content", output_format="JPEG")
st.info("Repositorio original del proyecto en [CSIRO](https://data.csiro.au/collection/csiro:46885)")

st.divider()

st.subheader("Tabla de Contenido")
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True, height=257):
        st.markdown("##### Módulos Principales")
        st.page_link("pages/Contexto.py", label="1️⃣ Módulo 1: Contexto")
        st.page_link("pages/Introduccion.py", label="2️⃣ Módulo 2: Introducción")
        st.page_link("pages/Objetivos.py", label="3️⃣ Módulo 3: Objetivos")
        st.page_link("pages/Metodologia.py", label="4️⃣ Módulo 4: Metodología")
        st.page_link("pages/Discusion_y_Analisis.py", label="5️⃣ Módulo 5: Discusión y Análisis")
        st.page_link("pages/Conclusiones_y_Recomendaciones.py", label="6️⃣ Módulo 6: Conclusiones y Recomendaciones")
        st.page_link("pages/Referencias_Bibliograficas.py", label="7️⃣ Referencias Bibliográficas")

with col2:
    with st.container(border=True):
        st.markdown("#### Secciones Complementarias")
        st.page_link("pages/Resumen_Estadistico.py", label="📑 Informe Estadístico")
        st.page_link("pages/Graficos.py", label="📈 Gráficos")
        st.page_link("pages/Glosario.py", label="📖 Glosario")
        st.page_link("pages/Contacto.py", label="📞 Contacto")

footer_component()