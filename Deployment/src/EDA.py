import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    # element title
    st.title("Taxi Price Regresion Data Exploration")

    # element gambar
    st.image('dataset-cover.jpg',
            caption= 'source: google images')

    # Header
    st.header('Latar Belakang')
    # markdown
    st.markdown('''
                Dalam beberapa tahun terakhir, layanan taksi menghadapi berbagai tantangan yang menimbulkan keresahan di kalangan masyarakat. Salah satu masalah utama yang sering dikeluhkan adalah **ketidaktransparanan tarif**. Banyak pengguna merasa harga perjalanan taksi tidak konsisten dan tidak mencerminkan kondisi aktual, seperti jarak, waktu, atau tingkat kemacetan. Hal ini menimbulkan persepsi bahwa sistem penetapan tarif kurang adil dan cenderung merugikan pelanggan.

Secara keseluruhan, keresahan masyarakat terhadap layanan taksi berakar pada **ketidakadilan tarif** dalam operasional. Oleh karena itu, diperlukan inovasi yang mampu menghadirkan sistem tarif dinamis, transparan, dan adil, sehingga kepercayaan masyarakat terhadap layanan taksi dapat kembali meningkat.''')

    st.header('Dataset')
    st.markdown('Taxi Price Rreggresion yang diambil dari web Kaggle.com')
    # load data dengan pandas
    data = pd.read_csv('taxi_trip_pricing.csv')
    # # rename columns
    # data.rename(columns={'ValueEUR': 'Price', 'Overall': 'Rating'}, inplace=True)
    # tampilkan dataframe
    st.dataframe(data)

    # EDA
    st.header('Exploratory Data Analysis')

    st.subheader('Korelasi tiap kolom')

    # rating histogram
    fig = plt.figure(figsize=(16, 5))
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title('Korelasi Antar Fitur')
    # menampilkan matplotlib chart
    st.pyplot(fig)

    # insight
    st.markdown('''Berdasarkan hasil analisis korelasi, variabel Trip_Price memiliki hubungan yang sangat kuat dengan Trip_Distance_km, menunjukkan bahwa jarak perjalanan merupakan faktor utama penentu harga. Selain itu, faktor Per_Km_Rate dan Trip_Duration_Minutes juga memberikan pengaruh yang cukup berarti terhadap pembentukan tarif, meskipun tidak sekuat jarak perjalanan. Sementara itu, variabel seperti Base_Fare dan Passenger_Count hampir 
                tidak menunjukkan korelasi yang jelas dengan harga perjalanan, sehingga kontribusinya terhadap perubahan tarif dapat dianggap minimal.''')

    # weight vs height
    st.subheader('Trip_Distance_km vs Trip_Price Distribution')
    # plotly chart
    fig = px.scatter(data, x='Trip_Distance_km', y='Trip_Price')
    st.plotly_chart(fig)

    st.title("Distribusi Kolom Dataset")

    # pilih kolom numerik
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # dropdown untuk memilih kolom
    option = st.selectbox(
        'Pilih atribut untuk divisualisasikan:',
        options=numerical_cols
    )

    st.write("Anda memilih:", option)

    # visualisasi histogram
    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data[option], kde=True, bins=30, color='skyblue')
    plt.title(f'Distribusi Kolom: {option}', fontsize=14)
    plt.xlabel(option)
    plt.ylabel("Frekuensi")
    st.pyplot(fig)

    # opsi tambahan: tampilkan semua distribusi sekaligus
    if st.checkbox("Tampilkan semua kolom numerik"):
        for col in numerical_cols:
            fig = plt.figure(figsize=(10, 4))
            sns.histplot(data[col], kde=True, bins=30)
            plt.title(f'Distribusi Kolom: {col}', fontsize=12)
            plt.xlabel(col)
            plt.ylabel("Frekuensi")
            st.pyplot(fig)

if __name__ == '__main__':
    run()