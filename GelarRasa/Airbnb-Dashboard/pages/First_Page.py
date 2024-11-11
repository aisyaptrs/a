import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Judul aplikasi Streamlit
st.title("New York Airbnb Dashboard")
st.markdown("Menampilkan peta interaktif untuk listing Airbnb di New York City.")

# Load dataset
csv_path = r"C:\Users\Aisya\OneDrive\Documents\GelarRasa\Airbnb-Dashboard\AB_NYC_2019.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(csv_path)

# Mengisi nilai NaN di kolom 'reviews_per_month' dengan 0
df['reviews_per_month'].fillna(0, inplace=True)

# Membuat peta interaktif
m = folium.Map(location=[40.73, -73.95], zoom_start=10)

# Menambahkan marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Menambahkan marker ke cluster
for i, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"""
        <b>Neighbourhood Group:</b> {row['neighbourhood_group']}<br>
        <b>Neighbourhood:</b> {row['neighbourhood']}<br>
        <b>Room Type:</b> {row['room_type']}<br>
        <b>Price:</b> ${row['price']} per night<br>
        <b>Minimum Nights:</b> {row['minimum_nights']}<br>
        <b>Availability:</b> {row['availability_365']} days/year
        """,
        tooltip=row['neighbourhood']
    ).add_to(marker_cluster)

# Tampilkan peta di Streamlit
st_data = st_folium(m, width=700, height=500)

# Menampilkan data dalam tabel jika dibutuhkan
if st.checkbox("Tampilkan Dataframe Airbnb"):
    st.dataframe(df)
