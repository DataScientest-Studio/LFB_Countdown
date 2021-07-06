# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""
from lightgbm import LGBMRegressor
import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim



from application_calculs import generate_test_data, affichage_resultat
from presentation import affichage_pres
from conclusion import affichage_conclu








#Sidebar
st.sidebar.image('figures/logoLFB.png')
st.sidebar.markdown("<br>",unsafe_allow_html = True)
page = st.sidebar.radio("", options = ['Présentation', 'Analyse des données','Modélisation','Conclusion','Application']) 
st.sidebar.markdown("<br><br>",unsafe_allow_html = True)
st.sidebar.image('figures/LogoDatascientest.png')

page = st.sidebar.radio("", options = ['Présentation', 'Modélisation','Application']) 


#Importation des fichiers
boroughs = pd.read_csv("data/boroughs.csv", index_col = 0)
district = pd.read_csv("data/district.csv", index_col = 0)
type_incident = pd.read_csv("data/type_incident.csv", index_col = 0)
property_type = pd.read_csv("data/property_type.csv", index_col = 0)


#Page Présentation
if page == 'Présentation':
    st.title("LFB CountDown")
    
    affichage_pres()
    

    
#Page Conclusion
if page== 'Conclusion':
    st.title("Bilan du projet")
    affichage_conclu()
    
#Page Application
if page == 'Application':
    #Header
    st.image("figures/header.png")
    st.image("figures/simulation.png")
    #Formulaire
    ##Date/heure
    st.image("figures/date.png")
    date=str(st.date_input("Date d'appel"))
    timeofcall=str(st.time_input("Heure d'appel"))
    ##Type
    st.image("figures/type.png")
    inc=st.selectbox("Choisissez le type d'incident",type_incident['type_incident'])
    ##Lieu
    st.image("figures/localisation.png")


if page == 'Application':
    
    st.image('figures/header.png')
    st.image('figures/date.png')
    date=st.date_input("Date d'appel")
    time=st.time_input("Heure d'appel")

    st.image('figures/type.png')
    inc=st.selectbox("Choisissez le type d'incident",type_incident['type_incident'])
    
    st.image('figures/localisation.png')
    prop=st.selectbox('Choisissez le type de lieu',property_type['property_type'])
    
    options = ['Je renseigne les coordonnées géographiques',
               'Je renseigne une adresse postale',]
    choix = st.radio("Saisissez le lieu de l'incident", options = options) 
    
    #Utilisation du package geopy pour définir l'adresse, les coordonnées, le borough et le district en 
    #fonction de la saisie utilisateur
    geolocator = Nominatim(user_agent="projet_pompier")
    #Pour les saisies d'adresse
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

    #Pour les saisies de coordonnées
    if choix==options[0]:
        lat=st.number_input("Saisissez la latitude", 51.0,52.0,51.5181388,format='%.7f',step=0.00001)
        lon=st.number_input("Saisissez la longitude", -1.0,1.0,0.0062938,format='%.7f',step=0.00001)
        coord=lat,lon
        location = geolocator.reverse(coord)
        st.write("L'adresse suivante a été reconnue :", location.address)
        
    #Détermination du borough
    bor_connu=False
    if 'city_district' in location.raw['address']:
        for i in range(len(boroughs)):
            if location.raw['address']['city_district'].split('of ')[-1].upper()==sorted(boroughs['boroughs'])[i]:  
                bor=st.selectbox('Confirmez le borough correspondant',sorted(boroughs['boroughs']),i)
                bor_connu=True
    #Si geopy ne détermine pas le quartier, c'est l'utilisateur qui doit le choisir
    if not bor_connu:
        bor=st.selectbox('Choisissez le borough correspondant',sorted(boroughs['boroughs']))
    #Determination du district
    dis_connu = False
    if 'postcode' in location.raw['address']:
        for i in range(len(district)):
            if location.raw['address']['postcode'].split(' ')[0]==sorted(district['district'])[i]:  
                dis=st.selectbox('Confirmez le district correspondant',sorted(district['district']),i)
                dis_connu = True
    #Si geopy ne détermine pas le district, c'est l'utilisateur qui doit le choisir
    if not dis_connu:
        dis=st.selectbox('Choisissez le district correspondant',sorted(district['district']))

    #Calcul de la prédiction
    if st.button('Calculer'):
        stat,res=generate_test_data(date,timeofcall,inc,prop,bor,dis,lat,lon)
        
        #Affichage de la station retenue
        st.write('La caserne **{}** prend en charge votre alerte.'.format(stat))
        
        #Calcul des temps et heures d'arrivée de la fourchette résultat
        stimea1,stimea2,stemps1,stemps2=affichage_resultat(timeofcall,res)
        
        #affichage des temps et heures calculés
        st.write('Les secours arriveront sur place entre **{}** {} et **{}** {}'.format(stimea1,stemps1,stimea2,stemps2))
