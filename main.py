import streamlit as st

st.set_page_config(
    page_title="Data Insights del Robot DyRET",
    page_icon="public/icons/favicon.ico",
    layout="centered",
    initial_sidebar_state="expanded"
)

resumen = [
    st.Page("pages/Presentacion.py", title="Presentacion", icon="📽️"),
    st.Page("pages/Contexto.py", title="Modulo 1: Contexto", icon="1️⃣"),
    st.Page("pages/Introduccion.py", title="Modulo 2: Introducción", icon="2️⃣"),
    st.Page("pages/Objetivos.py", title="Modulo 3: Objetivo general y específico", icon="3️⃣"),
    st.Page("pages/Metodologia.py", title="Modulo 4: Metodología", icon="4️⃣"), 
    st.Page("pages/Glosario.py", title="Glosario", icon="📖")
]

dataset = [
    st.Page("pages/Resumen_Estadistico.py", title="Informe Estadistico", icon="📑"),
    st.Page("pages/Graficos.py", title="Graficos", icon="📈"),
    st.Page("pages/Discusion_y_Analisis.py", title="Modulo 5: Discusion y Analisis", icon="5️⃣"),
    st.Page("pages/Conclusiones_y_Recomendaciones.py", title="Modulo 6: Conclusiones y Recomendaciones", icon="6️⃣"),
    st.Page("pages/Referencias_Bibliograficas.py", title="Modulo 7: Referencias Bibliográficas", icon="7️⃣"),
]

extra = [
    st.Page("pages/Contacto.py", title="Contacto", icon="📞"),
]

pages = {
    "💻 Resumen": resumen,
    "📂 Presentación": dataset,
    "⚙️ Otros": extra
}

pg = st.navigation(pages)
pg.run()