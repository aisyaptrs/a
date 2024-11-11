import streamlit as st
import pandas as pd
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Judul aplikasi Streamlit
st.title("New York Airbnb Dashboard")
st.markdown("Menampilkan peta interaktif untuk listing Airbnb di New York City.")
