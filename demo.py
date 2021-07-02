# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split


import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import generate_train_data
from modelisation import get_model

from geopy.geocoders import Nominatim



page = st.sidebar.radio("", options = ['Présentation', 'Modélisation','Application']) 

#df = pd.read_csv("train.csv", index_col = 'PassengerId')

if page == 'Présentation':
    st.title("Démo Streamlit Mar21 DA DS")
    
    st.markdown("""
                Ce projet va entraîner un modèle de Machine Learning
                sur le dataset du [titanic](https://www.kaggle.com/c/titanic/overview).
                
                                
                
                """)
    
#    img = plt.imread("assets/titanic.jpg")
    
#    st.image(img)
    
    #sns.countplot(df['Survived'])
    
    fig = plt.gcf()

    #st.pyplot(fig) 
    
    
    
    st.markdown("""
                Voici un aperçu du dataset.
                
                """)
    st.write(df)

if page == 'Modélisation':
    
    # Import et nettoyage des données
    
    X, y = generate_train_data()
    
    # Split des données
    
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 1)
    
    # Entrainement du modèle
    
    options = ['Regression Logistique', 'KNN', 'Decision Tree']
    
    choix = st.radio("Choisissez un modèle", options = options) 
    
    model, score = get_model(choix, X_train, y_train, X_test, y_test)
           
        
    st.markdown("""
                Ce modèle a obtenu un score de :
                
                """)    
    st.write(score)

if page == 'Application':
    #st.title,image...
    options = ['Je renseigne une adresse postale',
               'Je sélectionne un point sur la carte', 
               'Je renseigne les coordonnées géographiques (au format xxx)']
    choix = st.radio("Choisissez un modèle", options = options) 

    if choix==options[0]:
        adress=st.text_input("Saisissez une adresse", key="adress")
        geolocator = Nominatim(user_agent="projet_pompier")
        location = geolocator.geocode(adress)
        if location==None:
            st.write("Les coordonnées de votre adresse sont inconnues.")
        else:
            lat=location.latitude
            lon=location.longitude
            coord=(lat,lon)
            st.write("Les coordonnées de votre adresse sont :",coord)
            date=st.date_input("Date d'appel")
            time=st.time_input("Heure d'appel")

#    if choix==options[1]:
        
#    if choix==options[2]:




