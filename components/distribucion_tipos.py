import streamlit as st
import polars as pl
import plotly.express as px

ruta_csv = "data/df_qcat_filtrado.csv"

def distribucion_tipos(ruta_csv: str):
    df_lazy = pl.scan_csv(ruta_csv)

    schema = df_lazy.collect_schema()
    tipos = [str(t) for t in schema.values()]
    columnas = list(schema.keys())

    st.subheader("Tipos de datos:")
        
    info = pl.DataFrame({"Columna": columnas, "Tipo de Dato": tipos})
    info_pd = info.to_pandas()
    conteo_tipos = info_pd["Tipo de Dato"].value_counts().reset_index()
    conteo_tipos.columns = ["Tipo de Dato", "Cantidad"]

    fig = px.bar(
        conteo_tipos,
        x="Tipo de Dato",
        y="Cantidad",
        color="Tipo de Dato",
        text="Cantidad",
        color_discrete_sequence=px.colors.qualitative.Dark24,
        title="Distribución de tipos de datos",
        )

    fig.update_traces(
        textposition='outside',
    )
    
    fig.update_layout(
        template="plotly_dark",
        xaxis_title=None,
        yaxis_title="Número de columnas",
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
        )

    config = {
        "displayModeBar": True,
        "displaylogo": False,
        "responsive": True
        }
    
    st.plotly_chart(fig, config=config)

    if st.toggle("Ver detalle de columnas"):
            st.dataframe(info, width="stretch", height=400)

    st.subheader("Estadísticas descriptivas (numéricas):")
    df_describe = df_lazy.describe()
    st.dataframe(df_describe)