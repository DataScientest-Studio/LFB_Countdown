# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

import streamlit as st
import pandas as pd
import datetime

from preprocessing import generate_test_data
from presentation import affichage_pres

from geopy.geocoders import Nominatim


st.sidebar.image('figures/logoLFB.png')
st.sidebar.markdown("<br>",unsafe_allow_html = True)
page = st.sidebar.radio("", options = ['Présentation', 'Application']) 
st.sidebar.markdown("<br><br><br>",unsafe_allow_html = True)
st.sidebar.image('figures/LogoDatascientest.png')

boroughs = pd.read_csv("data/boroughs.csv", index_col = 0)
district = pd.read_csv("data/district.csv", index_col = 0)
type_incident = pd.read_csv("data/type_incident.csv", index_col = 0)
property_type = pd.read_csv("data/property_type.csv", index_col = 0)


if page == 'Présentation':
    st.title("Projet London Fire Brigade CountDown")
    
    affichage_pres()
    




if page == 'Application':
    st.image("figures/header.png")
    st.image("figures/simulation.png")
    st.image("figures/date.png")
    date=str(st.date_input("Date d'appel"))
    timeofcall=str(st.time_input("Heure d'appel"))

    st.image("figures/type.png")
    inc=st.selectbox("Choisissez le type d'incident",type_incident['type_incident'])
    st.image("figures/localisation.png")
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
        stat,res=generate_test_data(date,timeofcall,inc,prop,bor,dis,lat,lon)
        
        st.write('La caserne', stat,'prend en charge votre alerte.')
        
        hour=int(timeofcall.split(':')[0])
        minute=int(timeofcall.split(':')[1])
        second=int(timeofcall.split(':')[2][:2])
        
        timecall=second+60*minute+3600*hour
        
        timea1=timecall+res[5]
        timea2=timecall+res[1]
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
        tempsa1min=str(int(res[5]//60))
        tempsa1sec=str(int(res[5]%60))
        if int(tempsa1sec)<10:
            tempsa1sec='0'+tempsa1sec
        tempsa2min=str(int(res[1]//60))
        tempsa2sec=str(int(res[1]%60))
        if int(tempsa2sec)<10:
            tempsa2sec='0'+tempsa2sec
        stemps1='('+tempsa1min+'min '+tempsa1sec+'s)'
        stemps2='('+tempsa2min+'min '+tempsa2sec+'s)'
        st.write('Les secours arriveront sur place entre',stimea1,stemps1,'et',stimea2,stemps2)
        

    
        
