# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# leer los datos
car_data = pd.read_csv(
    r'C:\Users\dayan\OneDrive\Escritorio\proyecto_sprint_7\sprint7-repo\vehicles_us.csv')

# Agregar un encabezado a la aplicación
st.header('Análisis de Datos de Vehículos')

# Crear botones para generar los gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Función para mostrar el histograma
if hist_button:
    st.write('Creando un histograma para la columna odómetro')
    fig_hist = px.histogram(car_data, x="odometer")  # Crear el histograma
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Función para mostrar el gráfico de dispersión
if scatter_button:
    st.write('Creando un gráfico de dispersión para las columnas odómetro y precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Gráfico de Dispersión: Odómetro vs Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Opcional: Usar casillas de verificación para seleccionar el gráfico
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Construyendo un histograma para la columna odómetro')
    fig_hist_checkbox = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist_checkbox, use_container_width=True)

if build_scatter:
    st.write('Construyendo un gráfico de dispersión para odómetro vs precio')
    fig_scatter_checkbox = px.scatter(
        car_data, x="odometer", y="price", title="Gráfico de Dispersión: Odómetro vs Precio")
    st.plotly_chart(fig_scatter_checkbox, use_container_width=True)
