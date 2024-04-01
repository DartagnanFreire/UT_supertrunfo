import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
from streamlit_folium import st_folium

st.set_page_config(
    page_title='Testes',
    layout='wide'
)

# center on Liberty Bell, add marker
m = folium.Map(location=[-23.669103342163112, -46.55801895190962], zoom_start=16)
folium.Marker(
    [-23.669103342163112, -46.55801895190962], popup="Liberty Bell", tooltip="Liberty Bell"
)
Draw(export=True).add_to(m)


output = st_folium(m, width=1920, height=800)