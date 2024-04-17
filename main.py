import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from streamlit_option_menu import *
from fungsi import *

df1 = pd.read_csv('Data Cleaning (1).csv')
df2 = pd.read_csv('Data Cleaning.csv')
df3 = pd.read_csv('buat komposisi.csv')
df4 = pd.read_csv('buat predict.csv')

def main():
    menu = st.sidebar.selectbox("", ["Beranda", "Distribusi", "Hubungan", "Perbandingan dan Komposisi", "Predict"])
    if menu == "Beranda":
        st.title("Spesifikasi Laptop")
        st.subheader("Pembagian Laptop Berdasarkan Spesifikasi Teknis dan Harga")
        st.write("Analisis akan dilakukan untuk membagi laptop ke dalam kategori harga yang relevan berdasarkan spesifikasi teknisnya. Hal ini bertujuan untuk membantu produsen dan pengecer memahami hubungan antara fitur teknis laptop dan harganya, sehingga dapat meningkatkan strategi penetapan harga dan menarik customer dengan berbagai preferensi.")
        st.image("image/laptop.jpg", use_column_width=True)
    
        st.subheader("Hubungan antara Spesifikasi Laptop dan Tingkat Kepuasan Customer")
        st.write("Analisis akan dilakukan untuk menemukan hubungan antara spesifikasi laptop dan tingkat kepuasan customer. Informasi ini dapat digunakan oleh produsen untuk meningkatkan desain produk atau oleh pengecer untuk membuat strategi pemasaran yang lebih fokus.")
        st.image("image/laptop1.jpg", use_column_width=True)

        st.write("Dengan demikian, analisis dari dataset ini memiliki potensi untuk memberikan wawasan yang komprehensif dan mendalam mengenai pasar laptop India, memungkinkan perusahaan untuk mengambil keputusan yang lebih terinformasi dan responsif terhadap perubahan dalam preferensi dan kebutuhan konsumen.")

    elif menu == "Distribusi":
        st.title("Data Distribusi")
        data = load_data()
        scatter_plot(data)

    elif menu == "Hubungan":
        st.title("Hubungan")
        df = load_data()
        plot_correlation(df)
    
    elif menu == "Perbandingan dan Komposisi":
        st.title('Composition')
        compositionAndComparison(df3)
    
    elif menu == "Predict":
        predict(df4)    

if __name__ == '__main__':
    main()