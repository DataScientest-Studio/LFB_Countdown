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
                <h2>1 - ANALYSE DES DONNEES</h2>
                <br/>
                <h3>A - Introduction aux données</h3> 
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
                <h3>B - Analyse des données</h3> 
                <h4>i - Analyse des incidents en fonction des variables temporelles </h4> 
  
                >   Une première approche simple nous permet de vérifier visuellement si les différents facteurs temporels (mois, jour de la semaine, heure de la journée) ont une influence sur le nombre d'incidents :
                   
                """,unsafe_allow_html = True)
                
                
    st.image("figures\Moyenne_par_mois.png", width=600)
    st.image("figures\Moyenne_par_jour.png", width=600)
    st.image("figures\Moyenne_par_heures.png", width=600)
    
    st.markdown("""
                
                >   
                >   Nous pouvons remarquer que le nombre moyen d'incidents varie plus ou moins fortement selon ces facteurs :
                >   <ul><li> Un nombre moyen d'incidents plus important sur les mois estivaux (de mai à septembre) par rapport au reste de l'année, avec un pic sur le mois de juillet.</li>
                >   <li> Une relation que l'on retrouve en moindre mesure en fonction des jours de la semaine : une densité d'incidents un peu plus forte les vendredi et surtout samedi, mais comparable sur les autres jours.</li>
                >   <li> Et enfin, assez logiquement, une forte influence de l'horaire sur le nombre moyen d'incidents : une densité bien plus forte sur les heures de la journée avec un pic en fin d'après-midi/début de soirée.</li></ul>
                >   
                >   
                >   Nous avons ensuite réalisé des tests statistiques afin de vérifier que ces constats se vérifient. Nos 3 tests ANOVA concernant l'influence de nos 3 variables temporelles sur le nombre d'incidents moyen, nous indique que l'hypothèse selon laquelle les variables sont indépendantes est rejetée avec des p values extrêmement proches de 0. Nos 3 variables temporelles ont donc un effet statistique significatif sur le nombre d'incidents moyen.
                
                ><br/> Mois 
                
                >   |          |    df |         sum_sq |   mean_sq |        F |        PR(>F) |
                |:---------|------:|---------------:|----------:|---------:|--------------:|
                | Mois     |     1 | 3026.22        |  3026.22  |  25.8373 |   3.72452e-07 |
                | Residual | 65558 |    7.67853e+06 |   117.126 | nan      | nan           |
                <br/>
                <br/> Jours
                
                >   |          |     df |     sum_sq |   mean_sq |       F |        PR(>F) |
                |:---------|-------:|-----------:|----------:|--------:|--------------:|
                | jours    |      1 |    193.354 | 193.354   |  53.912 |   2.10278e-13 |
                | Residual | 259735 | 931530     |   3.58646 | nan     | nan           |
                <br/>
                <br/> Heures
                
                >   |          |     df |    sum_sq |    mean_sq |       F |        PR(>F) |
                |:---------|-------:|----------:|-----------:|--------:|--------------:|
                | heures   |      1 |    25.594 | 25.594     | 383.153 |   3.20373e-85 |
                | Residual | 164639 | 10997.6   |  0.0667985 | nan     | nan           |
                >  
                <br/><br/>
                >   Nous nous sommes également intéressés à savoir si ces mêmes variables pouvaient avoir une incidence sur le temps d'attente, c'est-à-dire le temps passé entre l'appel des secours et leur arrivée sur place.
                >   
                <br/>
                """,unsafe_allow_html = True)
    st.image("figures\Temps_attente_par_mois.png",width = 600)
    st.image("figures\Temps_attente_par_jour.png", width=600)
    st.image("figures\Temps_attente_par_heures.png", width=600)
    st.markdown("""
       
                <br/><br/>
                >   Les variations sur le temps d'attente sont moins flagrantes, mais s'expliquent en grande partie par le fait que cette variable n'a pas une grande amplitude de manière générale.<br/><br/>
                Néanmoins, certains enseignements se recoupent avec la distribution des incidents décrite plus haut :
                >   <ul><li> Le temps d'attente est sensiblement plus important sur les mois estivaux, tout comme l'était la densité des incidents.</li>
                >   <li> En revanche, nous n'observons pas de relation clairement visible entre le temps d'attente et le jour de la semaine ou l'heure de la journée.</li></ul>
                <br/><br/>
                >   Nous avons également vérifié à l'aide de tests ANOVA si ces variables temporelles influencent significativement le temps d'attente. 
                ><br/> Mois
                
                >   |          |    df |      sum_sq |        mean_sq |        F |        PR(>F) |
                |:---------|------:|------------:|---------------:|---------:|--------------:|
                | Mois     |     1 | 1.2569e+06  |     1.2569e+06 |  18.1985 |   1.99319e-05 |
                | Residual | 65558 | 4.52786e+09 | 69066.4        | nan      | nan           |
                <br/>
                <br/> Jours
                
                >   |          |     df |         sum_sq |   mean_sq |           F |    PR(>F) |
                |:---------|-------:|---------------:|----------:|------------:|----------:|
                | jours    |      1 | 2202.49        |   2202.49 |   0.0636286 |   0.80085 |
                | Residual | 259735 |    8.99067e+09 |  34614.8  | nan         | nan       |
                <br/>
                <br/> Heures
                
                >   |          |     df |      sum_sq |         mean_sq |       F |        PR(>F) |
                |:---------|-------:|------------:|----------------:|--------:|--------------:|
                | heures   |      1 | 3.72604e+06 |     3.72604e+06 | 211.216 |   7.98411e-48 |
                | Residual | 164639 | 2.90438e+09 | 17640.9         | nan     | nan           |
                >   
                <br/><br/>
                >   Pour ces 3 tests, nous avons posé l'hypothèse que le temps d'attente est indépendant du mois, du jour de la semaine et de l'heure de l'incident.
                Les p values des tests liés au mois et à l'heure de l'incident sont extrêment proches de 0, nous pouvons donc noter un effet statistique significatif de ces variables sur le temps d'attente. La p value du test lié au jour de la semaine est d'environ 80 %, indiquant donc cette variable n'a pas d'effet statistique significatif sur le temps d'attente des secours.
                
                <br/>
                <h4>ii - Analyse en fonction du type d'incident </h4> 
                >   Au-delà des facteurs temporels, nous nous sommes également demandé s'il pouvait exister un lien entre le temps d'attente et la nature de l'incident. En effet, selon le type d'incident, les besoins peuvent être différents en termes de type de véhicule à déployer, ce qui peut influencer le temps de déploiement en fonction de la disponibilité du véhicule par exemple.
                <br/><br/>
                Regardons tout d'abord la répartition des types d'incidents traités par la London Fire Brigade depuis 2014 :
                <br/>
                """,unsafe_allow_html = True)

    st.image("figures\Moyenne_par_type.png", width=600)
    st.markdown("""
                <br/>
                On remarque que la grande majorité des sources d'intervention sont liées aux Alarmes Automatiques d'Incendie. Ensuite, et dans une moindre mesure, on retrouve comme autres raisons principales : les incendies, les opérations d'entrée-sortie de personnes, les innondations puis les accidents de la route. D'après notre test ANOVA, le type d'incident a un lien significatif avec le nombre d'incidents (p value nulle).
                  
                >  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
                |:---------|------:|------------:|----------------:|--------:|---------:|
                | type     |    25 | 9.44883e+07 |     3.77953e+06 | 238.183 |        0 |
                | Residual | 17218 | 2.73218e+08 | 15868.1         | nan     |      nan |
                >  
                <br/><br/>
                Ici encore, nous vérifions l'incidence sur le temps d'attente visuellement puis statistiquement.
                <br/>
                """,unsafe_allow_html = True)
    st.image("figures\Temps_attente_par_type.png", width=800)
    st.markdown("""
                <br/>
                >   Le temps d'attente évolue donc du simple au double selon le type d'incident. La LFB met deux fois plus de temps pour se rendre sur un incendie que pour porter secours lors d'une noyade.
                Cette influence de la nature de l'intervention sur le temps d'attente est par ailleurs confirmée par le test ANOVA qui indique un lien significatif entre les deux variables (p value nulle).
                 
                >  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
                |:---------|------:|------------:|----------------:|--------:|---------:|
                | type     |    25 | 1.34913e+08 |     5.39652e+06 |  69.132 |        0 |
                | Residual | 17218 | 1.34406e+09 | 78061.1         | nan     |      nan |
                
                <br/>
                <h4>iii - Analyse en fonction de la localisation de l'incident </h4> 
                
                >   Dans un premier temps, nous avons souhaité visualiser l'ensemble des incidents en fonction de leur localisation, en colorant chaque point, représentant un incident, en fonction de la station qui a répondu en premier sur l'intervention.
                <br/><br/>
                >   Ceci nous permet de voir la répartition des stations et leur rayon d'action :
                <br/>
                """,unsafe_allow_html = True)

    st.image("figures\Carte_incident_station.png")
    st.markdown("""
                ><br/>
                Le test ANOVA évaluant l'indépendance de la station de déploiement du temps d'attente nous montre un lien significatif entre ces variables (p value nulle). On peut donc supposer que : soit certaines stations sont intrinsèquement plus performantes que d'autres (grâce à des équipes plus expérimentées par exemple), soit c'est l'emplacement des stations qui va agir indirectement sur le temps d'attente.
                 
                >   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
                |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
                | DeployedFromStation_Code |    101 | 5.69136e+08 |     5.63501e+06 | 315.144 |        0 |
                | Residual                 | 683719 | 1.22254e+10 | 17880.7         | nan     |      nan |
                >   
                <br/>
                Nous avons également prêté attention à la densité des incidents répartis sur l'ensemble de la ville (ici en 2020) : 
                """,unsafe_allow_html = True)
                
                
    stations=pd.read_csv('data/Stations_clean.csv',index_col=0)
    df=pd.read_csv('data/LFB_incident_clean.csv', index_col=0)
    
    
    
    dfgeo=df[['IncidentNumber','Latitude','Longitude','CallYear','DeployedFromStation_Name','AttendanceTimeSeconds']]
    
    dfgeo['Longmerc'],dfgeo['Latmerc']=transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), dfgeo['Longitude'].values, dfgeo['Latitude'].values)
    stations['Longmerc'],stations['Latmerc']=(transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), stations['Longitude'].values, stations['Latitude'].values));
    dfgeo21=dfgeo[dfgeo['CallYear']==2021].sample(7000)
    dfgeo20f=dfgeo[dfgeo['CallYear']==2020].sample(5000)
    dfgeo20=dfgeo[dfgeo['CallYear']==2020].sample(7000)
    dfgeo19=dfgeo[dfgeo['CallYear']==2019].sample(7000)
    sourcest=ColumnDataSource(data=stations)

    source21=ColumnDataSource(data=dfgeo21)
    source20f=ColumnDataSource(data=dfgeo20f)
    source20=ColumnDataSource(data=dfgeo20)
    source19=ColumnDataSource(data=dfgeo19)
    
    
    tuile=bokeh.tile_providers.get_provider('CARTODBPOSITRON')
    p=figure(title='Densité des incidents en 2020',x_axis_label='Longitude',y_axis_label='Latitude',
         width=900,height=600,x_range=(-53000, 31000), y_range=(6660000, 6755000), x_axis_type='mercator', y_axis_type ='mercator')
    p.add_tile(tuile)
    p.circle(source=source20f,x='Longmerc',y='Latmerc',alpha=0.1)
    s=p.triangle(source=sourcest,x='Longmerc',y='Latmerc',color='red',size=10)
    hover=HoverTool(renderers=[s],tooltips=[("station", "@NomStation")])
    p.add_tools(hover) 
    
    st.bokeh_chart(p, use_container_width=True)
    
    
    
    
    st.markdown("""
                >   Comme nous nous y attendions, les incidents sont plus nombreux au centre-ville qu'en périphérie, tout comme le sont les stations.
                <br/><br/>
                
                >   Le test ANOVA entre le nombre d'incidents et le district (PostCode_district) du lieu d'incident indique un lien significatif entre ces variables (p value nulle).
                  
                >   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
                |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
                | District |    328.0 | 3.343984e+08 |     1.019507e+06 | 22.724574 |        0 |
                | Residual                 | 134211.0 | 6.021195e+09 | 4.486365e+04         | nan     |      nan |
                >
                >   <br/>
                > Nous avons ensuite souhaité voir la répartition géographique des incidents sur la carte de Londres, en filtrant les données par année et en colorant ces points par rapport aux temps d'attente (les points verts représentant les temps d'attente les plus faibles, les points rouges les plus longs). Nous avons inséré les stations sur cette carte (triangles noirs) afin de visualiser l'impact de la proximité avec une station sur le délai d'intervention.
                """,unsafe_allow_html = True)
                
    sourcest2=ColumnDataSource(data=stations)            
    tuile=bokeh.tile_providers.get_provider('CARTODBPOSITRON')


    palette = brewer['RdYlGn'][10]
    color_mapper = LinearColorMapper(palette=palette, low=179, high=476)
    color_bar = ColorBar(color_mapper=color_mapper, width=8,location=(0,0), label_standoff=8)



    p21=figure(title="Incidents colorés par temps d'attente (en s) en 2021",x_axis_label='Longitude',y_axis_label='Latitude',tools=['box_select','lasso_select'],
         width=900,height=600,x_range=(-53000, 31000), y_range=(6660000, 6755000), x_axis_type='mercator', y_axis_type ='mercator')
    p21.add_tile(tuile)
    p21.circle(source=source21,x='Longmerc',y='Latmerc',alpha=0.3,color = {'field' :'AttendanceTimeSeconds', 'transform' : color_mapper})
    s21=p21.triangle(source=sourcest2,x='Longmerc',y='Latmerc',color='black',size=7)


    p20=figure(title="Incidents colorés par temps d'attente (en s) en 2020",x_axis_label='Longitude',y_axis_label='Latitude',
         width=900,height=600,x_range = p21.x_range, y_range = p21.y_range, x_axis_type='mercator', y_axis_type ='mercator')
    p20.add_tile(tuile)
    p20.circle(source=source20,x='Longmerc',y='Latmerc',alpha=0.2,color = {'field' :'AttendanceTimeSeconds', 'transform' : color_mapper})
    s20=p20.triangle(source=sourcest2,x='Longmerc',y='Latmerc',color='black',size=7)


    p19=figure(title="Incidents colorés par temps d'attente (en s) en 2019",x_axis_label='Longitude',y_axis_label='Latitude',
         width=900,height=600,x_range = p21.x_range, y_range = p21.y_range, x_axis_type='mercator', y_axis_type ='mercator')
    p19.add_tile(tuile)
    p19.circle(source=source19,x='Longmerc',y='Latmerc',alpha=0.2,color = {'field' :'AttendanceTimeSeconds', 'transform' : color_mapper})
    s19=p19.triangle(source=sourcest2,x='Longmerc',y='Latmerc',color='black',size=7)


    hover=HoverTool(renderers=[s19,s20,s21],tooltips=[("station", "@NomStation")])

    p21.add_layout(color_bar,  'left')
    p21.add_tools(hover)
    tab21 = Panel(child=p21, title="2021")
    p20.add_layout(color_bar, 'left')
    p20.add_tools(hover)
    tab20 = Panel(child=p20, title="2020")
    p19.add_layout(color_bar, 'left')
    p19.add_tools(hover)
    tab19 = Panel(child=p19, title="2019")



    tabs = Tabs(tabs=[tab19,tab20,tab21 ])
      
    st.bokeh_chart(tabs, use_container_width=True)          
                
    st.markdown("""           
                > Cette dernière visualisation permet de bien identifier les zones en fonction de la réactivité des secours. On observe que plus l'incident est éloigné d'une station, plus le temps d'attente tend à augmenter. 
                <br/><br/>
                
                >   Le test ANOVA qui concerne le temps d'attente et le district (PostCode_district) du lieu d'incident indique un lien significatif entre ces variables (p value nulle).
                
                >   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
                |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
                | District |    328.0 | 9.468728e+05 |     2886.807444 | 88.86169 |        0 |
                | Residual                 | 134211.0 | 4.360049e+06 | 32.486524         | nan     |      nan |
                >  
                
                <br/>
                
                >   De plus, le test de Pearson liant la distance entre le lieu d'incident et la station de déploiement avec le temps d'attente nous indique que ces variables ont un lien significatif (p value nulle) et que leur corrélation est relativement importante (coefficient de Pearson : 51.5%).
                   
                >   |                          |     résultat test |
                |:-------------------------|-------:|
                | pearson_coeff |    0.515065 | 
                | p-value                 | 0.000000 |
                
                <h4>iv - Autres tests statistiques réalisés </h4> 
                
                >   Nous avons également étudié la corrélation entre le type de retard éventuel (DelayCode_Description) et le temps d'attente et notre test ANOVA indique un lien significatif entre ces variables (p value nulle). Cependant, nous ne pourrons pas conserver cette variable pour la modélisation car elle n'est connu qu'à posteriori : elle ne peut donc pas servir à la prédiction.
                
                >   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
                |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
                | DelayCode_Description |    9.0 | 3.273134e+09 |     3.636815e+08 | 26118.986271 |        0 |
                | Residual                 | 683811.0 | 9.521404e+09 | 1.392403e+04         | nan     |      nan |
                
                <br/>
                
                <h3>C - Conclusion sur l'analyse des données</h3> 
                
                >   Cette première étape d'analyse des données nous confirme bien que les indicateurs étudiés seront indispensables dans le cadre de la modélisation du temps d'intervention de la LFB. 
                """,unsafe_allow_html = True)
            

    