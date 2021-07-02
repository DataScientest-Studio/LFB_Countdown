<p align="center"><h1>Projet London Fire Brigade CountDown</h1></p>
<br/><br/>
<p align="center"><img src=figures\LFB_illustration.png width=1000></p>
<br/><br/>
                                                 

<p align="center"><h3>Elora VABOIS, Marie LE COZ, Nicolas RAYMOND</h3></p>
<p align="center"><h3>DA Bootcamp Mai 2021</h3></p>
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
>   <p align="center">
>   |          |    df |         sum_sq |   mean_sq |        F |        PR(>F) |
>  |:---------|------:|---------------:|----------:|---------:|--------------:|
>  | Mois     |     1 | 3026.22        |  3026.22  |  25.8373 |   3.72452e-07 |
>  | Residual | 65558 |    7.67853e+06 |   117.126 | nan      | nan           |
>   
>   |          |     df |     sum_sq |   mean_sq |       F |        PR(>F) |
>  |:---------|-------:|-----------:|----------:|--------:|--------------:|
>  | jours    |      1 |    193.354 | 193.354   |  53.912 |   2.10278e-13 |
>  | Residual | 259735 | 931530     |   3.58646 | nan     | nan           |
>   
>   |          |     df |    sum_sq |    mean_sq |       F |        PR(>F) |
>  |:---------|-------:|----------:|-----------:|--------:|--------------:|
>  | heures   |      1 |    25.594 | 25.594     | 383.153 |   3.20373e-85 |
>  | Residual | 164639 | 10997.6   |  0.0667985 | nan     | nan           |
>  </p>
>  <br/><br/>
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
>   <p align="center">
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
>   </p>
>  <br/><br/>
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
>  <p align="center">
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 9.44883e+07 |     3.77953e+06 | 238.183 |        0 |
>  | Residual | 17218 | 2.73218e+08 | 15868.1         | nan     |      nan |
>  </p>
>  <br/><br/>
>  Ici encore, nous vérifions l'incidence sur le temps d'attente visuellement puis statistiquement.
>  <br/><br/>
>   <p align="center"><img src=figures\Temps_attente_par_type.png width=800></p>
>  <br/><br/>
>   Le temps d'attente évolue donc du simple au double selon le type d'incident. La LFB met deux fois plus de temps pour se rendre sur un incendie que pour porter secours lors d'une noyade.
>  Cette influence de la nature de l'intervention sur le temps d'attente est par ailleurs confirmée par le test ANOVA qui indique un lien significatif entre les deux variables (p value nulle).
>  <p align="center">
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 1.34913e+08 |     5.39652e+06 |  69.132 |        0 |
>  | Residual | 17218 | 1.34406e+09 | 78061.1         | nan     |      nan |
</p>
<br/>
<h4>iii - Analyse en fonction de la localisation de l'incident </h4> 

>   Dans un premier temps, nous avons souhaité visualiser l'ensemble des incidents en fonction de leur localisation, en colorant chaque point, représentant un incident, en fonction de la station qui a répondu en premier sur l'intervention.
>  <br/><br/>
>  Ceci nous permet de voir la répartition des stations et leur rayon d'action :
>  <br/><br/>
>   <p align="center"><img src=figures\Carte_incident_station.png></p>
>  <br/><br/>
>   Le test ANOVA évaluant l'indépendance de la station de déploiement du temps d'attente nous montre un lien significatif entre ces variables (p value nulle). On peut donc supposer que : soit certaines stations sont intrinsèquement plus performantes que d'autres (grâce à des équipes plus expérimentées par exemple), soit c'est l'emplacement des stations qui va agir indirectement sur le temps d'attente.
>   <p align="center">
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>  | DeployedFromStation_Code |    101 | 5.69136e+08 |     5.63501e+06 | 315.144 |        0 |
>  | Residual                 | 683719 | 1.22254e+10 | 17880.7         | nan     |      nan |
>   </p>
>  <br/>
>  Nous avons également prêté attention à la densité des incidents répartis sur l'ensemble de la ville (ici en 2020) : 
