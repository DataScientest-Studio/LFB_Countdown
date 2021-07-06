# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

import pandas as pd
import numpy as np
import datetime
import re
from joblib import load



def generate_test_data(date,time,inc,prop,bor,dis,lat,lon):

    df = pd.read_csv("data/colonnes.csv",index_col=1)
    df['sim']=0
    df.drop('Unnamed: 0',inplace=True,axis=1)
    df=df[1:]
    
    df.loc['InLondon']=1
    df.loc['PlusCode_InitialMobilisation']=1
    
    df.loc['TimeOfCall']=int(time.split(':')[0])+round(int(time.split(':')[1])/60, 2)
    
    inc_col='IncidentType_'+inc
    inc_col=re.sub('[^A-Za-z0-9_]+', '', inc_col)
    
    df.loc[inc_col]=1
    
    bor_col='Borough_'+bor.upper()
    bor_col=re.sub('[^A-Za-z0-9_]+', '', bor_col)
    
    df.loc[bor_col]=1
    
    dis_col='District_'+dis
    dis_col=re.sub('[^A-Za-z0-9_]+', '', dis_col)
    
    df.loc[dis_col]=1
    
    month=int(date.split('-')[1])
    month_col='Month_'+str(month)
    df.loc[month_col]=1
    
    
    day=pd.to_datetime(date,format='%Y-%m-%d')
    #day=day.dt.weekday
    day=day.day_of_week
    
    stations=pd.read_csv('data/Stations_clean.csv',index_col=0)
    dist=stations.apply(lambda row :np.sqrt((row['Longitude']-lon)**2+(row['Latitude']-lat)**2),axis=1) 
    dist=pd.Series(dist,name='dist')
    stations=stations.join(dist)
    
    distance=2.0
    station_proche=''
    for i in range(len(stations)):
        if stations.iloc[i]['dist']<distance:
            distance = stations.iloc[i]['dist']
            station_proche=stations.iloc[i]['NomStation']
            
    df.loc['distFromStation']=distance
    stat_col='DeployedFromSt_'+station_proche
    stat_col=re.sub('[^A-Za-z0-9_]+', '', stat_col)
    df.loc[stat_col]=1
    
    df=df.transpose()
    
    
    lgbm4=load("models/lgbm4.joblib")
    res=[]
    for pumps in range(1,11):
        df['NumPumpsAttending']=[pumps]
        tab=lgbm4.predict(df)
        res.append(*tab)
    
    
    
    
    
    return station_proche,res
    


