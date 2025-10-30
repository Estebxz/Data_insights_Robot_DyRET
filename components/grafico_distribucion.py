import streamlit as st
import pandas as pd
import plotly.express as px

from components.UI.msg_temporal import msg_temp

@st.cache_data
def load_data():
    df = pd.read_csv("data/df_qcat_filtrado.csv")

    patas_config = {
        'FL_net': {'label': 'Pata delantera izquierda', 'color': '#FAEE82'},
        'FR_net': {'label': 'Pata delantera derecha', 'color': '#F7CCA6'},
        'BL_net': {'label': 'Pata trasera izquierda', 'color': '#DDCDFF'},
        'BR_net': {'label': 'Pata trasera derecha', 'color': '#94D8E0'}
    }

    return(df, patas_config)
    
def grafico_distribucion():
    df, patas_config = load_data()
    st.header("Distribución de Fuerzas Netas")
    
    patas_seleccionadas = st.multiselect(
        label="Elige una o más patas para visualizar y comparar su distribución:",
        options=list(patas_config.keys()),
        format_func=lambda key: patas_config[key]['label'],
        default=['FR_net'],
    )

    if not patas_seleccionadas:
        msg_temp(texto="Seleccione al menos una pata", tipo="warning", duracion=5)
    
    else:
        df_melted = df.melt(
            value_vars=patas_seleccionadas,
            var_name="Pata",
            value_name="Fuerza (N)"
        )
        
        df_melted['Nombre_Pata'] = df_melted['Pata'].apply(lambda x: patas_config[x]['label'])
        
        color_map = {patas_config[key]['label']: patas_config[key]['color'] for key in patas_seleccionadas}

        fig = px.histogram(
            df_melted, 
            x="Fuerza (N)", 
            color="Nombre_Pata",
            nbins=50,
            histnorm='probability density',
            title=f"Distribución de la Fuerza Neta por {patas_config[patas_seleccionadas[0]]['label']}",
            color_discrete_map=color_map
        )
        
        fig.update_layout(
            xaxis_title='Fuerza neta (N)',
            yaxis_title='Frecuencia',
            legend=dict(orientation='h', yanchor="bottom", y=1.02, xanchor="right", x=1),
            height=600,
            bargap=0.1
        )
        
        fig.update_traces(opacity=0.7)
        
        st.plotly_chart(fig)