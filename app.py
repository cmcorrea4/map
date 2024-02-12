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

st.write('Se entiende por accidente de tránsito  evento, generalmente involuntario, generado al menos por un un vehículo en movimiento, que causa daños a '
         'personas y bienes involucrados en él, e igualmente afecta la normal circulación de los vehículos que se movilizan por la vía o vías comprendidas en el' 
         'lugar o dentro de la zona de influencia del hecho0 (Ley 769 de 2002 - Código Nacional de Tránsito)'
         )
st.subheader('Sistema de consulta de Accidentalidad municipio de Medellín')

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
nm= st.slider('Selecciona el número de registros de accidentes quieres visualizar', 5, 1500)


dfLa = pd.DataFrame({'lat':La[0 : nm]})
dfLo = pd.DataFrame({'lon':Lo[0 : nm]})
dfdia= pd.DataFrame({'día' :day[0:nm]})
dfhor= pd.DataFrame({'Hora' :hour[0:nm]})
dfbarr=pd.DataFrame({'Barrio':neig[0:nm]})
dfdir=pd.DataFrame({'Dirección':dir[0:nm]})
df_g=pd.concat([dfLa, dfLo, dfdia, dfhor,dfdir,dfbarr], axis=1)

st.dataframe(df_g)
st.map(df_g)

st.subheader('Filtrado')
option_hour_min = st.selectbox('Selecciona filtro por Hora',
                               ('08:00:00', '09:00:00', '10:00:00','11:00:00','12:00:00','13:00:00','14:00:00'),key='1')
#option_hour_max = st.selectbox('Selecciona filtro por Hora',
#                               ('08:00:00', '09:00:00', '10:00:00','11:00:00','12:00:00','13:00:00','14:00:00'),key='2')
option_day = st.selectbox('Selecciona filtro por día',('LUNES', 'MARTES', 'MIÉRCOLES','JUEVES','VIERNES','SÁBADO','DOMINGO'))
#df_filtrado = df_g.query('día == "MIÉRCOLES" and Hora >= "08:00:00" and Hora <= "10:00:00"')
df_filtrado = df_g.query('día == @option_day and Hora >=  @option_hour_min ')
st.dataframe(df_filtrado)

try:
   st.metric("Cantidad de Incidentes dentro del filtro", df_filtrado.shape[0])
except:
    pass
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

st.map(df_filtrado)
#st.write(df)
