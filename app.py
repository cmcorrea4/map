import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

with open('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Accidentalidad Municipio de Medellín 2016")
# Carga el archivo GeoJSON como un GeoDataFrame
gdf = gpd.read_file('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson')


La = []
Lo= []
    
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    La.append(coordinates[1])
    Lo.append(coordinates[0])  
nm=200

dfLa = pd.DataFrame({'lat':La[0 : nm]})
dfLo = pd.DataFrame({'lon':Lo[0 : nm]})
df_g=pd.concat([dfLa, dfLo], axis=1)

st.write(df_g)

st.map(df_g)

# Convierte el GeoDataFrame en un DataFrame de pandas
df2 = pd.DataFrame(gdf)

st.write(df2.columns[1])
st.write(df2.columns[2])
st.write(df2.columns[3])
st.write(df2['hora'].iloc[3])
st.write(df2['geometry'].iloc[2])
df2['geometry'].iloc[4]
df2['geometry'].shape
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
