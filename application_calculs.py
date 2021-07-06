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
    """
    Cette fonction permet de génerer toutes les données nécessaires aux modèles pour le calcul de prédiction à partir
    des donnéees saisies par l'utilisateur

    """
    #Importation de la trame des données test
    df = pd.read_csv("data/colonnes.csv",index_col=1)
    df['sim']=0
    df.drop('Unnamed: 0',inplace=True,axis=1)
    df=df[1:]
    
    #InLondon est toujours égal à 1
    df.loc['InLondon']=1
    
    #On considère toujours une première mobilisation
    df.loc['PlusCode_InitialMobilisation']=1
    
    #On saisit l'heure de l'appel
    df.loc['TimeOfCall']=int(time.split(':')[0])+round(int(time.split(':')[1])/60, 2)
    
    #On met 1 dans le type d'incident correspondant
    inc_col='IncidentType_'+inc
    inc_col=re.sub('[^A-Za-z0-9_]+', '', inc_col)
    df.loc[inc_col]=1
    
    #On met 1 dans le borough correspondant
    bor_col='Borough_'+bor.upper()
    bor_col=re.sub('[^A-Za-z0-9_]+', '', bor_col)
    df.loc[bor_col]=1
    
    #On met 1 dans le district correspondant
    dis_col='District_'+dis
    dis_col=re.sub('[^A-Za-z0-9_]+', '', dis_col)
    df.loc[dis_col]=1
    
    #On met 1 dans le mois correspondant
    month=int(date.split('-')[1])
    month_col='Month_'+str(month)
    df.loc[month_col]=1
    
    #On met 1 dans le jour correspondant
    day=pd.to_datetime(date,format='%Y-%m-%d')
    day=day.weekday

    #On calcule la distance entre l'incident et chaque station
    stations=pd.read_csv('data/Stations_clean.csv',index_col=0)
    dist=stations.apply(lambda row :np.sqrt((row['Longitude']-lon)**2+(row['Latitude']-lat)**2),axis=1) 
    dist=pd.Series(dist,name='dist')
    stations=stations.join(dist)
    
    #On trie les stations par distance à l'incident croissante
    stat=stations.sort_values('dist',ascending=True)

    #On charge le modèle
    lgbm4=load("models/lgbm4.joblib")
    
    #On fait les prédictions pour la station la plus proche en considérant le déploiement de 1 à 5 véhicules
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
    
    #On fait les prédictions pour la 2ème station la plus proche en considérant le déploiement de 1 à 5 véhicules
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
    
    #On fait les prédictions pour la 3ème station la plus proche en considérant le déploiement de 1 à 5 véhicules
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
        
    #On agrège les résultats des 3 stations dans un dataframe
    res=pd.DataFrame({'Nb vehicules':range(1,6),'Stat0':res0,'Stat1':res1,'Stat2':res2}).set_index('Nb vehicules')
    
    #On agrège le nom des 3 stations dans une liste
    stations=[*stat0,*stat1,*stat2]
    
    #On récupère le nom de station, les résultats pour la station la plus rapide (moyenne des 5 déploiements) et ses informations
    station=stations[res.describe().loc['mean'].argmin()]
    res=res[res.columns[res.describe().loc['mean'].argmin()]]
    detstat=stat[stat['NomStation']==station]
    
    return station,res,detstat
    
def affichage_resultat(timeofcall,res):
    hour=int(timeofcall.split(':')[0])
    minute=int(timeofcall.split(':')[1])
    second=int(timeofcall.split(':')[2][:2])
        
    timecall=second+60*minute+3600*hour
    if res[5]<res[1]:
        reslow=res[5]
        reshigh=res[1]
    else :
        reslow=res[1]
        reshigh=res[5]
            
    timea1=timecall+reslow
    timea2=timecall+reshigh
    if timea1>=86400:
        timea1=timea1-86400
    if timea2>=86400:
        timea2=timea2-86400
    timea1h=str(int(timea1//3600))
    if int(timea1h)<10:
        timea1h='0'+timea1h
    timea1s=timea1%3600
    timea1m=str(int(timea1s//60))
    if int(timea1m)<10:
        timea1m='0'+timea1m
    timea1s=str(int(timea1s%60))
    if int(timea1s)<10:
        timea1s='0'+timea1s
    stimea1=timea1h+':'+timea1m+':'+timea1s
    timea2h=str(int(timea2//3600))
    if int(timea2h)<10:
        timea2h='0'+timea2h
    timea2s=timea2%3600
    timea2m=str(int(timea2s//60))
    if int(timea2m)<10:
        timea2m='0'+timea2m
    timea2s=str(int(timea2s%60))
    if int(timea2s)<10:
        timea2s='0'+timea2s
    stimea2=timea2h+':'+timea2m+':'+timea2s
    tempsa1min=str(int(reslow//60))
    tempsa1sec=str(int(reslow%60))
    if int(tempsa1sec)<10:
        tempsa1sec='0'+tempsa1sec
    tempsa2min=str(int(reshigh//60))
    tempsa2sec=str(int(reshigh%60))
    if int(tempsa2sec)<10:
        tempsa2sec='0'+tempsa2sec
    stemps1='('+tempsa1min+'min '+tempsa1sec+'s)'
    stemps2='('+tempsa2min+'min '+tempsa2sec+'s)'
        
    return stimea1,stimea2,stemps1,stemps2

