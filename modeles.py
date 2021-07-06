# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:31:26 2021

@author: Elora, Marie, Nicolas
"""

import streamlit as st
import pandas as pd
#from pyproj import Proj, transform
from bokeh.palettes import brewer
from bokeh.plotting import figure, output_notebook, show
output_notebook()
import bokeh.tile_providers
from bokeh.models import ColumnDataSource, LabelSet,HoverTool,ColorBar,LinearColorMapper
from bokeh.models.widgets import Panel, Tabs
from bokeh.plotting import figure


def affichage_mod():

    st.markdown("""

                <h2>2 - MODELISATION</h2>

                <h3>A - Preprocessing des données</h3> 
                <br\>
                Une fois l’analyse du dataset réalisée, nous avons procédé au nettoyage et au preprocessing des données, afin d’assurer le bon déroulement de la phase de modélisation.
                <br/>
                Nous avons donc déterminé : 
                </br><ul><li>Les variables explicatives à supprimer : celles n’ayant pas influence sur notre variable cible ou étant redondantes avec d’autres variables ainsi que celles n'étant connues qu'à posteriori. </li></br><li>Les variables explicatives à convertir : dichotomisation des variables catégorielles, conversion de la variable ‘TimeOfCall’ en variable numérique (float). </li> </br><li>Les variables explicatives à créer : fusion des 2 variables liées ‘SpecialServiceType’ et ‘StopCodeDescription’ en une variable unique ‘IncidentTypeGlobal’, puis, une fois les coordonnées géographiques des casernes récupérées, création d’une variable ‘distFromStation’ indiquant la distance entre le lieu de l’intervention et la caserne étant intervenue et suppression des coordonnées (car nous avons déjà les variables Borough - quartier - et DeployedFromStation - station de déploiement - qui donnent des indications sur l’emplacement de l’incident). </li></ul>
                </br><br/>

                La majeure partie de nos features étant des variables catégorielles contenant de nombreuses modalités pour la plupart, la dichotomisation a ainsi généré un dataset final avant modélisation de dimension conséquente avec 549 colonnes pour environ 680 000 lignes.<br/><br/>
                Nous avons ensuite mis en place un Train Test split en nous assurant que les données les plus récentes soient conservées pour le test.<br/><br/>
                Enfin, nous avons procédé à l’étape de scaling afin de générer un dataset normalisé pour les modèles qui le nécessitent.
                <br/>

                <h4> i - Première itération </h4> 

                <h5><li> Modèles entraînés </li></h5> 
                <br/>
                Les modèles qu'on a instanciés dans un premier temps sont les modèles de régression linéaires classiques (LinearRegression seul puis avec SelectKBest et SelectFromModel, ElasticNetCV), HistGradientBoosting, DecisionTree, ainsi que Lasso et Ridge. Nous avons décidé de ne pas tester KNN qui n'est pas adapté aux gros datasets de par son mode de calcul.
                <br><br/>
                Nous avons recherché les hyper-paramètres optimaux à l'aide d'une GridSearch pour les modèles qui le permettaient.
                <br/>    
                <h5><li> Contraintes rencontrées </li></h5> 
                <br/>
                Nous avons rencontré de nombreuses difficultés techniques liées à la taille du dataset (memory error, interruption kernels et temps de calculs extrêmement importants… ).
                <br/><br/>
                Nous avons donc dû nous limiter à un dataset contenant les 250 000 dernières lignes (les plus récentes).
                <br/>
                
                <h5><li> Résultats obtenus </li></h5> 
                <br/>

                >   |    | model                               |   R² train |      R² test |   mse train |        mse test |   mae train |         mae test | paramètres retenus                                                                                                                                                          |
                |---:|:------------------------------------|-----------:|-------------:|------------:|----------------:|------------:|-----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                |  0 | LinearRegression                    |   0.324491 | -4.21421e+12 |     11500.1 |     6.37987e+16 |     70.1761 | 922374           |                                                                                                                                                                             |
                |  1 | SelectKBest régression linéaire     |   0.299405 |  0.338849    |     11927.2 | 10009.1         |     72.2332 |     68.5351      | f_regression,k=100,nb_cols=100                                                                                                                                              |
                |  2 | SelectFromModel régression linéaire |   0.068366 | -2.02101e+15 |     15860.5 |     3.05961e+19 |     89.8018 |      2.01978e+07 | nb_cols=111                                                                                                                                                                 |
                |  3 | ElasticNetCV                        |   0.323789 |  0.355323    |     11512.1 |  9759.74        |     70.2753 |     67.4525      | alpha :  0.05 parmi alphas=(0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0), l1_ratio :  0.75 parmi l1_ratio=(0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.99)    |
                |  4 | LassoCV                             |   0.32375  |  0.356218    |     11512.7 |  9746.19        |     70.1925 |     67.3646      | alpha=0.066393                                                                                                                                                              |
                |  5 | RidgeCV                             |   0.324491 |  0.35625     |     11500.1 |  9745.71        |     70.1762 |     67.3651      | alpha=1 parmi alphas= (0.0001,0.0005,0.001, 0.005,0.01, 0.05,0.1,0.5,1)                                                                                                     |
                |  6 | DecisionTree                        |   0.344382 |  0.347896    |     11161.5 |  9872.18        |     70.5671 |     67.6965      | max_depth=7 parmi [2, 3, 4, 5, 6, 7, 8], criterion=friedman_mse                                                                                                             |
                |  7 | DecisionTree                        |   0.344382 |  0.347034    |     11161.5 |  9885.23        |     70.5671 |     67.7137      | max_depth=7 parmi [2, 3, 4, 5, 6, 7, 8], criterion=mse                                                                                                                      |
                |  8 | HistGradientBoosting                |   0.391331 |  0.389738    |     10362.2 |  9238.74        |     66.6608 |     64.8576      | min_samples_leaf = 500, loss=least_squares parmi [least_squares,least_absolute_deviation], max_iter=250 parmi [50,70,100,120,150,170,200,250], max_depth=8 parmi range(3,9) |
                > 
                <br/><br/>
                Le modèle le plus performant est le modèle Hist Gradient Boosting quelque soit le critère de performance observé : il présente les R² les plus élevés ainsi que les MSE et MAE les plus faibles.

                <br><br/>
                Pour cette première itération, nous obtenons pour l’ensemble de nos tests, hormis pour le HistGradientBoosting :

                > <ul><li> Des scores R² peu concluants</li>
                > <li>Des MAE d'environ une minute et 10 secondes pour la plupart des modèles.</li></ul>

                <br><br/>

                Suite à cette itération, nous avons essayé de renouveler l'expérience avec ces modèles sur le dataset complet. Nous avons préparer les codes de ces modèles en élargissant les plages de recherche d'hyper-paramètres et en créant des pipelines pour les modèles qui le nécessitaient afin que notre mentor puisse les faire tourner sur ces machines, plus puissantes. Malheureusement, un des modèle à bloqué le kernel qui n'avait toujours pas abouti après plus de 24h et nous n'en avons récupéré aucun résultat.
                <br/>
                
                <h4> ii - Deuxième itération </h4> 

                <h5><li> Objectifs </li></h5>
                <br/>
                Suite à notre échec précédent, nous avons repris notre dataset réduit avec les 250 000 mobilisations les plus récentes. Nous avons essayé d'améliorer les premières performances obtenues grâce au modèle HistGradientBoosting.
                <br/><br/>
                Nous avons décidé d’optimiser la recherche d’hyper-paramètres à l’aide du package Optuna. Optuna a le même objectif que la GridSearchCV&#8239;: il permet de trouver la combinaison d'hyper-paramètres la plus performante. Cependant, il n'opère pas de la même manière. Tandis que la GridSearch évalue toutes les combinaisons d'hyper-paramètres existantes parmi les valeurs qui lui ont été fournies, ce sont des plages de valeurs qui sont fournies à Optuna. Cela lui permet d'explorer l'ensemble de l'espace sans avoir à tester toutes les combinaisons pour un paramètre ayant peu d'influence par exemple.
                <br/><br/>
                Nous avons également remplacé HistGradientBoosting par LightGBM qui est optimisé en temps de calcul.
                <br/><br/>
                Au cours des différentes itérations, il a fallu déterminer si nous étions en régime de sur ou sous-apprentissage et le combattre.
                <br/><br/>

                """,unsafe_allow_html = True)

