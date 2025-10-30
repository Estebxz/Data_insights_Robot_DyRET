import streamlit as st
import folium
from streamlit_folium import st_folium

def mapa_interactivo():
    latitude = -27.4698
    longitude = 153.0251
    
    m = folium.Map(location=[latitude, longitude], zoom_start=4, min_zoom=4, max_zoom=16)

    folium.Marker(
        [latitude, longitude],
        popup="Brisbane",
        tooltip="Lugar de recolección de datos"
    ).add_to(m)

    st.subheader("Ubicación de recolección de datos - Brisbane 🇦🇺")
    st_folium(m, width=725, height=500, key="my_map")