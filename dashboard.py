import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set style seaborn
sns.set(style='dark')

# Baca file linggar_archive.csv
linggar_archive = pd.read_csv("all_data.csv")

# Streamlit App
st.title("Dashboard Jumlah Penyewa Sepeda pada Bike Rental")

# Tabs
tabs = ["Dashboard Jumlah Penyewa Sepeda berdasarkan Cuaca", "Dashboard Jumlah Penyewa Sepeda per Hari selama 2011 dan 2022"]
current_tab = st.sidebar.radio("Pilih Tab", tabs)

if current_tab == tabs[0]:
    # Visualisasi Jumlah Penyewa Sepeda pada Bike Rental
    st.subheader("Visualisasi Jumlah Penyewa Sepeda berdasarkan Cuaca pada Bike Rental")

    # Hitung jumlah penyewa sepeda pada cuaca cerah (weathersit = 1)
    cuaca_cerah = linggar_archive[linggar_archive['weathersit'] == 1]['cnt'].sum()

    # Hitung jumlah penyewa sepeda pada cuaca berkabut (weathersit = 2)
    cuaca_berkabut = linggar_archive[linggar_archive['weathersit'] == 2]['cnt'].sum()

    # Data untuk visualisasi
    categories = ['Cuaca Cerah', 'Cuaca Berkabut']
    values = [cuaca_cerah, cuaca_berkabut]

    # Visualisasikan data dengan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['black', 'pink'])
    ax.set_xlabel('Cuaca')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
    ax.set_title('Proporsi Jumlah Penyewa Sepeda berdasarkan Cuaca')

    # Tampilkan plot menggunakan Streamlit
    st.pyplot(fig)

elif current_tab == tabs[1]:
    # Analisis Jumlah Penyewa Sepeda pada Bike Rental
    st.subheader('Visualisasi Jumlah Penyewa Sepeda per Hari selama 2011 dan 2022 pada Bike Rental')

    # Hitung jumlah pengguna sepeda berdasarkan hari dalam seminggu
    jumlah_pengguna_per_hari = linggar_archive.groupby('weekday')['cnt'].sum()

    # Reset index untuk mempermudah pengolahan data
    jumlah_pengguna_per_hari = jumlah_pengguna_per_hari.reset_index()

    # Membuat urutan hari dalam seminggu
    weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Membuat plot dalam bentuk pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(jumlah_pengguna_per_hari['cnt'], labels=jumlah_pengguna_per_hari['weekday'], autopct='%1.1f%%', startangle=140)

    # Memberikan judul plot
    ax.set_title('Proporsi Jumlah Pengguna Sepeda per Hari selama 2011 dan 2022')

    # Menampilkan plot
    st.pyplot(fig)
