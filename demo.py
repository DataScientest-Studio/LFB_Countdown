# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""
from lightgbm import LGBMRegressor
import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split


import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import generate_test_data
from modelisation import get_model

from geopy.geocoders import Nominatim
from presentation import affichage_pres


page = st.sidebar.radio("", options = ['Présentation', 'Modélisation','Application']) 

#st.sidebar.image('figures/LogoDatascientest.png')

boroughs = pd.read_csv("data/boroughs.csv", index_col = 0)
district = pd.read_csv("data/district.csv", index_col = 0)
type_incident = pd.read_csv("data/type_incident.csv", index_col = 0)
property_type = pd.read_csv("data/property_type.csv", index_col = 0)
#df = pd.read_csv("data/LFB_incident_clean.csv", index_col = 1)
#df=df[-250000:]
#print(df['IncGeo_BoroughName'].unique())


if page == 'Présentation':
    st.title("LFB CountDown")
    
    affichage_pres()
    
#    img = plt.imread("assets/titanic.jpg")
    
#    st.image(img)
    
    #sns.countplot(df['Survived'])
    
    #fig = plt.gcf()

(    #st.pyplot(fig) 
    
    
    
    #st.markdown("""
    #            Voici un aperçu du dataset.
                
    #            """)
    #st.write(df)

#if page == 'Modélisation':
    
    # Import et nettoyage des données
    
    #X, y = generate_train_data()
    
    # Split des données
    
    #X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 1)
    
    # Entrainement du modèle
    
    #options = ['Regression Logistique', 'KNN', 'Decision Tree']
    
    #choix = st.radio("Choisissez un modèle", options = options) 
    
    #model, score = get_model(choix, X_train, y_train, X_test, y_test)
           
        
    #st.markdown("""
     #           Ce modèle a obtenu un score de :
                
    #            """)    
    #st.write(score)

if page == 'Application':
    #st.title,image...
    
    date=st.date_input("Date d'appel")
    time=st.time_input("Heure d'appel")

    
    inc=st.selectbox("Choisissez le type d'incident",type_incident['type_incident'])
    
    prop=st.selectbox('Choisissez le type de lieu',property_type['property_type'])
    
    options = ['Je renseigne les coordonnées géographiques',
               'Je renseigne une adresse postale',
               #'Je sélectionne un point sur la carte'
               ]
    choix = st.radio("Saisissez le lieu de l'incident", options = options) 
    
    
    geolocator = Nominatim(user_agent="projet_pompier")
    if choix==options[1]:
        address=st.text_input("Saisissez une adresse","Birch Close, Canning Town")
        location = geolocator.geocode(address)
        if location==None:
            st.write("Les coordonnées de votre adresse sont inconnues.")
        else:
            lat=location.latitude
            lon=location.longitude
            coord=lat,lon
            location = geolocator.reverse(coord)
            st.write("L'adresse suivante a été reconnue :", location.address)
            st.write("Les coordonnées de cette adresse sont :",coord)

        
    if choix==options[0]:
        lat=st.number_input("Saisissez la latitude", 51.0,52.0,51.5181388,format='%.7f',step=0.00001)
        lon=st.number_input("Saisissez la longitude", -1.0,1.0,0.0062938,format='%.7f',step=0.00001)
        coord=lat,lon
        location = geolocator.reverse(coord)
        st.write("L'adresse suivante a été reconnue :", location.address)
        
    
    bor_connu=False
    if 'city_district' in location.raw['address']:
        for i in range(len(boroughs)):
            if location.raw['address']['city_district'].split('of ')[-1].upper()==sorted(boroughs['boroughs'])[i]:  
                bor=st.selectbox('Confirmez le borough correspondant',sorted(boroughs['boroughs']),i)
                bor_connu=True
    if not bor_connu:
        bor=st.selectbox('Choisissez le borough correspondant',sorted(boroughs['boroughs']))
    dis_connu = False
    if 'postcode' in location.raw['address']:
        for i in range(len(district)):
            if location.raw['address']['postcode'].split(' ')[0]==sorted(district['district'])[i]:  
                dis=st.selectbox('Confirmez le district correspondant',sorted(district['district']),i)
                dis_connu = True
    if not dis_connu:
        dis=st.selectbox('Choisissez le district correspondant',sorted(district['district']))


    if st.button('Calculer'):
        stat,res=generate_test_data('2021-07-04','15:30:00','Suicide/attempts','Dwelling','Harrow','BR1',51.5181388,0.0062938)
        st.write('Le premier camion sera déployé depuis :', stat)
        st.write('Le temps de déploiement dépend du nombre de camions envoyés :')
        df=pd.DataFrame({'Nombre de camions':range(1,11),"Temps d'attente (en s)":res})
        st.dataframe(df)

    
        

#proposer le meilleur et également le top 3 des meilleures options

#streamlit.bokeh_chart