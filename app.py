import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import time

# Cargar los datos
vehicules_dataframe = pd.read_csv('vehicles_us.csv')

st.title(":blue[Sprint 7.]Herramientas de Desarrollo Software :sunglasses:", anchor=None)
st.divider()

resume_project = """
Este proyecto me permitirá reforzar mis habilidades en ingeniería de software a través de la creación y gestión de
 entornos virtuales en Python, el desarrollo de una aplicación web y su posterior despliegue en la nube. Aunque 
 se proporciona un conjunto de datos de anuncios de venta de coches, el enfoque principal no está en el análisis 
 de datos, sino en la aplicación de herramientas esenciales para el desarrollo y la implementación de software.
"""


def stream_resume():
    for word in resume_project.split(" "):
        yield word + " "
        time.sleep(0.06)
if st.button("Resumen del Proyecto",type="secondary",icon="🔥"):
    st.write_stream(stream_resume)


st.markdown(":blue-background[DATAFRAME DE LA EVALUACIÓN]")

st.dataframe(vehicules_dataframe)

st.subheader("1. Historigrama", divider="blue")
option = st.selectbox(
    "¿Qué historigrama te gustaría visualizar?",
    ("Año de modelo del vehículo", "Distancia recorrida por el vehiculo (odómetro)", "Precio de compra del vehículo"),
)
st.write("You selected:", option)

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('HISTORIGRAMA',option.upper())
    if option=="Año de modelo del vehículo":
        fig_hist = px.histogram(vehicules_dataframe, x="model_year")
        st.plotly_chart(fig_hist, use_container_width=True)
    elif option=="Distancia recorrida por el vehiculo (odómetro)":
        fig_hist = px.histogram(vehicules_dataframe, x="odometer")
        st.plotly_chart(fig_hist, use_container_width=True)
    elif option=="Precio de compra del vehículo":
        fig_hist = px.histogram(vehicules_dataframe, x="price")
        st.plotly_chart(fig_hist, use_container_width=True)


st.subheader("2. Gráfico de Barras referente a los Tipos de coche", divider="blue")
car_types=['SUV','pickup','sedan','truck','coupe','van','convertible','hatchback','wagon','mini-van','other','offroad','bus']
options = st.multiselect(
    "¿Qué tipos de coche deseas incluir en el gráfico?",
    ["todos"]+car_types,
)
hist_button = st.button('Construir Gráfico de Barras')
if hist_button:
    if "todos" in options:
        fig_bar=px.bar(vehicules_dataframe,x="type")
        st.plotly_chart(fig_bar,use_container_width=True)
    else:
        filter_df=vehicules_dataframe[vehicules_dataframe["type"].isin(options)]
        fig_bar=px.bar(filter_df,x="type")
        st.plotly_chart(fig_bar,use_container_width=True,xlabel="Tipo de Coches",ylabel="Cantidad")



st.subheader("3. Gráfico de Dispersión", divider="blue")
st.write('Gráfico de dispersión entre Odometer y Precio (Siempre Visible)')
fig_scatter = px.scatter(vehicules_dataframe, x="odometer", y="price")
st.plotly_chart(fig_scatter, use_container_width=True)



