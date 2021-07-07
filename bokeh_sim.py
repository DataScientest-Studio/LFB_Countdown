# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:27:07 2021

@authors: Elora, Marie, Nicolas
"""
import streamlit as st
import pandas as pd
from pyproj import Proj, transform

import bokeh.tile_providers
from bokeh.models import ColumnDataSource

from bokeh.plotting import figure

def bokeh_simulation(lat,lon,detstat):
    dfi=pd.DataFrame({'Latitude':[lat],'Longitude':[lon]})
    dfi['Longmerc'],dfi['Latmerc']=transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), dfi['Longitude'].values, dfi['Latitude'].values)
    dfs=pd.DataFrame({'Latitude':[detstat['Latitude']],'Longitude':[detstat['Longitude']]})
    dfs['Longmerc'],dfs['Latmerc']=(transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), dfs['Longitude'].values, dfs['Latitude'].values));
    
    sourcei=ColumnDataSource(dfi)
    sources=ColumnDataSource(dfs)
    tuile=bokeh.tile_providers.get_provider('CARTODBPOSITRON')
    p=figure(title='Incident et station de déploiement',x_axis_label='Longitude',y_axis_label='Latitude',
         width=900,height=600,x_range=(-53000, 31000), y_range=(6660000, 6755000), x_axis_type='mercator', y_axis_type ='mercator')
    p.add_tile(tuile)
    p.square(source=sourcei,x='Longmerc',y='Latmerc',color='red',legend_label='incident')
    p.triangle(source=sources,x='Longmerc',y='Latmerc',color='black',size=10,legend_label='caserne')
    
   
    p.legend.location = "top_left" 
    st.bokeh_chart(p, use_container_width=True)
    
