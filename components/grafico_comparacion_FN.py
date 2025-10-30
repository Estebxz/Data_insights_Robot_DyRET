import pandas as pd
import plotly.express as px
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/df_qcat_filtrado.csv")

    patas_config = {
        'FL': {'label': 'Pata Izquierda delantera', "color": "#FAEE82"},
        'FR': {'label': 'Pata Derecha delantera', "color": "#F7CCA6"},
        'BL': {'label': 'Pata Izquierda trasera', "color": "#DDCDFF"},
        'BR': {'label': 'Pata Derecha trasera', "color": "#94D8E0"}
    }
    return df, patas_config

def grafico_fuerzas_netas():
    df, patas_config = load_data()
     
    st.header("Comparación de Fuerzas Netas - Cada Pata")
    col_select1, col_select2 = st.columns(2)
    patas_opciones = list(patas_config.keys())

    with col_select1:
        pata_1 = st.selectbox(
            "Selecciona una pata (comparacion A):",
            options=patas_opciones,
            format_func=lambda x: patas_config[x]["label"],
            key="pata_1"
        )

    with col_select2:
        pata_2 = st.selectbox(
            "Selecciona una pata (comparacion B):",
            options=[p for p in patas_opciones if p != pata_1],
            format_func=lambda x: patas_config[x]["label"],
            key="pata_2"
        )

    col1, col2 = st.columns(2)
    seleccionadas = [pata_1, pata_2]
    columnas = [col1, col2]

    for pata, col in zip(seleccionadas, columnas):
        cfg = patas_config[pata]
        fig = px.scatter(
            df,
            x="Tiempo_s",
                y=f"{pata}_net",
                color_discrete_sequence=[cfg["color"]],
                title=f"{cfg['label']}",
                labels={"Tiempo_s": "Tiempo (s)", f"{pata}_net": "Fuerza (N)"},
                opacity=0.8,
            )
        fig.update_layout(
            height=400,
            margin=dict(l=30, r=30, t=60, b=30),
            title=dict(x=0.5),
            yaxis=dict(
                showgrid=True,
                title="Fuerza (N)"
            ),
        )
        col.plotly_chart(fig)