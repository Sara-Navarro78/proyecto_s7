import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Proyecto Sprint 7 TripleTen.')
st.header('Aplicación web de anuncios de venta de autos.')

hist_button = st.button('Construir histograma') # Crea un botón que, al hacer clic en él, construya un histograma 
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
         fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Construir gráfico de dispersión') # Crear un botón que construya un gráfico de dispersión plotly-express
if disp_button: # al hacer clic en el botón
         # escribir un mensaje
         st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
         # crear un gráfico de dispersión
         fig = px.scatter(car_data, x="odometer", y="price")  # Asumiendo que quieres comparar odometer vs price
     
         # mostrar un gráfico de dispersión
         st.plotly_chart(fig, use_container_width=True)
