import streamlit as st
import polars as pl
from components.UI.msg_temporal import msg_temp
from components.distribucion_tipos import distribucion_tipos

ruta_csv = "data/df_qcat_filtrado.csv"

def generar_informe_dataset(ruta_csv: str):
    df_lazy = pl.scan_csv(ruta_csv)

    st.subheader("Vista previa:")
    df_preview = df_lazy.collect().head(10)
    st.dataframe(df_preview, width="content", height=400)

    st.subheader("Información general:")
    schema = df_lazy.collect_schema()
    columnas = list(schema.keys())
    n_columnas = len(columnas)
    n_filas = df_lazy.select(pl.count()).collect().item()
    duplicados = 0
    a, b = st.columns(2)
    c, d = st.columns(2)
    
    a.metric("Número de filas", n_filas, delta= "-1.181.869 registros menos", border=True)
    b.metric("Número de columnas", n_columnas, delta= "7 columnas nuevas", border=True)
    c.metric("Numero de nulos", 0, delta_color="off", delta= "0", border=True)
    d.metric("Numero de duplicados", duplicados, delta_color="off", delta="0" , border=True)
    
    st.divider()

    distribucion_tipos(ruta_csv)
    msg_temp("✅ Informe generado correctamente", tipo="success", duracion=2)