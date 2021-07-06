<h1>Projet London Fire Brigade CountDown</h1>
<br/><br/>
<p align="center"><img src=figures\LFB_illustration.png width=1000></p>
<br/><br/>
                                                 

<h3>Elora VABOIS, Marie LE COZ, Nicolas RAYMOND</h3>
<h3>DA Bootcamp Mai 2021</h3>
<br/><br/>


<h2>INTRODUCTION</h2>
<br/>

>   Dans le cadre de notre formation Data Analyst, un projet fil rouge nous est proposé nous donnant ainsi l'opportunité d'appliquer sur un cas concret et global les connaissances acquises tout au long de notre parcours. Le choix du sujet a été une étape cruciale pour notre équipe et nous avons finalement jeté notre dévolu sur un des projets proposés dans le catalogue fourni : « Prédiction du temps de réponse d’un véhicule de la Brigade des Pompiers de Londres ».
>  <br/><br/>
>  Au delà du sujet en lui-même, ce choix résulte en grande partie de la richesse des données exploitables, la variété des types d'analyse que nous avons rapidement identifiés (temporelles, géographiques, etc.) et des applications qu'elles entraîneraient. Nous avions également à coeur de travailler sur un sujet pour lequel nous percevions un challenge en Machine Learning. 
>  <br/><br/>
>  Ce projet vise à étudier l'ensemble des différents incidents auxquels ont répondu et pour lesquels sont intervenus les pompiers de la célèbre brigade de Londres entre 2009 et 2021, avec pour objectif final de pouvoir prédire le temps d'attente des pompiers pour les incidents ultérieurs. 

<br/><br/>
<h2>1 - ANALYSE DES DONNEES</h2>
<br/>

<h3>A - Introduction aux données</h3> 

> </br>Nous avons à notre disposition 3 jeux de données officielles afin d'analyser les contours du projet : 
> <ul><li>Un fichier regroupant tous les incidents entre 2009 et 2021 </li>
>   <li>Un fichier regroupant tous les déploiements sur ces incidents (matériels) sur la même période </li> 
>   <li>Un fichier récent de la liste des casernes de la brigade </li></ul>
>  <br/>
>   Les données fournies dans le fichier "Incident" sont indexées sur le numéro de l'incident. Pour chacun, de nombreuses informations nous sont fournies, à commencer par la date et l'heure de l'appel, plusieurs éléments relatifs au lieu de l'incident (adresse, type de lieu), la nature de l'incident, le temps d'attente entre l'appel et l'arrivée du premier véhicule, etc ...
>  <br/><br/>
>   Le fichier "Mobilisation" nous renseigne sur le déploiement des véhicules pour chaque incident, et contient le numéro de l'incident sur lequel ils sont envoyés, le type de véhicule, le temps de mobilisation avant le départ de ce véhicule, son temps de trajet, l'heure d'arrivée sur les lieux. Parfois, plusieurs véhicules peuvent être déployés sur le même incident. Dans ce cas de figure, nous disposons d'une variable indiquant l'ordre d'appel de ces véhicules. Enfin, pour une partie des données, la latitude et la longitude du lieu de l'incident sont renseignées.
>  <br/><br/>
>   La liste des casernes ayant évolué sur la période que couvre notre dataset, la London Fire Brigade nous a aimablement fourni sur demande la liste exhaustive des casernes en activité à ce jour sous leur giron ainsi que les adresses correspondantes.
>  <br/><br/>
>   Le but de notre étude est de pouvoir mettre en place un modèle prédictif qui indiquera le temps d'attente entre un appel et l'arrivée des secours sur place en fonction de plusieurs critères à déterminer. 
<br/>


<br/>
<h3>B - Nettoyage des données</h3> 

>   Dans un premier temps, un nettoyage et une réduction du jeu de données s'avère indispensable afin de :
> <ul><li>Ne conserver que les données utiles et pertinentes à notre étude</li>
>      <li> Réduire le volume de données très conséquent</li></ul>
>  <br/>
>   Nous avons donc réduit et nettoyé au maximum notre dataset pour en faciliter l'étude. Notre action majeure a été d'éliminer toutes les données antérieures à 2014 en raison de la fermeture d'une dizaine de stations à cette date, cela induisant inévitablement un problème de comparabilité de plusieurs indicateurs.<br/>
>  Nous avons également éliminé nombre de variables inutiles à notre étude et avons reconstitué les données manquantes, notamment les coordonnées géographiques des incidents et des stations. <br/>
>  Enfin, nous avons supprimé quelques incidents ayant peu de sens pour notre étude, comme les incidents de type "Water Provision" pour lequels nous avions très peu d'observations.


<br/>
<h3>C - Analyse des données</h3> 

<h4>i - Analyse des incidents en fonction des variables temporelles </h4> 
  
>   Une première approche simple nous permet de vérifier visuellement si les différents facteurs temporels (mois, jour de la semaine, heure de la journée) ont une influence sur le nombre d'incidents :
>   
>   <p align="center"><img src=figures\Moyenne_par_mois.png width=600></p>
>   <p align="center"><img src=figures\Moyenne_par_jour.png width=600></p>
>   <p align="center"><img src=figures\Moyenne_par_heures.png width=600></p>
>   
>   Nous pouvons remarquer que le nombre moyen d'incidents varie plus ou moins fortement selon ces facteurs :
>   <ul><li> Un nombre moyen d'incidents plus important sur les mois estivaux (de mai à septembre) par rapport au reste de l'année, avec un pic sur le mois de juillet.</li>
>   <li> Une relation que l'on retrouve en moindre mesure en fonction des jours de la semaine : une densité d'incidents un peu plus forte les vendredi et surtout samedi, mais comparable sur les autres jours.</li>
>   <li> Et enfin, assez logiquement, une forte influence de l'horaire sur le nombre moyen d'incidents : une densité bien plus forte sur les heures de la journée avec un pic en fin d'après-midi/début de soirée.</li></ul>
>   
>   
>   Nous avons ensuite réalisé des tests statistiques afin de vérifier que ces constats se vérifient. Nos 3 tests ANOVA concernant l'influence de nos 3 variables temporelles sur le nombre d'incidents moyen, nous indique que l'hypothèse selon laquelle les variables sont indépendantes est rejetée avec des p values extrêmement proches de 0. Nos 3 variables temporelles ont donc un effet statistique significatif sur le nombre d'incidents moyen.
>   <br/>
>  |          |    df |         sum_sq |   mean_sq |        F |        PR(>F) |
>  |:---------|------:|---------------:|----------:|---------:|--------------:|
>  | Mois     |     1 | 3026.22        |  3026.22  |  25.8373 |   3.72452e-07 |
>  | Residual | 65558 |    7.67853e+06 |   117.126 | nan      | nan           |
>   
>  |          |     df |     sum_sq |   mean_sq |       F |        PR(>F) |
>  |:---------|-------:|-----------:|----------:|--------:|--------------:|
>  | jours    |      1 |    193.354 | 193.354   |  53.912 |   2.10278e-13 |
>  | Residual | 259735 | 931530     |   3.58646 | nan     | nan           |
>   
>  |          |     df |    sum_sq |    mean_sq |       F |        PR(>F) |
>  |:---------|-------:|----------:|-----------:|--------:|--------------:|
>  | heures   |      1 |    25.594 | 25.594     | 383.153 |   3.20373e-85 |
>  | Residual | 164639 | 10997.6   |  0.0667985 | nan     | nan           |
>  
>  <br/>
>   Nous nous sommes également intéressés à savoir si ces mêmes variables pouvaient avoir une incidence sur le temps d'attente, c'est-à-dire le temps passé entre l'appel des secours et leur arrivée sur place.
>   
>  <br/>
>   <p align="center"><img src=figures\Temps_attente_par_mois.png width=600></p>
>   <p align="center"><img src=figures\Temps_attente_par_jour.png width=600></p>
>   <p align="center"><img src=figures\Temps_attente_par_heures.png width=600></p>
>  <br/><br/>
>   Les variations sur le temps d'attente sont moins flagrantes, mais s'expliquent en grande partie par le fait que cette variable n'a pas une grande amplitude de manière générale.<br/><br/>
>  Néanmoins, certains enseignements se recoupent avec la distribution des incidents décrite plus haut :
>   <ul><li> Le temps d'attente est sensiblement plus important sur les mois estivaux, tout comme l'était la densité des incidents.</li>
>   <li> En revanche, nous n'observons pas de relation clairement visible entre le temps d'attente et le jour de la semaine ou l'heure de la journée.</li></ul>
>  <br/><br/>
>   Nous avons également vérifié à l'aide de tests ANOVA si ces variables temporelles influencent significativement le temps d'attente. 
>   <br/>
>   |          |    df |      sum_sq |        mean_sq |        F |        PR(>F) |
>  |:---------|------:|------------:|---------------:|---------:|--------------:|
>  | Mois     |     1 | 1.2569e+06  |     1.2569e+06 |  18.1985 |   1.99319e-05 |
>  | Residual | 65558 | 4.52786e+09 | 69066.4        | nan      | nan           |
> 
>   |          |     df |         sum_sq |   mean_sq |           F |    PR(>F) |
>  |:---------|-------:|---------------:|----------:|------------:|----------:|
>  | jours    |      1 | 2202.49        |   2202.49 |   0.0636286 |   0.80085 |
>  | Residual | 259735 |    8.99067e+09 |  34614.8  | nan         | nan       |
>   
>   |          |     df |      sum_sq |         mean_sq |       F |        PR(>F) |
>  |:---------|-------:|------------:|----------------:|--------:|--------------:|
>  | heures   |      1 | 3.72604e+06 |     3.72604e+06 | 211.216 |   7.98411e-48 |
>  | Residual | 164639 | 2.90438e+09 | 17640.9         | nan     | nan           |
>   
>  <br/>
>  Pour ces 3 tests, nous avons posé l'hypothèse que le temps d'attente est indépendant du mois, du jour de la semaine et de l'heure de l'incident.
>  Les p values des tests liés au mois et à l'heure de l'incident sont extrêment proches de 0, nous pouvons donc noter un effet statistique significatif de ces variables sur le temps d'attente. La p value du test lié au jour de la semaine est d'environ 80 %, indiquant donc cette variable n'a pas d'effet statistique significatif sur le temps d'attente des secours.

<br/>
<h4>ii - Analyse en fonction du type d'incident </h4> 

>   Au-delà des facteurs temporels, nous nous sommes également demandé s'il pouvait exister un lien entre le temps d'attente et la nature de l'incident. En effet, selon le type d'incident, les besoins peuvent être différents en termes de type de véhicule à déployer, ce qui peut influencer le temps de déploiement en fonction de la disponibilité du véhicule par exemple.
>  <br/><br/>
>  Regardons tout d'abord la répartition des types d'incidents traités par la London Fire Brigade depuis 2014 :
>  <br/><br/>
>   <p align="center"><img src=figures\Moyenne_par_type.png width=600></p>
>  <br/><br/>
>   On remarque que la grande majorité des sources d'intervention sont liées aux Alarmes Automatiques d'Incendie. Ensuite, et dans une moindre mesure, on retrouve comme autres raisons principales : les incendies, les opérations d'entrée-sortie de personnes, les innondations puis les accidents de la route. D'après notre test ANOVA, le type d'incident a un lien significatif avec le nombre d'incidents (p value nulle).
>  <br/>
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 9.44883e+07 |     3.77953e+06 | 238.183 |        0 |
>  | Residual | 17218 | 2.73218e+08 | 15868.1         | nan     |      nan |
>  
>  <br/><br/>
>  Ici encore, nous vérifions l'incidence sur le temps d'attente visuellement puis statistiquement.
>  <br/><br/>
>   <p align="center"><img src=figures\Temps_attente_par_type.png width=800></p>
>  <br/><br/>
>   Le temps d'attente évolue donc du simple au double selon le type d'incident. La LFB met deux fois plus de temps pour se rendre sur un incendie que pour porter secours lors d'une noyade.
>  Cette influence de la nature de l'intervention sur le temps d'attente est par ailleurs confirmée par le test ANOVA qui indique un lien significatif entre les deux variables (p value nulle).
>  <br/>
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 1.34913e+08 |     5.39652e+06 |  69.132 |        0 |
>  | Residual | 17218 | 1.34406e+09 | 78061.1         | nan     |      nan |
>
<br/>
<h4>iii - Analyse en fonction de la localisation de l'incident </h4> 

>   Dans un premier temps, nous avons souhaité visualiser l'ensemble des incidents en fonction de leur localisation, en colorant chaque point, représentant un incident, en fonction de la station qui a répondu en premier sur l'intervention.
>  <br/><br/>
>  Ceci nous permet de voir la répartition des stations et leur rayon d'action :
>  <br/><br/>
>   <p align="center"><img src=figures\Carte_incident_station.png></p>
>  <br/><br/>
>   Le test ANOVA évaluant l'indépendance de la station de déploiement du temps d'attente nous montre un lien significatif entre ces variables (p value nulle). On peut donc supposer que : soit certaines stations sont intrinsèquement plus performantes que d'autres (grâce à des équipes plus expérimentées par exemple), soit c'est l'emplacement des stations qui va agir indirectement sur le temps d'attente.
>   <br/>
>  |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>  | DeployedFromStation_Code |    101 | 5.69136e+08 |     5.63501e+06 | 315.144 |        0 |
>  | Residual                 | 683719 | 1.22254e+10 | 17880.7         | nan     |      nan |
>   
>  <br/>
>  Nous avons également prêté attention à la densité des incidents répartis sur l'ensemble de la ville (ici en 2020) : 
>
>  voir figure CarteDeDensiteBokeh.html
>
>   Comme nous nous y attendions, les incidents sont plus nombreux au centre-ville qu'en périphérie, tout comme le sont les stations.
> <br/><br/>
> Le test ANOVA entre le nombre d'incidents et le district (PostCode_district) du lieu d'incident indique un lien significatif entre ces variables (p value nulle).
>   <br/>
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
> |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
> | District |    328.0 | 3.343984e+08 |     1.019507e+06 | 22.724574 |        0 |
> | Residual                 | 134211.0 | 6.021195e+09 | 4.486365e+04         | nan     |      nan ||
>
>   <br/>
> Nous avons ensuite souhaité voir la répartition géographique des incidents sur la carte de Londres, en filtrant les données par année et en colorant ces points par rapport aux temps d'attente (les points verts représentant les temps d'attente les plus faibles, les points rouges les plus longs). Nous avons inséré les stations sur cette carte (triangles noirs) afin de visualiser l'impact de la proximité avec une station sur le délai d'intervention.
>
>  voir figure TempsDAttenteParAn.html
>
>   Cette dernière visualisation permet de bien identifier les zones en fonction de la réactivité des secours. On observe que plus l'incident est éloigné d'une station, plus le temps d'attente tend à augmenter. 
>   <br/><br/>
>   Le test ANOVA qui concerne le temps d'attente et le district (PostCode_district) du lieu d'incident indique un lien significatif entre ces variables (p value nulle).
>   <br/>
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>   |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>   | District |    328.0 | 9.468728e+05 |     2886.807444 | 88.86169 |        0 |
>   | Residual                 | 134211.0 | 4.360049e+06 | 32.486524         | nan     |      nan ||
>  
>   <br/>
>   De plus, le test de Pearson liant la distance entre le lieu d'incident et la station de déploiement avec le temps d'attente nous indique que ces variables ont un lien significatif (p value nulle) et que leur corrélation est relativement importante (coefficient de Pearson : 51.5%).
>   <br/>
>   |                          |     résultat test |
>   |:-------------------------|-------:|
>   | pearson_coeff |    0.515065 | 
>   | p-value                 | 0.000000 ||


<h4>iv - Autres tests statistiques réalisés </h4> 

>   Nous avons également étudié la corrélation entre le type de retard éventuel (DelayCode_Description) et le temps d'attente et notre test ANOVA indique un lien significatif entre ces variables (p value nulle). Cependant, nous ne pourrons pas conserver cette variable pour la modélisation car elle n'est connu qu'à posteriori : elle ne peut donc pas servir à la prédiction.
>   <br/>
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>   |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>   | DelayCode_Description |    9.0 | 3.273134e+09 |     3.636815e+08 | 26118.986271 |        0 |
>   | Residual                 | 683811.0 | 9.521404e+09 | 1.392403e+04         | nan     |      nan |


<br/>
<h3>D - Conclusion sur l'analyse des données</h3> 

>   Cette première étape d'analyse des données nous confirme bien que les indicateurs étudiés seront indispensables dans le cadre de la modélisation du temps d'intervention de la LFB. 
<h2>2 - MODELISATION</h2>
<br/>

<h3>A - Preprocessing des données</h3> 

>   Une fois l’analyse du dataset réalisée, nous avons procédé au nettoyage et au preprocessing des données, afin d’assurer le bon déroulement de la phase de modélisation.
>   Nous avons donc déterminé : </br><ul><li>Les variables explicatives à supprimer : celles n’ayant pas influence sur notre variable cible ou étant redondantes avec d’autres variables ainsi que celles n'étant connues qu'à posteriori. </li></br><li>Les variables explicatives à convertir : dichotomisation des variables catégorielles, conversion de la variable ‘TimeOfCall’ en variable numérique (float). </li> </br><li>Les variables explicatives à créer : fusion des 2 variables liées ‘SpecialServiceType’ et ‘StopCodeDescription’ en une variable unique ‘IncidentTypeGlobal’, puis, une fois les coordonnées géographiques des casernes récupérées, création d’une variable ‘distFromStation’ indiquant la distance entre le lieu de l’intervention et la caserne étant intervenue et suppression des coordonnées (car nous avons déjà les variables Borough - quartier - et DeployedFromStation - station de déploiement - qui donnent des indications sur l’emplacement de l’incident). </li></ul>
>   </br>
>   La majeure partie de nos features étant des variables catégorielles contenant de nombreuses modalités pour la plupart, la dichotomisation a ainsi généré un dataset final avant modélisation de dimension conséquente avec 549 colonnes pour environ 680 000 lignes.<br/><br/>
>   Nous avons ensuite mis en place un Train Test split en nous assurant que les données les plus récentes soient conservées pour le test.<br/><br/>
>   Enfin, nous avons procédé à l’étape de scaling afin de générer un dataset normalisé pour les modèles qui le nécessitent.

<br/>
<h3>B - Itérations modélisation</h3> 

<h4> i - Première itération </h4> 

<h5><li> Modèles entraînés </li></h5> 

>   Les modèles qu'on a instanciés dans un premier temps sont les modèles de régression linéaires classiques (LinearRegression seul puis avec SelectKBest et SelectFromModel, ElasticNetCV), HistGradientBoosting, DecisionTree, ainsi que Lasso et Ridge. Nous avons décidé de ne pas tester KNN qui n'est pas adapté aux gros datasets de par son mode de calcul.
>   <br>
>   Nous avons recherché les hyper-paramètres optimaux à l'aide d'une GridSearch pour les modèles qui le permettaient.

<h5><li> Contraintes rencontrées </li></h5> 

>   Nous avons rencontré de nombreuses difficultés techniques liées à la taille du dataset (memory error, interruption kernels et temps de calculs extrêmement importants… ).
>   Nous avons donc dû nous limiter à un dataset contenant les 250 000 dernières lignes (les plus récentes).

<h5><li> Résultats obtenus </li></h5> 

>   |    | model                               |   R² train |      R² test |   mse train |        mse test |   mae train |         mae test | paramètres retenus                                                                                                                                                          |
>   |---:|:------------------------------------|-----------:|-------------:|------------:|----------------:|------------:|-----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
>   |  0 | LinearRegression                    |   0.324491 | -4.21421e+12 |     11500.1 |     6.37987e+16 |     70.1761 | 922374           |                                                                                                                                                                             |
>   |  1 | SelectKBest régression linéaire     |   0.299405 |  0.338849    |     11927.2 | 10009.1         |     72.2332 |     68.5351      | f_regression,k=100,nb_cols=100                                                                                                                                              |
>   |  2 | SelectFromModel régression linéaire |   0.068366 | -2.02101e+15 |     15860.5 |     3.05961e+19 |     89.8018 |      2.01978e+07 | nb_cols=111                                                                                                                                                                 |
>   |  3 | ElasticNetCV                        |   0.323789 |  0.355323    |     11512.1 |  9759.74        |     70.2753 |     67.4525      | alpha :  0.05 parmi alphas=(0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0), l1_ratio :  0.75 parmi l1_ratio=(0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.99)    |
>   |  4 | LassoCV                             |   0.32375  |  0.356218    |     11512.7 |  9746.19        |     70.1925 |     67.3646      | alpha=0.066393                                                                                                                                                              |
>   |  5 | RidgeCV                             |   0.324491 |  0.35625     |     11500.1 |  9745.71        |     70.1762 |     67.3651      | alpha=1 parmi alphas= (0.0001,0.0005,0.001, 0.005,0.01, 0.05,0.1,0.5,1)                                                                                                     |
>   |  6 | DecisionTree                        |   0.344382 |  0.347896    |     11161.5 |  9872.18        |     70.5671 |     67.6965      | max_depth=7 parmi [2, 3, 4, 5, 6, 7, 8], criterion=friedman_mse                                                                                                             |
>   |  7 | DecisionTree                        |   0.344382 |  0.347034    |     11161.5 |  9885.23        |     70.5671 |     67.7137      | max_depth=7 parmi [2, 3, 4, 5, 6, 7, 8], criterion=mse                                                                                                                      |
>   |  8 | HistGradientBoosting                |   0.391331 |  0.389738    |     10362.2 |  9238.74        |     66.6608 |     64.8576      | min_samples_leaf = 500, loss=least_squares parmi [least_squares,least_absolute_deviation], max_iter=250 parmi [50,70,100,120,150,170,200,250], max_depth=8 parmi range(3,9) |
> 
> Le modèle le plus performant est le modèle Hist Gradient Boosting quelque soit le critère de performance observé : il présente les R² les plus élevés ainsi que les MSE et MAE les plus faibles.
>   <br>
>   Pour cette première itération, nous obtenons pour l’ensemble de nos tests, hormis pour le HistGradientBoosting :
> <ul><li> Des scores R² peu concluants</li>
> <li>Des MAE d'environ une minute et 10 secondes pour la plupart des modèles.</li></ul>
>   <br>
>   Suite à cette itération, nous avons essayé de renouveler l'expérience avec ces modèles sur le dataset complet.

<br>
<h4> ii - Deuxième itération </h4> 

<h5><li> Objectifs </li></h5> 

>   Nous avons créé un script regroupant tous nos modèles et produisant un fichier “Resultat.csv” de manière à pouvoir tester nos modèles sur le dataset complet (très lourd) sur une machine plus puissante. Nous avons également ajouté des hyper-paramètres que nous n’avions pas pu tester sur nos machines (par exemple des criterions pour les DecisionTree).

<h5><li> Modèles entraînés et ajustement réalisés </li></h5> 

>   Nous avons utilisé les mêmes modèles que précédemment et y avons ajouté les modèles GradientBoosting, HistGradientBoosting, LassoCV et Ridge sur le dataset pré-formaté grâce au transformateur PolynomialFeatures. Ce dernier permet de créer de nouvelles variables représentant l'interaction des variables initiales (si on a un dataset avec les variables a et b, PolynomialFeatures renverra un nouveau dataset avec les variables 1, a, b et ab avec les paramètres degree=2 et interaction_only=True).


<h5><li> Contraintes rencontrées </li></h5> 

>   Le modèle DecisionTree a bloqué le script qui ne s’était toujours pas arrêté après plus de 24 heures.

<h5><li> Résultats obtenus </li></h5> 

>   Nous n’avons pu recueillir aucun résultat au cours de cette tentative.

<br/>
<h4> iii - Troisième itération </h4> 

<h5><li> Objectifs </li></h5>

>   Suite à notre échec précédent, nous avons repris notre dataset réduit avec les 250 000 mobilisations les plus récentes. Nous avons essayé d'améliorer les premières performances obtenues grâce au modèle HistGradientBoosting.
>   <br/><br/>
>   Nous avons décidé d’optimiser la recherche d’hyper-paramètres à l’aide du package Optuna. Optuna a le même objectif que la GridSearchCV&#8239;: il permet de trouver la combinaison d'hyper-paramètres la plus performante. Cependant, il n'opère pas de la même manière. Tandis que la GridSearch évalue toutes les combinaisons d'hyper-paramètres existantes parmi les valeurs qui lui ont été fournies, ce sont des plages de valeurs qui sont fournies à Optuna. Cela lui permet d'explorer l'ensemble de l'espace sans avoir à tester toutes les combinaisons pour un paramètre ayant peu d'influence par exemple.
>   <br>Nous avons également remplacé HistGradientBoosting par LightGBM qui est optimisé en temps de calcul.
>   Au cours des différentes itérations, il a fallu déterminer si nous étions en régime de sur ou sous-apprentissage et le combattre.

<h5><li> Modèles entraînés et ajustement réalisés </li></h5>

>   Nous avons entraîné le modèle LGBMRegressor avec le package Optuna. Nous avons procédé en plusieurs itérations pour trouver quels hyper-paramètres tester et sur quelles plages.

<h5><li> Résultats obtenus au cours des différentes étapes </li></h5>

<u><em>Etape 1</em></u>
>   3 hyper-paramètres testés avec 200 trials :
>   <br/>
>   ```py
learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
max_depth = trial.suggest_int('max_depth', 2, 50)
n_estimators = trial.suggest_int('n_estimators', 20,500)
>   ```
>   Best trial :
<br/>
>   ```py
learning_rate = 0.1012069771826192
max_depth = 40
n_estimators = 488
>   ```
>   <br/>  
>   | model                                                                         |   R² train |   R² test |   mse train |   mse test |   mae train |   mae test |
>   |:------------------------------------------------------------------------------|-----------:|----------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor1 |   0.454652 |  0.409216 |     9284.22 |    8943.85 |     62.8125 |    63.2457 |
>   
>   Les performances sont plutôt satisfaisantes, la MAE s'est rapproché d'une minute.
>   <br/>
>   Nous sommes en sur-apprentissage léger. 
>   Pour l’étape 2, nous essaierons d’ajouter d’autres hyper-paramètres afin de tenter de le réduire.

<u><em>Etape 2</em></u>
>   6 hyper-paramètres testés avec 200 trials :
>   <br/>
>   ```py
learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
max_depth = trial.suggest_int('max_depth', 2, 80)
n_estimators = trial.suggest_int('n_estimators', 20,800)
reg_alpha = trial.suggest_loguniform('reg_alpha', 1e-5,10)
reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-5,10)
subsample_for_bin = trial.suggest_int('subsample_for_bin', 200000, 500000)
>   ```
>   Best trial :
<br/>
>   ```py
learning_rate = 0.0735978242412042
max_depth = 76
n_estimators = 737
reg_alpha = 0.000987737786289064
reg_lambda = 3.6393223694815996e-05
subsample_for_bin = 226071
>   ```
>   <br/> 
>   | model                                                                            |   R² train |   R² test |   mse train |   mse test |   mae train |   mae test |
>   |:---------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor2    |      0.459334 |     0.410594 |      9204.5 |       8923 |      62.532 |    63.1363 ||
>   
>   Les performances ont légèrement augmenté. En examinant les essais, le paramètre subsample_for_bin ne semble pas avoir beaucoup d’influence, c’est pourquoi nous avons décidé de le laisser à sa valeur par défaut et de tester d’autres paramètres connus pour agir contre le sur-apprentissage. Nous allons également réduire les plages de max_depth et n_estimators pour essayer de limiter ce sur-apprentissage.

<u><em>Etape 3</em></u>
>   8 hyper-paramètres testés avec 200 trials :
>   <br/>
>   ```py
learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
max_depth = trial.suggest_int('max_depth', 2, 40)
n_estimators = trial.suggest_int('n_estimators', 20,500)
reg_alpha = trial.suggest_loguniform('reg_alpha', 1e-5,10)
reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-5,10)
num_leaves = trial.suggest_int('num_leaves', 10, 50)
min_split_gain = trial.suggest_uniform('min_split_gain', 0,1)
min_child_samples = trial.suggest_int('min_child_samples', 5, 50)
>   ```
>   Best trial :
<br/>
>   ```py
learning_rate = 0.08611376087571489
max_depth = 28
n_estimators = 467
reg_alpha = 0.007369798680853325
reg_lambda = 0.0002296807544488281
num_leaves = 47
min_split_gain = 0.5709551773016567
min_child_samples = 32
>   ```
>   <br/>
>   |model                                                                           |   R² train |   R² test |   mse train |   mse test |   mae train |   mae test |
>   |:--------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor3    |      0.463816 |     0.411167 |     9128.22 |    8914.33 |     62.1916 |     63.052 ||
>   
>   Le sur-apprentissage a légèrement augmenté, nous allons essayer de le réduire en diminuant les plages de test des hyper-paramètres.

<u><em>Etape 4</em></u>
>   8 hyper-paramètres testés avec 400 trials :
<br/>
>   ```py 
learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
max_depth = trial.suggest_int('max_depth', 2, 20)
n_estimators = trial.suggest_int('n_estimators', 20,300)
reg_alpha = trial.suggest_loguniform('reg_alpha', 1e-5,10)
reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-5,10)
num_leaves = trial.suggest_int('num_leaves', 10, 35)
min_split_gain = trial.suggest_uniform('min_split_gain', 0,1)
min_child_samples = trial.suggest_int('min_child_samples', 40, 200)
>   ```
>   Best trial :
>   <br/>
>   ```py
learning_rate = 0.1512198354101122
max_depth = 17
n_estimators = 295
reg_alpha = 0.0005383830447172724
reg_lambda = 0.00011538095876075694
num_leaves = 32
min_split_gain = 0.473924522550586
min_child_samples = 43
>   ```
>   <br/>
>   |model                                                                        |   R² train |   R² test |   mse train |   mse test |   mae train |   mae test |
>   |:-----------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor4 |      0.445746 |     0.410001 |     9435.83 |    8931.97 |     63.1968 |    63.1481 ||
>   
>   Lors de cet essai, le sur-apprentissage est moins important qu’auparavant et la performance est quasiment identique (à peine moindre), c’est pourquoi cela nous paraît être un compromis acceptable.


<h3>C - Choix et interprétabilité du modèle</h3>


<h4> i - Modèle retenu  </h4> 

>   | model                                                                            |   R² train |   R² test |   mse train |   mse test |   mae train |   mae test |
>   |:---------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   | LGBMRegressor1    |      0.454652 |     0.409216 |     9284.22 |    8943.85 |     62.8125 |    63.2457 ||
>   | LGBMRegressor2   |      0.459334 |     0.410594 |     9204.50  |    8923.00    |     62.5320  |    63.1363 ||
>   | LGBMRegressor3    |      0.463816 |     0.411167 |     9128.22 |    8914.33 |     62.1916 |    63.0520  ||
>   | LGBMRegressor4     |      0.445746 |     0.410001 |     9435.83 |    8931.97 |     63.1968 |    63.1481 ||            |
>   
>   Finalement, nous avons décidé de retenir le modèle LGBMRegressor4 qui produit de bons résultats tout en exigeant un temps de calcul très raisonnable (non seulement par rapport aux modèles de la première itération puisque LightGBM est optimisé, mais également par rapport aux 3 premiers LGBMRegressor car c'est celui qui présente le n_estimators le plus faible). On pourra lui reprocher d’être peu interprétable mais nous allons essayer d’y remédier dans la partie suivante grâce aux packages Skater et Shap.

<br/>
<h4> ii - Interprétabilité du modèle  </h4> 

<h5><li> Visualisation géographique de l'erreur </li></h5>

>   Avant d'utiliser les packages d'interprétabilité, nous allons visualiser géographiquement l'erreur sur le jeu de données test, de manière à repérer d'éventuelles anomalies ou bien à confirmer la performance du modèle.


