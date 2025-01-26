# Importar las librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title('Análisis de Vehículos - Histograma')

# Encabezado para el histograma
st.header('Construcción de un histograma para el análisis de los odómetros')

car_data = pd.read_csv(
    # leer los datos
    r'C:\Users\dayan\OneDrive\Escritorio\proyecto_sprint_7\sprint7-repo\vehicles_us.csv')

# Crear un botón para construir el histograma
hist_button = st.button('Construir histograma')  # Crea un botón

# Acción al hacer clic en el botón para el histograma
if hist_button:
    # Mensaje que aparece cuando se hace clic
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear el histograma usando Plotly
    fig_hist = px.histogram(car_data, x="odometer",
                            title="Distribución del Odómetro de los Vehículos")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Encabezado para el gráfico de dispersión
st.header('Construcción de un gráfico de dispersión')

# Crear un botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')  # Crea un botón

# Acción al hacer clic en el botón para el gráfico de dispersión
if scatter_button:
    # Mensaje que aparece cuando se hace clic
    st.write(
        'Creación de un gráfico de dispersión entre las columnas "odometer" y "price"')

    # Crear el gráfico de dispersión usando Plotly
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Relación entre Odómetro y Precio de los Vehículos")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
