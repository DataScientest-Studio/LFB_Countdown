<p align="center"><h1>Projet London Fire Brigade CountDown</h1></p>
<br/><br/>
<p align="center"><img src=figures\LFB_illustration.png width=1000></p>
<br/><br/>
                                                 

<p align="center"><h3>Elora VABOIS, Marie LE COZ, Nicolas RAYMOND</h3></p>
<p align="center"><h3>DA Bootcamp Mai 2021</h3></p>
<br/><br/>


<h2>INTRODUCTION</h2>
<br/>

>   Dans le cadre de notre formation Data Analyst, un projet fil rouge nous est propos� nous donnant ainsi l'opportunit� d'appliquer sur un cas concret et global les connaissances acquises tout au long de notre parcours. Le choix du sujet a �t� une �tape cruciale pour notre �quipe et nous avons finalement jet� notre d�volu sur un des projets propos�s dans le catalogue fourni : � Pr�diction du temps de r�ponse d�un v�hicule de la Brigade des Pompiers de Londres �.
>  <br/><br/>
>  Au del� du sujet en lui-m�me, ce choix r�sulte en grande partie de la richesse des donn�es exploitables, la vari�t� des types d'analyse que nous avons rapidement identifi�s (temporelles, g�ographiques, etc.) et des applications qu'elles entra�neraient. Nous avions �galement � coeur de travailler sur un sujet pour lequel nous percevions un challenge en Machine Learning. 
>  <br/><br/>
>  Ce projet vise � �tudier l'ensemble des diff�rents incidents auxquels ont r�pondu et pour lesquels sont intervenus les pompiers de la c�l�bre brigade de Londres entre 2009 et 2021, avec pour objectif final de pouvoir pr�dire le temps d'attente des pompiers pour les incidents ult�rieurs. 

<br/><br/>
<h2>1 - ANALYSE DES DONNEES</h2>
<br/>

<h3>A - Introduction aux donn�es</h3> 

> </br>Nous avons � notre disposition 3 jeux de donn�es officielles afin d'analyser les contours du projet : 
> <ul><li>Un fichier regroupant tous les incidents entre 2009 et 2021 </li>
>   <li>Un fichier regroupant tous les d�ploiements sur ces incidents (mat�riels) sur la m�me p�riode </li> 
>   <li>Un fichier r�cent de la liste des casernes de la brigade </li></ul>
>  <br/>
>   Les donn�es fournies dans le fichier "Incident" sont index�es sur le num�ro de l'incident. Pour chacun, de nombreuses informations nous sont fournies, � commencer par la date et l'heure de l'appel, plusieurs �l�ments relatifs au lieu de l'incident (adresse, type de lieu), la nature de l'incident, le temps d'attente entre l'appel et l'arriv�e du premier v�hicule, etc ...
>  <br/><br/>
>   Le fichier "Mobilisation" nous renseigne sur le d�ploiement des v�hicules pour chaque incident, et contient le num�ro de l'incident sur lequel ils sont envoy�s, le type de v�hicule, le temps de mobilisation avant le d�part de ce v�hicule, son temps de trajet, l'heure d'arriv�e sur les lieux. Parfois, plusieurs v�hicules peuvent �tre d�ploy�s sur le m�me incident. Dans ce cas de figure, nous disposons d'une variable indiquant l'ordre d'appel de ces v�hicules. Enfin, pour une partie des donn�es, la latitude et la longitude du lieu de l'incident sont renseign�es.
>  <br/><br/>
>   La liste des casernes ayant �volu� sur la p�riode que couvre notre dataset, la London Fire Brigade nous a aimablement fourni sur demande la liste exhaustive des casernes en activit� � ce jour sous leur giron ainsi que les adresses correspondantes.
>  <br/><br/>
>   Le but de notre �tude est de pouvoir mettre en place un mod�le pr�dictif qui indiquera le temps d'attente entre un appel et l'arriv�e des secours sur place en fonction de plusieurs crit�res � d�terminer. 
<br/>


<br/>
<h3>B - Nettoyage des donn�es</h3> 

>   Dans un premier temps, un nettoyage et une r�duction du jeu de donn�es s'av�re indispensable afin de :
> <ul><li>Ne conserver que les donn�es utiles et pertinentes � notre �tude</li>
>      <li> R�duire le volume de donn�es tr�s cons�quent</li></ul>
>  <br/>
>   Nous avons donc r�duit et nettoy� au maximum notre dataset pour en faciliter l'�tude. Notre action majeure a �t� d'�liminer toutes les donn�es ant�rieures � 2014 en raison de la fermeture d'une dizaine de stations � cette date, cela induisant in�vitablement un probl�me de comparabilit� de plusieurs indicateurs.<br/>
>  Nous avons �galement �limin� nombre de variables inutiles � notre �tude et avons reconstitu� les donn�es manquantes, notamment les coordonn�es g�ographiques des incidents et des stations. <br/>
>  Enfin, nous avons supprim� quelques incidents ayant peu de sens pour notre �tude, comme les incidents de type "Water Provision" pour lequels nous avions tr�s peu d'observations.


<br/>
<h3>C - Analyse des donn�es</h3> 

<h4>i - Analyse des incidents en fonction des variables temporelles </h4> 
  
>   Une premi�re approche simple nous permet de v�rifier visuellement si les diff�rents facteurs temporels (mois, jour de la semaine, heure de la journ�e) ont une influence sur le nombre d'incidents :
>   
>   <p align="center"><img src=figures\Moyenne_par_mois.png width=600></p>
>   <p align="center"><img src=figures\Moyenne_par_jour.png width=600></p>
>   <p align="center"><img src=figures\Moyenne_par_heures.png width=600></p>
>   
>   Nous pouvons remarquer que le nombre moyen d'incidents varie plus ou moins fortement selon ces facteurs :
>   <ul><li> Un nombre moyen d'incidents plus important sur les mois estivaux (de mai � septembre) par rapport au reste de l'ann�e, avec un pic sur le mois de juillet.</li>
>   <li> Une relation que l'on retrouve en moindre mesure en fonction des jours de la semaine : une densit� d'incidents un peu plus forte les vendredi et surtout samedi, mais comparable sur les autres jours.</li>
>   <li> Et enfin, assez logiquement, une forte influence de l'horaire sur le nombre moyen d'incidents : une densit� bien plus forte sur les heures de la journ�e avec un pic en fin d'apr�s-midi/d�but de soir�e.</li></ul>
>   
>   
>   Nous avons ensuite r�alis� des tests statistiques afin de v�rifier que ces constats se v�rifient. Nos 3 tests ANOVA concernant l'influence de nos 3 variables temporelles sur le nombre d'incidents moyen, nous indique que l'hypoth�se selon laquelle les variables sont ind�pendantes est rejet�e avec des p values extr�mement proches de 0. Nos 3 variables temporelles ont donc un effet statistique significatif sur le nombre d'incidents moyen.
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
>   Nous nous sommes �galement int�ress�s � savoir si ces m�mes variables pouvaient avoir une incidence sur le temps d'attente, c'est-�-dire le temps pass� entre l'appel des secours et leur arriv�e sur place.
>   
>  <br/>
>   <p align="center"><img src=figures\Temps_attente_par_mois.png width=600></p>
>   <p align="center"><img src=figures\Temps_attente_par_jour.png width=600></p>
>   <p align="center"><img src=figures\Temps_attente_par_heures.png width=600></p>
>  <br/><br/>
>   Les variations sur le temps d'attente sont moins flagrantes, mais s'expliquent en grande partie par le fait que cette variable n'a pas une grande amplitude de mani�re g�n�rale.<br/><br/>
>  N�anmoins, certains enseignements se recoupent avec la distribution des incidents d�crite plus haut :
>   <ul><li> Le temps d'attente est sensiblement plus important sur les mois estivaux, tout comme l'�tait la densit� des incidents.</li>
>   <li> En revanche, nous n'observons pas de relation clairement visible entre le temps d'attente et le jour de la semaine ou l'heure de la journ�e.</li></ul>
>  <br/><br/>
>   Nous avons �galement v�rifi� � l'aide de tests ANOVA si ces variables temporelles influencent significativement le temps d'attente. 
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
>  Pour ces 3 tests, nous avons pos� l'hypoth�se que le temps d'attente est ind�pendant du mois, du jour de la semaine et de l'heure de l'incident.
>  Les p values des tests li�s au mois et � l'heure de l'incident sont extr�ment proches de 0, nous pouvons donc noter un effet statistique significatif de ces variables sur le temps d'attente. La p value du test li� au jour de la semaine est d'environ 80 %, indiquant donc cette variable n'a pas d'effet statistique significatif sur le temps d'attente des secours.

<br/>
<h4>ii - Analyse en fonction du type d'incident </h4> 

>   Au-del� des facteurs temporels, nous nous sommes �galement demand� s'il pouvait exister un lien entre le temps d'attente et la nature de l'incident. En effet, selon le type d'incident, les besoins peuvent �tre diff�rents en termes de type de v�hicule � d�ployer, ce qui peut influencer le temps de d�ploiement en fonction de la disponibilit� du v�hicule par exemple.
>  <br/><br/>
>  Regardons tout d'abord la r�partition des types d'incidents trait�s par la London Fire Brigade depuis 2014 :
>  <br/><br/>
>   <p align="center"><img src=figures\Moyenne_par_type.png width=600></p>
>  <br/><br/>
>   On remarque que la grande majorit� des sources d'intervention sont li�es aux Alarmes Automatiques d'Incendie. Ensuite, et dans une moindre mesure, on retrouve comme autres raisons principales : les incendies, les op�rations d'entr�e-sortie de personnes, les innondations puis les accidents de la route. D'apr�s notre test ANOVA, le type d'incident a un lien significatif avec le nombre d'incidents (p value nulle).
>  <p align="center">
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 9.44883e+07 |     3.77953e+06 | 238.183 |        0 |
>  | Residual | 17218 | 2.73218e+08 | 15868.1         | nan     |      nan |
>  </p>
>  <br/><br/>
>  Ici encore, nous v�rifions l'incidence sur le temps d'attente visuellement puis statistiquement.
>  <br/><br/>
>   <p align="center"><img src=figures\Temps_attente_par_type.png width=800></p>
>  <br/><br/>
>   Le temps d'attente �volue donc du simple au double selon le type d'incident. La LFB met deux fois plus de temps pour se rendre sur un incendie que pour porter secours lors d'une noyade.
>  Cette influence de la nature de l'intervention sur le temps d'attente est par ailleurs confirm�e par le test ANOVA qui indique un lien significatif entre les deux variables (p value nulle).
>  <p align="center">
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 1.34913e+08 |     5.39652e+06 |  69.132 |        0 |
>  | Residual | 17218 | 1.34406e+09 | 78061.1         | nan     |      nan |
</p>
<br/>
<h4>iii - Analyse en fonction de la localisation de l'incident </h4> 

>   Dans un premier temps, nous avons souhait� visualiser l'ensemble des incidents en fonction de leur localisation, en colorant chaque point, repr�sentant un incident, en fonction de la station qui a r�pondu en premier sur l'intervention.
>  <br/><br/>
>  Ceci nous permet de voir la r�partition des stations et leur rayon d'action :
>  <br/><br/>
>   <p align="center"><img src=figures\Carte_incident_station.png></p>
>  <br/><br/>
>   Le test ANOVA �valuant l'ind�pendance de la station de d�ploiement du temps d'attente nous montre un lien significatif entre ces variables (p value nulle). On peut donc supposer que : soit certaines stations sont intrins�quement plus performantes que d'autres (gr�ce � des �quipes plus exp�riment�es par exemple), soit c'est l'emplacement des stations qui va agir indirectement sur le temps d'attente.
>   <p align="center">
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>  | DeployedFromStation_Code |    101 | 5.69136e+08 |     5.63501e+06 | 315.144 |        0 |
>  | Residual                 | 683719 | 1.22254e+10 | 17880.7         | nan     |      nan |
>   </p>
>  <br/>
>  Nous avons �galement pr�t� attention � la densit� des incidents r�partis sur l'ensemble de la ville (ici en 2020) : 
