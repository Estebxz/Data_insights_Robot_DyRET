import streamlit as st
import pandas as pd

def tabla_superficies():
    superficies = ["⚫ Hormigón", "🟢 césped", "⚪ grava", "▪️ mulch", "🟤 tierra", "🟡 arena"]
    df_superficies = pd.DataFrame(superficies, columns=["superficie"])
    df_superficies.index.name = "id_superficie"
    
    st.dataframe(
        df_superficies,
        width="stretch",
        height="auto"
    )