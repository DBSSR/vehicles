import streamlit as st
import plotly.express as px
import pandas as pd

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # poner titulo al grafico
    st.header('Vehicles Histogram Graphic')
            
            # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

    fig1.show()


disper_button = st.button('Construir dispersion') # crear un botón
        
if disper_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # poner titulo al grafico
    st.header('Vehicles Dispersion Graphic')
            
            # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

    fig2.show()