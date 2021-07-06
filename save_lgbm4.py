# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

import pandas as pd
import re
from lightgbm import LGBMRegressor
from joblib import dump

#Importation du dataset
df=pd.read_csv('data/LFB_incident_clean.csv',index_col=1)

#Suppression des variables inutiles
df.drop(['Unnamed: 0'],axis=1,inplace =True)
df.drop(['ResourceMobilisationId'],axis=1,inplace =True)
df.drop(['DateAndTimeMobilised'],axis=1,inplace =True)
df.drop(['DateAndTimeArrived'],axis=1,inplace =True)
df.drop(['TurnoutTimeSeconds'],axis=1,inplace =True)
df.drop(['TravelTimeSeconds'],axis=1,inplace =True)
df.drop(['DeployedFromStation_Code'],axis=1,inplace =True)
df.drop(['PumpOrder'],axis=1,inplace =True)
df.drop(['FirstPumpArriving_AttendanceTime'],axis=1,inplace =True)
df.drop(['HourOfCall'],axis=1,inplace =True)
df.drop(['IncGeo_BoroughCode'],axis=1,inplace =True)
df.drop(['IncGeo_WardCode'],axis=1,inplace =True)
df.drop(['IncGeo_WardNameNew'],axis=1,inplace =True)
df.drop(['NumStationsWithPumpsAttending'],axis=1,inplace =True)
df.drop(['PropertyType'],axis=1,inplace =True)
df.drop(['SpecialServiceType'],axis=1,inplace =True)
df.drop(['StopCodeDescription'],axis=1,inplace =True)
df.drop(['IncidentGroup'],axis=1,inplace =True)
df.drop(['Resource_Code'],axis=1,inplace =True)
df.drop(['IncidentStationGround'],axis=1,inplace =True)
df.drop(['CallYear'],axis=1,inplace =True)
df.drop(['DelayCode_Description'],axis=1,inplace =True)
df.drop(['AddressQualifier'],axis=1,inplace =True)
df.drop(['Latitude'],axis=1,inplace =True)
df.drop(['Longitude'],axis=1,inplace =True)

#Encodage des colonnes
df = df.join(pd.get_dummies(df['DeployedFromStation_Name'],prefix='DeployedFromSt'))
df.drop(['DeployedFromStation_Name'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['PlusCode_Description'],prefix='PlusCode'))
df.drop(['PlusCode_Description'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['IncGeo_BoroughName'],prefix='Borough'))
df.drop(['IncGeo_BoroughName'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['Postcode_district'],prefix='District'))
df.drop(['Postcode_district'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['PropertyCategory'],prefix='Property'))
df.drop(['PropertyCategory'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['CallMonth'],prefix='Month'))
df.drop(['CallMonth'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['CallDay'],prefix='Day'))
df.drop(['CallDay'],axis=1,inplace =True)
df = df.join(pd.get_dummies(df['IncidentTypeGlobal'],prefix='IncidentType'))
df.drop(['IncidentTypeGlobal'],axis=1,inplace =True)


#Transformation de la variable time of call en heure décimale
df['TimeOfCall']=pd.to_datetime(df['TimeOfCall'],format='%Y-%m-%d %H:%M:%S')
df['TimeOfCall']=df['TimeOfCall'].dt.hour+round(df['TimeOfCall'].dt.minute/60, 2)


#Tri chronologique des données
df['DateOfCall']=pd.to_datetime(df['DateOfCall'],format='%Y-%m-%d %H:%M:%S')
df=df.sort_values('DateOfCall')
df.drop(['DateOfCall'],axis=1,inplace =True)

#Réduction du dataset trop volumineux
df=df[-250000:]

## résolution de l'erreur des caractères JSON dans les noms des colonnes pour le LGBMRegressor
df = df.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))

#Création des DataFrames de features et target
target=df['AttendanceTimeSeconds']
data=df.drop('AttendanceTimeSeconds',axis=1)

#Création du modèle LGBM
lgbm4=LGBMRegressor(learning_rate=0.1512198354101122,max_depth=17,n_estimators=295,reg_alpha=0.0005383830447172724,
                    reg_lambda=0.00011538095876075694, num_leaves= 32, min_split_gain= 0.473924522550586, min_child_samples= 43)

#Entraînement du modèle sur le jeu de données complet
lgbm4.fit(data,target)

#Sauvegarde du modèle
dump(lgbm4,'models/lgbm4.joblib')









