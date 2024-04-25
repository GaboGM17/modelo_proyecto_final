import streamlit as st
import requests

# Título de la aplicación
st.title('Predicción de precios de viviendas')

# Encabezado y descripción
st.write('Esta aplicación predice el precio de una vivienda utilizando un modelo de aprendizaje automático.')

# Sección para ingresar los parámetros de la vivienda
st.header('Ingrese los parámetros de la vivienda:')
crim = st.number_input('CRIM: (Tasa de criminalidad per capita)', value=0.0)
zn = st.number_input('ZN: (Proporción de terrenos residenciales', value=0.0)
indus = st.number_input('INDUS: (Proporcion de terrenos industriales', value=0.0)
chas = st.selectbox('CHAS: (Limita con el río Charles?)', [0, 1])
nox = st.number_input('NOX: (Concentración de oxidos de nitrogeno', value=0.0)
rm = st.number_input('RM: (Promedio de habitaciones por vivienda)', value=0.0)
age = st.number_input('AGE: (Proporcion de viviendas antiguas)', value=0.0)
dis = st.number_input('DIS: (Distancia a centros de empleo en millas)', value=0.0)
rad = st.number_input('RAD: (Indice de accesibilidad a autopistas)', value=0.0)
tax = st.number_input('TAX: (Tasa de impuestos sobre la propiedad)', value=0.0)
ptratio = st.number_input('PTRATIO: (Indice de alumnos por maestro)', value=0.0)
b = st.number_input('UNEMPLO: (Indice de desempleo en la zona)', value=0.0)
lstat = st.number_input('LSTAT: (Indice de pobreza en la zona)', value=0.0)

# Botón para ejecutar la predicción
if st.button('Predecir precio'):
    # Formatear los datos como un JSON
    data = {
        "CRIM": crim,
        "ZN": zn,
        "INDUS": indus,
        "CHAS": chas,
        "NOX": nox,
        "RM": rm,
        "AGE": age,
        "DIS": dis,
        "RAD": rad,
        "TAX": tax,
        "PTRATIO": ptratio,
        "B": b,
        "LSTAT": lstat
    }

    # Hacer la solicitud al API
    url = 'http://127.0.0.1:8000/predict'  # Cambiar la URL si es necesario
    response = requests.post(url, json=data)

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        prediction = response.json()['predicted_price']
        st.success(f'El precio estimado de la vivienda es: {prediction}')
    else:
        st.error('Ha ocurrido un error al procesar la solicitud. Por favor, inténtalo de nuevo más tarde.')
