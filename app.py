import streamlit as st
import pandas as pd
import numpy as np

import geopandas as gpd


# Carga el archivo GeoJSON como un GeoDataFrame
gdf = gpd.read_file('tu_archivo.geojson')

# Convierte el GeoDataFrame en un DataFrame de pandas
df2 = pd.DataFrame(gdf)






df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [6.250136, -75.566067],  #6.250136 -75.566067
    columns=['lat', 'lon'])

st.map(df)
