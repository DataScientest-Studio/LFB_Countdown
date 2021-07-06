# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

import streamlit as st
import pandas as pd


from preprocessing2 import generate_test_data


from geopy.geocoders import Nominatim


st.sidebar.image('figures/LogoLFB.png')
page = st.sidebar.radio("", options = ['Présentation', 'Application']) 

st.sidebar.image('figures/LogoDatascientest.png')

boroughs = pd.read_csv("data/boroughs.csv", index_col = 0)
district = pd.read_csv("data/district.csv", index_col = 0)
type_incident = pd.read_csv("data/type_incident.csv", index_col = 0)
property_type = pd.read_csv("data/property_type.csv", index_col = 0)


if page == 'Présentation':
    st.title("Démo Streamlit Mar21 DA DS")
    
    st.markdown("""
                Ce projet va entraîner un modèle de Machine Learning
                sur le dataset du [titanic](https://www.kaggle.com/c/titanic/overview).
                
                                
                <center><h3>Elora VABOIS, Marie LE COZ, Nicolas RAYMOND</h3></center>
                <center><h3>DA Bootcamp Mai 2021</h3></center>
                <br/><br/>
                """)
                
    st.header('titre')
    




if page == 'Application':
    #st.title,image...
    
    date=str(st.date_input("Date d'appel"))
    time=str(st.time_input("Heure d'appel"))

    
    inc=st.selectbox("Choisissez le type d'incident",type_incident['type_incident'])
    
    prop=st.selectbox('Choisissez le type de lieu',property_type['property_type'])
    
    options = ['Je renseigne les coordonnées géographiques',
               'Je renseigne une adresse postale',]
    
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
        stat,res=generate_test_data(date,time,inc,prop,bor,dis,lat,lon)
        st.write('Le premier véhicule sera déployé depuis :', stat)
        st.write('Le temps de déploiement dépend du nombre de camions envoyés :')
        df=pd.DataFrame({'Nombre de camions':range(1,11),"Temps d'attente (en s)":res})
        st.dataframe(df)

    
        

#proposer le meilleur et également le top 3 des meilleures options

#streamlit.bokeh_chart