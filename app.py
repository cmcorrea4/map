import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

with open('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Accidentalidad Municipio de Medellín 2016")
# Carga el archivo GeoJSON como un GeoDataFrame
#gdf = gpd.read_file('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson')


La = []
Lo= []
day=[]
hour=[]
neig=[]
dir=[]    
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    dia=feature['properties']['dia']
    Hora=feature['properties']['hora']
    barrio=feature['properties']['barrio']
    direccion=feature['properties']['direccion']
    La.append(coordinates[1])
    Lo.append(coordinates[0])  
    day.append(dia)
    hour.append(Hora)
    neig.append(barrio)
    dir.append(direccion)
    
    
#nm=100
nm= st.slider('Selecciona el número de registros de accidentes quieres visualizar', 1, 200, 5)


dfLa = pd.DataFrame({'lat':La[0 : nm]})
dfLo = pd.DataFrame({'lon':Lo[0 : nm]})
dfdia= pd.DataFrame({'día' :day[0:nm]})
dfhor= pd.DataFrame({'Hora' :hour[0:nm]})
dfbarr=pd.DataFrame({'Barrio':neig[0:nm]})
dfdir=pd.DataFrame({'Dirección':dir[0:nm]})
df_g=pd.concat([dfLa, dfLo, dfdia, dfhor,dfdir,dfbarr], axis=1)

st.write(df_g)
st.subheader('Organizado por tiempo')
df_g = df_g.sort_values('Hora')
st.write(df_g)
st.map(df_g)

st.subheader('Filtrado')

df_filtrado = df_g.query('día == "MIÉRCOLES" and Hora >= "08:00:00" and Hora <= "10:00:00"')
st.write(df_filtrado)

# Convierte el GeoDataFrame en un DataFrame de pandas
#df2 = pd.DataFrame(gdf)

#st.write(df2.columns[1])
#st.write(df2.columns[2])
#st.write(df2.columns[3])
#st.write(df2['hora'].iloc[3])
#st.write(df2['geometry'].iloc[2])
#df2['geometry'].iloc[4]
#df2['geometry'].shape
#type(df2['geometry'])
#st.write(df2['geometry'])
#st.dataframe(df2.columns.values)

#geometry = df2['geometry']

# Convierte la serie de geometría en un DataFrame de pandas
#df4 = pd.DataFrame(geometry)
#st.dataframe(df4)


df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [6.250136, -75.566067],  #6.250136 -75.566067
    columns=['lat', 'lon'])

st.map(df)
st.write(df)
