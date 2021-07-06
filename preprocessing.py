# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

import pandas as pd
import numpy as np
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
    
    
    #for i in range(len(stations)):
    #    if stations.iloc[i]['dist']<distance:
    #        distance = stations.iloc[i]['dist']
    #        station_proche=stations.iloc[i]['NomStation']
    stat=stations.sort_values('dist',ascending=True)

    lgbm4=load("models/lgbm4.joblib")
    

    df0=df.copy()        
    df0.loc['distFromStation']=stat['dist'].head(1).values
    stat_col='DeployedFromSt_'+stat['NomStation'].head(1).values
    stat_col=re.sub('[^A-Za-z0-9_]+', '', *stat_col)
    stat0=stat['NomStation'].head(1).values
    df0.loc[stat_col]=1
    
    df0=df0.transpose()
    
    
    
    res0=[]
    for pumps in range(1,6):
        df0['NumPumpsAttending']=[pumps]
        tab=lgbm4.predict(df0)
        res0.append(*tab)
    
    
    df1=df.copy()
    df1.loc['distFromStation']=stat['dist'].head(2).tail(1).values
    stat_col='DeployedFromSt_'+stat['NomStation'].head(2).tail(1).values
    stat_col=re.sub('[^A-Za-z0-9_]+', '', *stat_col)
    stat1=stat['NomStation'].head(2).tail(1).values
    df1.loc[stat_col]=1
    
    df1=df1.transpose()
    
  
    
    res1=[]
    for pumps in range(1,6):
        df1['NumPumpsAttending']=[pumps]
        tab=lgbm4.predict(df1)
        res1.append(*tab)
    
    df2=df.copy()
    df2.loc['distFromStation']=stat['dist'].head(3).tail(1).values
    stat_col='DeployedFromSt_'+stat['NomStation'].head(3).tail(1).values
    stat_col=re.sub('[^A-Za-z0-9_]+', '', *stat_col)
    stat2=stat['NomStation'].head(3).tail(1).values
    df2.loc[stat_col]=1
    
    df2=df2.transpose()
    
    
    
    res2=[]
    for pumps in range(1,6):
        df2['NumPumpsAttending']=[pumps]
        tab=lgbm4.predict(df2)
        res2.append(*tab)
        
    res=pd.DataFrame({'Nb vehicules':range(1,6),'Stat0':res0,'Stat1':res1,'Stat2':res2}).set_index('Nb vehicules')
    
    stations=[*stat0,*stat1,*stat2]
    station=stations[res.describe().loc['mean'].argmin()]
    res=res[res.columns[res.describe().loc['mean'].argmin()]]
    
    
    
    return station,res
    


#print(generate_test_data('2021-07-04','23:40','Flooding','Dwelling','Newham','E7',51.5,0))