import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from components.UI.msg_temporal import msg_temp

@st.cache_data
def load_data():
    df = pd.read_csv("data/df_qcat_filtrado.csv")

    patas = {
        'FL': ('Pata Izquierda delantera', '#FAEE82'),
        'FR': ('Pata Derecha delantera', '#F7CCA6'),
        'BL': ('Pata Izquierda trasera', '#DDCDFF'),
        'BR': ('Pata Derecha trasera', '#94D8E0')
    }

    superficies = {
        'Hormigón': '⚫ Hormigón',
        'césped': '🟢 Césped',
        'grava': '⚪ Grava',
        'mulch': '▪️ Mulch',
        'tierra': '🟤 Tierra',
        'arena': '🟡 Arena'
    }

    data_list = []

    for sup in df['Superficie'].unique():
        df_sup = df[df['Superficie'] == sup].copy()

        min_time, max_time = int(df_sup['Tiempo_s'].min()), int(df_sup['Tiempo_s'].max())
        bins = range(min_time, max_time + 2, 1)

        df_sup['intervalo_t'] = pd.cut(df_sup['Tiempo_s'], bins=bins, right=False)

        for pata_code, (pata_label, color) in patas.items():
            df_mean = (
                df_sup.groupby('intervalo_t', observed=False)
                .agg({f'{pata_code}_net': 'mean'})
                .reset_index()
            )

            df_mean.rename(columns={f'{pata_code}_net': 'fuerza_neta_promedio'}, inplace=True)
            df_mean['t_medio'] = df_mean['intervalo_t'].apply(lambda x: x.left + 0.5)
            
            df_mean['Superficie'] = sup
            df_mean['Pata_Codigo'] = pata_code
            df_mean['Pata_Label'] = pata_label
            df_mean['Color'] = color
            
            data_list.append(df_mean.dropna(subset=['fuerza_neta_promedio']))

    return pd.concat(data_list, ignore_index=True), patas, superficies


def analizador_fuerza_neta():
    df_all, patas, superficies = load_data()
    st.header("Fuerza Neta por ***Pata*** y ***Superficie***")

    col1, col2 = st.columns(2)
    with col1:
        superficie_seleccionada = st.selectbox(
            "Selecciona una Superficie:",
            options=df_all['Superficie'].unique(),
            format_func=lambda x: str(superficies.get(x, x))
        )
    with col2:
        patas_disponibles = df_all['Pata_Codigo'].unique()
        patas_seleccionadas = st.multiselect(
            "Selecciona una o más Patas:",
            options=patas_disponibles,
            format_func=lambda x: patas[x][0],
            default=['FL', 'FR']
        )

    if not patas_seleccionadas:
        msg_temp(texto="Selecciona al menos una pata.", tipo="warning", duracion=5)
        pass
        
    fig = go.Figure()
    
    df_filtrado = df_all[
        (df_all['Superficie'] == superficie_seleccionada) &
        (df_all['Pata_Codigo'].isin(patas_seleccionadas))
    ]

    for pata_code in patas_seleccionadas:
        df_plot = df_filtrado[df_filtrado['Pata_Codigo'] == pata_code]
        pata_label, color = patas[pata_code]

        fig.add_trace(
            go.Scatter(
                x=df_plot['t_medio'],
                y=df_plot['fuerza_neta_promedio'],
                mode='lines+markers',
                name=pata_label,
                line=dict(color=color, width=2.5),
                marker=dict(size=5)
            )
        )

    titulo_superficie = superficies.get(superficie_seleccionada, superficie_seleccionada)
    fig.update_layout(
        title=f"Fuerza Neta Promedio sobre {titulo_superficie}",
        xaxis_title="Tiempo (s)",
        yaxis_title="Fuerza neta promedio (N)",
        width=750,
        height=550,
        legend=dict(orientation='h', yanchor="bottom", y=1.02, xanchor="right", x=1),
        template='plotly_white'
    )

    st.plotly_chart(fig)