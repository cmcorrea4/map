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


lat = []
for feature in data['features']:
    #name = feature['properties']['name']
    coordinates = feature['geometry']['coordinates'][1]
    st.write(coordinates)
    
#    for lat in coordinates:
    lat.append((lat)

#df4 = pd.DataFrame(lat, columns=['latitud'])

#st.dataframe(df4)


# Convierte el GeoDataFrame en un DataFrame de pandas
df2 = pd.DataFrame(gdf)

st.write(df2.columns[1])
st.write(df2.columns[2])
st.write(df2.columns[3])
st.write(df2['hora'].iloc[3])
st.write(df2['geometry'].iloc[2])
df2['geometry'].iloc[4]
df2['geometry'].shape
type(df2['geometry'])
st.write(df2['geometry'])
st.dataframe(df2.columns.values)

#geometry = df2['geometry']

# Convierte la serie de geometría en un DataFrame de pandas
#df4 = pd.DataFrame(geometry)
#st.dataframe(df4)





df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [6.250136, -75.566067],  #6.250136 -75.566067
    columns=['lat', 'lon'])

st.map(df)
