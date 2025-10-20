import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache_data
def load_data():
    df = pd.read_csv("data/df_qcat_filtrado.csv")

    patas_config = {
        'FL': {'label': 'Izquierda delantera'},
        'FR': {'label': 'Derecha delantera'},
        'BL': {'label': 'Izquierda trasera'},
        'BR': {'label': 'Derecha trasera'}
    }
    return df, patas_config

def grafico_comparacion_fuerzas():
    df, patas_config = load_data()
    st.header("Componentes de Fuerza Promedio (x, y, z) por ***Pata*** y ***Terreno***")

    superficies = df['Superficie'].unique().tolist()
    superficie_sel = st.selectbox("Selecciona la superficie:", superficies)

    df_sup = df[df['Superficie'] == superficie_sel].copy()

    df_sup['intervalo_t'] = pd.cut(
        df_sup['Tiempo_s'],
        bins=range(int(df_sup['Tiempo_s'].min()), int(df_sup['Tiempo_s'].max()) + 2, 1),
        right=False
    )

    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=[p['label'] for p in patas_config.values()],
        horizontal_spacing=0.08,
        vertical_spacing=0.15
    )

    for i, (pata, pconf) in enumerate(patas_config.items()):
        df_mean = df_sup.groupby('intervalo_t', observed=False).agg({
            f'{pata}_x': 'mean',
            f'{pata}_y': 'mean',
            f'{pata}_z': 'mean'
        }).reset_index()

        df_mean['t_medio'] = df_mean['intervalo_t'].apply(lambda x: x.left + 0.5)

        row = i // 2 + 1
        col = i % 2 + 1

        fig.add_trace(
            go.Scatter(
                x=df_mean['t_medio'], y=df_mean[f'{pata}_x'], mode='lines',
                name='Fx' if i == 0 else None,
                line=dict(color='blue', width=2),
                showlegend=(i == 0)
            ),
            row=row, col=col
        )

        fig.add_trace(
            go.Scatter(
                x=df_mean['t_medio'], y=df_mean[f'{pata}_y'], mode='lines',
                name='Fy' if i == 0 else None,
                line=dict(color='green', width=2),
                showlegend=(i == 0)
            ),
            row=row, col=col
        )

        fig.add_trace(
            go.Scatter(
                x=df_mean['t_medio'], y=df_mean[f'{pata}_z'], mode='lines',
                name='Fz' if i == 0 else None,
                line=dict(color='red', width=2),
                showlegend=(i == 0)
            ),
            row=row, col=col
        )

        fig.update_xaxes(title_text="Tiempo (s)", row=row, col=col)
        #fig.update_yaxes(title_text="Fuerza promedio (N)", row=row, col=col)

    fig.update_layout(
        height=800,
        width=1400,
        title=dict(
            text=f"Componentes de Fuerza Promedio (Fx, Fy, Fz) por Pata - Terreno: {superficie_sel}"
        ),
        hovermode="x unified",
        template="plotly_white",
        legend=dict(orientation='h', yanchor="bottom", y=1.03, xanchor="right", x=1),
    )

    st.plotly_chart(fig)