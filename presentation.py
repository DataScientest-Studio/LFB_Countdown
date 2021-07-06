# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""
import streamlit as st
import pandas as pd
#from pyproj import Proj, transform
from bokeh.palettes import brewer
import bokeh.tile_providers
from bokeh.models import ColumnDataSource, HoverTool,ColorBar,LinearColorMapper
from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure


def affichage_pres():
    st.markdown("""
                <center><h3>Elora VABOIS, Marie LE COZ, Nicolas RAYMOND</h3></center>\n
                
                <center><h3>DA Bootcamp Mai 2021</h3></center>\n
                
                \n
                \n
                
                <h2>INTRODUCTION</h2>
                <br/>
                
                >   Dans le cadre de notre formation Data Analyst, un projet fil rouge nous est proposé nous donnant ainsi l'opportunité d'appliquer sur un cas concret et global les connaissances acquises tout au long de notre parcours. Le choix du sujet a été une étape cruciale pour notre équipe et nous avons finalement jeté notre dévolu sur un des projets proposés dans le catalogue fourni : « Prédiction du temps de réponse d’un véhicule de la Brigade des Pompiers de Londres ».
                >   <br/><br/>
                >   Au delà du sujet en lui-même, ce choix résulte en grande partie de la richesse des données exploitables, la variété des types d'analyse que nous avons rapidement identifiés (temporelles, géographiques, etc.) et des applications qu'elles entraîneraient. Nous avions également à coeur de travailler sur un sujet pour lequel nous percevions un challenge en Machine Learning. 
                >   <br/><br/>
                >   Ce projet vise à étudier l'ensemble des différents incidents auxquels ont répondu et pour lesquels sont intervenus les pompiers de la célèbre brigade de Londres entre 2009 et 2021, avec pour objectif final de pouvoir prédire le temps d'attente des pompiers pour les incidents ultérieurs. 
                >   <br/><br/>
                <h2>PRESENTATION DES DONNEES</h2>
                
                >   </br>Nous avons à notre disposition 3 jeux de données officielles afin d'analyser les contours du projet : 
                >   <ul><li>Un fichier regroupant tous les incidents entre 2009 et 2021 </li>
                >   <li>Un fichier regroupant tous les déploiements sur ces incidents (matériels) sur la même période </li> 
                >   <li>Un fichier récent de la liste des casernes de la brigade </li></ul>
                >   <br/>
                >   Les données fournies dans le fichier "Incident" sont indexées sur le numéro de l'incident. Pour chacun, de nombreuses informations nous sont fournies, à commencer par la date et l'heure de l'appel, plusieurs éléments relatifs au lieu de l'incident (adresse, type de lieu), la nature de l'incident, le temps d'attente entre l'appel et l'arrivée du premier véhicule, etc ...
                <br/><br/>
                >   Le fichier "Mobilisation" nous renseigne sur le déploiement des véhicules pour chaque incident, et contient le numéro de l'incident sur lequel ils sont envoyés, le type de véhicule, le temps de mobilisation avant le départ de ce véhicule, son temps de trajet, l'heure d'arrivée sur les lieux. Parfois, plusieurs véhicules peuvent être déployés sur le même incident. Dans ce cas de figure, nous disposons d'une variable indiquant l'ordre d'appel de ces véhicules. Enfin, pour une partie des données, la latitude et la longitude du lieu de l'incident sont renseignées.
                <br/><br/>
                >   La liste des casernes ayant évolué sur la période que couvre notre dataset, la London Fire Brigade nous a aimablement fourni sur demande la liste exhaustive des casernes en activité à ce jour sous leur giron ainsi que les adresses correspondantes.
                <br/><br/>
                >   Le but de notre étude est de pouvoir mettre en place un modèle prédictif qui indiquera le temps d'attente entre un appel et l'arrivée des secours sur place en fonction de plusieurs critères à déterminer. 
                <br/>
                <br/>
                """,unsafe_allow_html = True)

    