# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:31:26 2021

@author: Elora, Marie, Nicolas
"""

import streamlit as st



def affichage_mod():

    st.markdown("""

                <h2> A - Preprocessing des données</h2> 
                <br>
                Une fois l’analyse du dataset réalisée, nous avons procédé au nettoyage et au preprocessing des données, afin d’assurer le bon déroulement de la phase de modélisation.
                <br>
                Nous avons donc déterminé : 
                <br><ul><li>Les variables explicatives à supprimer : celles n’ayant pas influence sur notre variable cible ou étant redondantes avec d’autres variables ainsi que celles n'étant connues qu'à posteriori. </li></br><li>Les variables explicatives à convertir : dichotomisation des variables catégorielles, conversion de la variable ‘TimeOfCall’ en variable numérique (float). </li> </br><li>Les variables explicatives à créer : fusion des 2 variables liées ‘SpecialServiceType’ et ‘StopCodeDescription’ en une variable unique ‘IncidentTypeGlobal’, puis, une fois les coordonnées géographiques des casernes récupérées, création d’une variable ‘distFromStation’ indiquant la distance entre le lieu de l’intervention et la caserne étant intervenue et suppression des coordonnées (car nous avons déjà les variables Borough - quartier - et DeployedFromStation - station de déploiement - qui donnent des indications sur l’emplacement de l’incident). </li></ul>
                <br>

                La majeure partie de nos features étant des variables catégorielles contenant de nombreuses modalités pour la plupart, la dichotomisation a ainsi généré un dataset final avant modélisation de dimension conséquente avec 549 colonnes pour environ 680 000 lignes.<br/><br/>
                Nous avons ensuite mis en place un Train Test split en nous assurant que les données les plus récentes soient conservées pour le test.<br/><br/>
                Enfin, nous avons procédé à l’étape de scaling afin de générer un dataset normalisé pour les modèles qui le nécessitent.
                <br>

                <h2> B - Modélisations<h2/>
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

                |    | model                               |   R² train |      R² test |   mse train |        mse test |   mae train |         mae test | paramètres retenus                                                                                                                                                          |
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
                 
                <br/><br/>
                Le modèle le plus performant est le modèle Hist Gradient Boosting quelque soit le critère de performance observé : il présente les R² les plus élevés ainsi que les MSE et MAE les plus faibles.

                <br>
                Pour cette première itération, nous obtenons pour l’ensemble de nos tests, hormis pour le HistGradientBoosting :

                <ul><li> Des scores R² peu concluants</li>
                <li>Des MAE d'environ une minute et 10 secondes pour la plupart des modèles.</li></ul>

                <br>

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
                <br/>
                
                <h5><li> Modèles entraînés et ajustement réalisés </li></h5>
                <br/>
                Nous avons entraîné le modèle LGBMRegressor avec le package Optuna. Nous avons procédé en plusieurs itérations pour trouver quels hyper-paramètres tester et sur quelles plages.
                <br/>
                <h2>C - Choix et interprétabilité du modèle</h2>

                
                
                """, unsafe_allow_html = True)
                
                
                
    st.markdown("""
                
                <h4> i - Modèle retenu  </h4> 
                <br/>
                
                | model                                                                            |   R² train |   R² test |   mse train |   mse test |   mae train |   mae test |
                |:---------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
                | LGBMRegressor1    |      0.454652 |     0.409216 |     9284.22 |    8943.85 |     62.8125 |    63.2457 ||
                | LGBMRegressor2   |      0.459334 |     0.410594 |     9204.50  |    8923.00    |     62.5320  |    63.1363 ||
                | LGBMRegressor3    |      0.463816 |     0.411167 |     9128.22 |    8914.33 |     62.1916 |    63.0520  ||
                | LGBMRegressor4     |      0.445746 |     0.410001 |     9435.83 |    8931.97 |     63.1968 |    63.1481 ||            |
                <br/>
                Finalement, nous avons décidé de retenir le modèle LGBMRegressor4 qui produit de bons résultats tout en exigeant un temps de calcul très raisonnable (non seulement par rapport aux modèles de la première itération puisque LightGBM est optimisé, mais également par rapport aux 3 premiers LGBMRegressor car c'est celui qui présente le n_estimators le plus faible). On pourra lui reprocher d’être peu interprétable mais nous allons essayer d’y remédier dans la partie suivante grâce aux packages Skater et Shap.
                <br/>
                <h4> ii - Interprétabilité du modèle  </h4> 

                <h5><li> Visualisation géographique de l'erreur </li></h5>
                <br/>
                Avant d'utiliser les packages d'interprétabilité, nous allons visualiser géographiquement l'erreur sur le jeu de données test, de manière à repérer d'éventuelles anomalies ou bien à confirmer la performance du modèle.
                <br/>
                
                
                
                
                """, unsafe_allow_html = True)
                
                
                
                
                
                
                
    st.markdown("""
                <br/>
                On peut voir sur cette figure que les erreurs importantes (nous avons représenté les erreurs de plus de 2 minutes en rouge) sont réparties de manière à peu près homogènes sur la carte. On peut cependant repérer qu'elles sont un peu plus présentes en périphérie de la ville. Cela peut être dû au fait que ces incidents - éloignés des stations - sont peu nombreux et subissent des conditions de trafic différentes de celles du centre-ville - où se trouvent la majorité des incidents.

                <h5><li> Features importance du modèle LGBMRegressor </li></h5>

                <br/>
                Voici les features importantes d'après le modèle :
                <br>
                """,unsafe_allow_html = True)
    st.image("figures\Feature_importance_LGBM.png")
    st.markdown("""
                
                Ce graphique nous permet de hiérarchiser les variables selon leur importance pour la détermination du temps d’attente des pompiers d’après notre modèle. La variable la plus importante est la distance entre le lieu de l’incident et la station depuis laquelle est déployé le véhicule (distFromStation). 
                <br/><br/>
                Nous voyons ensuite que l’heure d’appel (TimeOfCall) est également déterminante : en effet, on peut supposer que le trafic routier n’est pas le même en fonction de l’heure de la journée et que cela joue un rôle important. <br/>Le nombre de véhicules déployés (NumPumpsAttending) est ensuite représenté, on peut supposer que l’urgence de la situation impacte le nombre de véhicules et le temps de déploiement, ce qui pourrait lier ces deux variables.
                <br/><br/>
                Le fait que l’incident ait lieu dans un logement (Property_Dwelling) et non à l'extérieur, sur la route ou autre, semble également être un critère important. On peut effectivement penser qu’il est plus facile de se rendre dans une habitation qu’en extérieur sans repère précis, car le fait de connaître l'adresse réduira le temps nécessaire pour se rendre sur place.

                <h5><li> Package Skater </li></h5>
                <br/>
                Le package Skater nous permet également de faire émerger l'importance des features dans la détermination du modèle. Ci-dessous le top 10 des features les plus importants :
                <br>
                """,unsafe_allow_html = True)
                
    st.image("figures\Skater_top10.png", width=700)
    st.markdown("""
               
               Comme identifié précédemment avec les features_Importance du modèle LGBM retenu, la distance entre le lieu de l’incident et la station depuis laquelle le véhicule est déployé (distFromStation) est à nouveau de le feature qui contribue de très loin le plus au modèle. 
               <br/><br/>
               Nous voyons à nouveau ressortir le nombre de véhicules déployés (NumPumpsAttending) ainsi que l'heure d'appel (TimeOfCall) et certains types de propriétés (Property_NonResidential et Property_Outdoor).
               <br/><br/>
               Le package Skater nous permet par ailleurs de disposer d'informations plus précises sur l'impact de ces features dans la prédiction du modèle.
               <br/>   
               Ainsi, la distance (distFromStation) affiche une relation quasi linéaire avec le temps d’attente prédit. Ceci paraît logique puisque plus la station est loin de l’incident, plus le temps de trajet a des chances d'être important.
               <br/>
               """,unsafe_allow_html = True)
               
    st.image("figures\distFromStation.png", width=500)
    st.markdown("""
                
                S'agissant du nombre de véhicules déployés (NumPumpsAttending), on constate que plus le nombre de camions qui interviennent est important, plus le temps d’attente prédit est court. Cela pourrait s'expliquer par le fait que les incidents necéssitant l'intervention de plusieurs véhicules ont probablement un niveau de gravité plus important et nécessitent en conséquence une réactivité plus forte des secours.
                <br/>
                """,unsafe_allow_html = True)
                
    st.image("figures/NumPumpsAttending.png", width=500)
    st.markdown("""
                
                L'heure à laquelle est donnée l'alerte (TimeOfCall) est ensuite le troisième feature en termes d'importance. Le temps d’attente prédit est plus long durant les heures de nuit qu’en journée. On peut supposer qu'il y a moins d'équipes disponibles la nuit, ce qui allongerait les temps d'attente. 
                <br/>
                """,unsafe_allow_html = True)
                
    st.image("figures/TimeOfCall.png", width=500)
    st.markdown("""
                
                Lorsqu’on compare cette courbe avec celle du temps d'attente réel (ci-dessous), on se rend compte que le modèle prend bien en compte les disparités observées selon les tranches horaires. 
                <br/>
                """,unsafe_allow_html = True)
                
    st.image("figures\Temps_attente_par_heures_Xtrain.png", width=500)
    st.markdown("""
                
                Enfin, parmi les autres facteurs qui contribuent le plus au modèle, on retrouve différents features issus de la variable PropertyType (Outdoor, NonResidential, Roadvehicle). Si Skater identifie la nature du lieu d'intervention parmi les facteurs les plus contributifs au modèle, les graphiques ci-dessous ne montrent cependant pas de différence marquée au niveau de la prédiction. Nous pouvons en déduire que ces critères, pris indépendamment, ne jouent pas un rôle important, mais que leur importance est conditionnée par le fait d'être combinée avec un ou plusieurs autres features.
                <br/>
                """,unsafe_allow_html = True)
                
    st.image("figures\Property_Outdoor.png", width=500)
    st.image("figures\Property_NonResidential.png", width=500)
    st.image("figures\Property_RoadVehicle.png", width=500)
    st.markdown("""
                <h5><li> Package Shap </li></h5>
                <br/>
                Le package Shap nous propose également une autre lecture de l'importance des features pour le modèle. Celui-ci détermine le classement suivant des 10 features les plus importants :
                <br/>
                """,unsafe_allow_html = True)
    st.image("figures\Shap_feature_importance.png", width=700)
    st.markdown("""
                
                On retrouve à nouveau la distance entre la station et l’incident (distFromStation) comme étant le facteur principal de la prédiction. Nous trouvons ensuite le nombre de véhicules déployés (NumPumpsAttending), l’heure d’appel (TimeOfCall) et le fait que le lieu de l'incident soit non résidentiel (Property_NonResidential).
                <br/>   
                """,unsafe_allow_html = True)
    st.image("figures\Shap_value_feature.png", width=700)
    st.markdown("""
                  
                Sur ce second graphique, nous pouvons voir que plus la distance entre la station et l’incident est grande, plus elle influe positivement sur le temps d’attente. Et à l'inverse, une diminution de la distance tend à réduire le temps d’attente&#8239;: cela confirme la relation forte existante entre la distance séparant le lieu d'incident et la caserne avec le temps d'attente. 
                <br><br> 
                Concernant les deux variables suivantes, les différentes valeurs sont moins dissociées, il est donc plus difficile de tirer des conclusions. On peut tout de même dire que lorsque peu de camions sont déployés (NumPumpsAttending), le temps d'attente augmente légèrement.
                <br><br>
                Lorsque l'incident a lieu dans un lieu non résidentiel (Property_NonResidential), le temps d'attente diminue légèrement.
                <br><br> Les incidents en extérieur (Property_Outdoor) peuvent soit faire diminuer, soit faire augmenter le temps d'attente.
                <br><br>Les incidents ayant lieu le dimanche semble bénéficier d'un temps d'attente légèrement inférieur comme nous l'avons vu lors de l'exploration de données.
                <br><br>Comme nous l’avions identifié lors de l’analyse des données, le modèle a bien retranscrit le fait que lorsque l’incident est de type médical (IncidentType_MedicalIncident), le temps d’attente diminue grandement. C'est également le cas en moindre proportion pour les accidents de la route (IncidentType_RoadTrafficCollision).
                <br/>
                
                <h3>D - Conclusion sur la partie modélisation</h3>
                <br/>
                Notre modèle présente une précision moyenne (MAE) d'environ 1 minute (63 secondes). Ceci semble être raisonnable lorsqu'on pense aux applications qui peuvent en être faites. En effet, si un opérateur téléphonique des pompiers l'utilise pour annoncer un temps d'attente estimé aux victimes, une minute d'erreur semble être acceptable. D'autre part, le calcul de cette estimation par notre modèle sera suffisament rapide pour cette utilisation.
                <br><br>
                Grâce à cette étude d'interprétabilité, nous avons pu voir que notre modèle semble présenter une logique plutôt compréhensible. Les variables utilisées semblent logiquement influentes et correspondent globalement à ce que l'on avait pu identifier lors de l'analyse des données.
                <br/>
                """,unsafe_allow_html = True)