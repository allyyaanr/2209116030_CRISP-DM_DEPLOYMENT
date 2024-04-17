import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle

def load_data():
    data = pd.read_csv("laptops.csv")
    return data

def load_data1():
    data1 = pd.read_csv("Data Cleaning (1).csv")
    return data1

def load_data2():
    data2 = pd.read_csv("data-before-mapping.csv")

def load_data3():
    data3 = pd.read_csv("Data Cleaning.csv")

def scatter_plot(data2):
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 6)
    sns.scatterplot(x='display(in inch)', y='price(in Rs.)', data=data2)
    ax.set_xlabel('Display(in inch)')
    ax.set_ylabel('Price (in Rs.)')
    ax.set_title("Korelasi antara Display(in inch) dan price(in Rs.)")
    ax.grid(True)
    st.pyplot(fig)
    text = 'Visualisasi tersebut adalah scatter plot yang menunjukkan hubungan antara ukuran layar laptop (dalam inch) dengan harga laptop (dalam rupee India). Pola umum menunjukkan bahwa semakin besar ukuran layar, semakin tinggi harga laptopnya, menunjukkan adanya korelasi positif antara kedua variabel tersebut.'
    st.write(text)

def plot_correlation(data1):
    numeric_df = data1.select_dtypes(include='number')
    corr_matrix = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)
    text = 'Visualisasi tersebut adalah heatmap yang menampilkan korelasi antara fitur-fitur numerik dalam dataset. Nilai-nilai dalam heatmap menunjukkan seberapa kuat korelasi antara dua fitur. Korelasi positif ditunjukkan dengan warna merah, korelasi negatif dengan warna biru, dan korelasi yang lemah atau tidak ada dengan warna netral. Ini membantu dalam mengidentifikasi hubungan antara fitur-fitur yang berbeda dalam data.'
    st.write(text)

def compositionAndComparison(data3):
    # Hitung rata-rata fitur untuk setiap kelas
    data3['PriceCategory'].replace({0: 'Cheap', 1: 'Affordable', 2: 'Expensive'}, inplace=True)
    class_composition = data3.groupby('PriceCategory').mean()
    
    # Plot komposisi kelas
    plt.figure(figsize=(10, 6))
    sns.heatmap(class_composition.T, annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title('Composition for each class')
    plt.xlabel('Class')
    plt.ylabel('Feature')
    st.pyplot(plt)
    text = 'Visualisasi heatmap diatas menunjukkan rata-rata nilai fitur untuk setiap kelas harga. Setiap baris pada heatmap mewakili fitur tertentu, seperti harga (price), processor, RAM, OS, storage, display, rating, jumlah penilaian (no_of_ratings), dan jumlah ulasan (no_of_reviews). Setiap kolom mewakili kelas harga, yaitu "Affordable", "Cheap", dan "Expensive". Warna pada heatmap menunjukkan nilai rata-rata untuk setiap fitur dan kelas harga. Semakin gelap warnanya, semakin tinggi nilainya. Sebaliknya, semakin terang warnanya, semakin rendah nilainya.'
    st.write(text)

def predict(df):
    price = st.slider('Price (in Rs.):',0,500000)
    selected_options = st.selectbox('Processor:', [i for i in df['processor'].unique()])
    selected_options1 = st.selectbox('Ram:', [i for i in df['ram'].unique()])
    selected_options2 = st.selectbox('OS:', [i for i in df['os'].unique()])
    selected_options3 = st.selectbox('Storage:', [i for i in df['storage'].unique()])
    selected_options4 = st.slider('Display:', 10,35)
    selected_options5 = st.slider('Rating:', 0,5)
    selected_options6 = st.slider('Number Of Rating:', 0,9000)
    selected_options7 = st.slider('Number Of Reviews:', 0 , 800)

    value = [price,selected_options,selected_options1,selected_options2,selected_options3,selected_options4,selected_options5,selected_options6,selected_options7]
    
    index_options = {
        'Processor': np.where(df['processor'].unique() == selected_options)[0][0],
        'Ram': np.where(df['ram'].unique() == selected_options1)[0][0],
        'OS': np.where(df['os'].unique() == selected_options2)[0][0],
        'Storage': np.where(df['storage'].unique() == selected_options3)[0][0],
    }

    # Membuat DataFrame dari data yang dipilih
    data_selected = pd.DataFrame({
        'price (in Rs.)': [price],
        'processor': [index_options['Processor']],
        'ram': [index_options['Ram']],
        'os': [index_options['OS']],
        'storage': [index_options['Storage']],
        'display (in inch)': [selected_options4],
        'rating': [selected_options5],
        'number_of_ratings': [selected_options6],
        'number_of_reviews': [selected_options7]
    })

    button = st.button('predict')

    if button :


        with open('gnb.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        predicted = loaded_model.predict(data_selected)

        st.success(predicted)

    text = 'Keterangan : Jika tertampil 1 ialah Laptop termasuk kedalam kategori Cheap (Murah), Jika tertampil 2 ialah Laptop termasuk kedalam kategori Affordable (Terjangkau), dan jika tertampil 3 ialah laptop termasuk kategori Expensive (Mahal).'
    st.write(text)


