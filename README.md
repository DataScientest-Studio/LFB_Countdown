<h1>Projet London Fire Brigade CountDown</h1>
<br/><br/>
<p align="center"><img src=figures\LFB_illustration.png width=1000></p>
<br/><br/>
                                                 

<h3>Elora VABOIS, Marie LE COZ, Nicolas RAYMOND</h3>
<h3>DA Bootcamp Mai 2021</h3>
<br/>


<h2>INTRODUCTION</h2>
<br/>

>   Dans le cadre de notre formation Data Analyst, un projet fil rouge nous est propos� nous donnant ainsi l'opportunit� d'appliquer sur un cas concret et global les connaissances acquises tout au long de notre parcours. Le choix du sujet a �t� une �tape cruciale pour notre �quipe et nous avons finalement jet� notre d�volu sur un des projets propos�s dans le catalogue fourni : � Pr�diction du temps de r�ponse d�un v�hicule de la Brigade des Pompiers de Londres �.
>  <br/><br/>
>  Au del� du sujet en lui-m�me, ce choix r�sulte en grande partie de la richesse des donn�es exploitables, la vari�t� des types d'analyse que nous avons rapidement identifi�s (temporelles, g�ographiques, etc.) et des applications qu'elles entra�neraient. Nous avions �galement � coeur de travailler sur un sujet pour lequel nous percevions un challenge en Machine Learning. 
>  <br/><br/>
>  Ce projet vise � �tudier l'ensemble des diff�rents incidents auxquels ont r�pondu et pour lesquels sont intervenus les pompiers de la c�l�bre brigade de Londres entre 2009 et 2021, avec pour objectif final de pouvoir pr�dire le temps d'attente des pompiers pour les incidents ult�rieurs. 

<br/><br/>
<h2>1 - ANALYSE DES DONNEES</h2>

<h3>A - Introduction aux donn�es</h3> 

</br>

> Nous avons � notre disposition 3 jeux de donn�es officielles afin d'analyser les contours du projet : 
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
>   Nous nous sommes �galement int�ress�s � savoir si ces m�mes variables pouvaient avoir une incidence sur le temps d'attente, c'est-�-dire le temps pass� entre l'appel des secours et leur arriv�e sur place.
>   
>  <br/><br/>
>   <p align="center"><img src=figures\Temps_attente_par_mois.png width=600></p>
>   <p align="center"><img src=figures\Temps_attente_par_jour.png width=600></p>
>   <p align="center"><img src=figures\Temps_attente_par_heures.png width=600></p>
>  
>   Les variations sur le temps d'attente sont moins flagrantes, mais s'expliquent en grande partie par le fait que cette variable n'a pas une grande amplitude de mani�re g�n�rale.<br/><br/>
>  N�anmoins, certains enseignements se recoupent avec la distribution des incidents d�crite plus haut :
>   <ul><li> Le temps d'attente est sensiblement plus important sur les mois estivaux, tout comme l'�tait la densit� des incidents.</li>
>   <li> En revanche, nous n'observons pas de relation clairement visible entre le temps d'attente et le jour de la semaine ou l'heure de la journ�e.</li></ul>
>  
>   Nous avons �galement v�rifi� � l'aide de tests ANOVA si ces variables temporelles influencent significativement le temps d'attente. 
>   <br/><br>
>
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
>  Pour ces 3 tests, nous avons pos� l'hypoth�se que le temps d'attente est ind�pendant du mois, du jour de la semaine et de l'heure de l'incident.
>  Les p values des tests li�s au mois et � l'heure de l'incident sont extr�ment proches de 0, nous pouvons donc noter un effet statistique significatif de ces variables sur le temps d'attente. La p value du test li� au jour de la semaine est d'environ 80 %, indiquant donc cette variable n'a pas d'effet statistique significatif sur le temps d'attente des secours.

<br/>
<h4>ii - Analyse en fonction du type d'incident </h4> 

>   Au-del� des facteurs temporels, nous nous sommes �galement demand� s'il pouvait exister un lien entre le temps d'attente et la nature de l'incident. En effet, selon le type d'incident, les besoins peuvent �tre diff�rents en termes de type de v�hicule � d�ployer, ce qui peut influencer le temps de d�ploiement en fonction de la disponibilit� du v�hicule par exemple.
>  <br/><br/>
>  Regardons tout d'abord la r�partition des types d'incidents trait�s par la London Fire Brigade depuis 2014 :
>  <br/><br/>
>   <p align="center"><img src=figures\Moyenne_par_type.png width=600></p>
>  <br/>
>   On remarque que la grande majorit� des sources d'intervention sont li�es aux Alarmes Automatiques d'Incendie. Ensuite, et dans une moindre mesure, on retrouve comme autres raisons principales : les incendies, les op�rations d'entr�e-sortie de personnes, les innondations puis les accidents de la route. D'apr�s notre test ANOVA, le type d'incident a un lien significatif avec le nombre d'incidents (p value nulle).
>  <br/><br/>
>
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 9.44883e+07 |     3.77953e+06 | 238.183 |        0 |
>  | Residual | 17218 | 2.73218e+08 | 15868.1         | nan     |      nan |
>  
>  <br/><br/>
>  Ici encore, nous v�rifions l'incidence sur le temps d'attente visuellement puis statistiquement.
>  <br/>
>   <p align="center"><img src=figures\Temps_attente_par_type.png width=800></p>
>  <br/>
>   Le temps d'attente �volue donc du simple au double selon le type d'incident. La LFB met deux fois plus de temps pour se rendre sur un incendie que pour porter secours lors d'une noyade.
>  Cette influence de la nature de l'intervention sur le temps d'attente est par ailleurs confirm�e par le test ANOVA qui indique un lien significatif entre les deux variables (p value nulle).
>  <br/><br/>
>
>  |          |    df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:---------|------:|------------:|----------------:|--------:|---------:|
>  | type     |    25 | 1.34913e+08 |     5.39652e+06 |  69.132 |        0 |
>  | Residual | 17218 | 1.34406e+09 | 78061.1         | nan     |      nan |
>
<br/>
<h4>iii - Analyse en fonction de la localisation de l'incident </h4> 

>   Dans un premier temps, nous avons souhait� visualiser l'ensemble des incidents en fonction de leur localisation, en colorant chaque point, repr�sentant un incident, en fonction de la station qui a r�pondu en premier sur l'intervention.
>  <br/><br/>
>  Ceci nous permet de voir la r�partition des stations et leur rayon d'action :
>   <p align="center"><img src=figures\Carte_incident_station.png></p>
>   Le test ANOVA �valuant l'ind�pendance de la station de d�ploiement du temps d'attente nous montre un lien significatif entre ces variables (p value nulle). On peut donc supposer que : soit certaines stations sont intrins�quement plus performantes que d'autres (gr�ce � des �quipes plus exp�riment�es par exemple), soit c'est l'emplacement des stations qui va agir indirectement sur le temps d'attente.
>   <br/>
>
>  |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>  |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>  | DeployedFromStation_Code |    101 | 5.69136e+08 |     5.63501e+06 | 315.144 |        0 |
>  | Residual                 | 683719 | 1.22254e+10 | 17880.7         | nan     |      nan |
>   
>  <br/>
>  Nous avons �galement pr�t� attention � la densit� des incidents r�partis sur l'ensemble de la ville (ici en 2020) : 
> <br>
>  voir figure CarteDeDensiteBokeh.html
>
>   Comme nous nous y attendions, les incidents sont plus nombreux au centre-ville qu'en p�riph�rie, tout comme le sont les stations.
> <br/><br/>
> Le test ANOVA entre le nombre d'incidents et le district (PostCode_district) du lieu d'incident indique un lien significatif entre ces variables (p value nulle).
>   <br/>
>
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
> |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
> | District |    328.0 | 3.343984e+08 |     1.019507e+06 | 22.724574 |        0 |
> | Residual                 | 134211.0 | 6.021195e+09 | 4.486365e+04         | nan     |      nan ||
>
>   <br/>
> Nous avons ensuite souhait� voir la r�partition g�ographique des incidents sur la carte de Londres, en filtrant les donn�es par ann�e et en colorant ces points par rapport aux temps d'attente (les points verts repr�sentant les temps d'attente les plus faibles, les points rouges les plus longs). Nous avons ins�r� les stations sur cette carte (triangles noirs) afin de visualiser l'impact de la proximit� avec une station sur le d�lai d'intervention.
><br>
>  voir figure TempsDAttenteParAn.html
>
>   Cette derni�re visualisation permet de bien identifier les zones en fonction de la r�activit� des secours. On observe que plus l'incident est �loign� d'une station, plus le temps d'attente tend � augmenter. 
>   <br/><br/>
>   Le test ANOVA qui concerne le temps d'attente et le district (PostCode_district) du lieu d'incident indique un lien significatif entre ces variables (p value nulle).
>   <br/>
>
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>   |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>   | District |    328.0 | 9.468728e+05 |     2886.807444 | 88.86169 |        0 |
>   | Residual                 | 134211.0 | 4.360049e+06 | 32.486524         | nan     |      nan ||
>  
>   <br/>
>   De plus, le test de Pearson liant la distance entre le lieu d'incident et la station de d�ploiement avec le temps d'attente nous indique que ces variables ont un lien significatif (p value nulle) et que leur corr�lation est relativement importante (coefficient de Pearson : 51.5%).
>   <br/><br/>
>
>   |                          |     r�sultat test |
>   |:-------------------------|-------:|
>   | pearson_coeff |    0.515065 | 
>   | p-value                 | 0.000000 ||


<h4>iv - Autres tests statistiques r�alis�s </h4> 

>   Nous avons �galement �tudi� la corr�lation entre le type de retard �ventuel (DelayCode_Description) et le temps d'attente et notre test ANOVA indique un lien significatif entre ces variables (p value nulle). Cependant, nous ne pourrons pas conserver cette variable pour la mod�lisation car elle n'est connu qu'� posteriori : elle ne peut donc pas servir � la pr�diction.
>   <br/>
>
>   |                          |     df |      sum_sq |         mean_sq |       F |   PR(>F) |
>   |:-------------------------|-------:|------------:|----------------:|--------:|---------:|
>   | DelayCode_Description |    9.0 | 3.273134e+09 |     3.636815e+08 | 26118.986271 |        0 |
>   | Residual                 | 683811.0 | 9.521404e+09 | 1.392403e+04         | nan     |      nan |

<br/>
<h3>D - Conclusion sur l'analyse des donn�es</h3> 

>   Cette premi�re �tape d'analyse des donn�es nous confirme bien que les indicateurs �tudi�s seront indispensables dans le cadre de la mod�lisation du temps d'intervention de la LFB. 
<br/>

<h2>2 - MODELISATION</h2>

<h3>A - Preprocessing des donn�es</h3> 

>   Une fois l�analyse du dataset r�alis�e, nous avons proc�d� au nettoyage et au preprocessing des donn�es, afin d�assurer le bon d�roulement de la phase de mod�lisation.
>   Nous avons donc d�termin� : </br><ul><li>Les variables explicatives � supprimer : celles n�ayant pas influence sur notre variable cible ou �tant redondantes avec d�autres variables ainsi que celles n'�tant connues qu'� posteriori. </li></br><li>Les variables explicatives � convertir : dichotomisation des variables cat�gorielles, conversion de la variable �TimeOfCall� en variable num�rique (float). </li> </br><li>Les variables explicatives � cr�er : fusion des 2 variables li�es �SpecialServiceType� et �StopCodeDescription� en une variable unique �IncidentTypeGlobal�, puis, une fois les coordonn�es g�ographiques des casernes r�cup�r�es, cr�ation d�une variable �distFromStation� indiquant la distance entre le lieu de l�intervention et la caserne �tant intervenue et suppression des coordonn�es (car nous avons d�j� les variables Borough - quartier - et DeployedFromStation - station de d�ploiement - qui donnent des indications sur l�emplacement de l�incident). </li></ul>
>   </br>
>   La majeure partie de nos features �tant des variables cat�gorielles contenant de nombreuses modalit�s pour la plupart, la dichotomisation a ainsi g�n�r� un dataset final avant mod�lisation de dimension cons�quente avec 549 colonnes pour environ 680&#8239;000 lignes.<br/><br/>
>   Nous avons ensuite mis en place un Train Test split en nous assurant que les donn�es les plus r�centes soient conserv�es pour le test.<br/><br/>
>   Enfin, nous avons proc�d� � l��tape de scaling afin de g�n�rer un dataset normalis� pour les mod�les qui le n�cessitent.

<br/>
<h3>B - It�rations mod�lisation</h3> 

<h4> i - Premi�re it�ration </h4> 

<h5><li> Mod�les entra�n�s </li></h5> 

>   Les mod�les qu'on a instanci�s dans un premier temps sont les mod�les de r�gression lin�aires classiques (LinearRegression seul puis avec SelectKBest et SelectFromModel, ElasticNetCV), HistGradientBoosting, DecisionTree, ainsi que Lasso et Ridge. Nous avons d�cid� de ne pas tester KNN qui n'est pas adapt� aux gros datasets de par son mode de calcul.
>   <br>
>   Nous avons recherch� les hyper-param�tres optimaux � l'aide d'une GridSearch pour les mod�les qui le permettaient.

<h5><li> Contraintes rencontr�es </li></h5> 

>   Nous avons rencontr� de nombreuses difficult�s techniques li�es � la taille du dataset (memory error, interruption kernels et temps de calculs extr�mement importants� ).
>   Nous avons donc d� nous limiter � un dataset contenant les 250 000 derni�res lignes (les plus r�centes).

<h5><li> R�sultats obtenus </li></h5> 

>   |    | model                               |   R� train |      R� test |   mse train |        mse test |   mae train |         mae test | param�tres retenus                                                                                                                                                          |
>   |---:|:------------------------------------|-----------:|-------------:|------------:|----------------:|------------:|-----------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
>   |  0 | LinearRegression                    |   0.324491 | -4.21421e+12 |     11500.1 |     6.37987e+16 |     70.1761 | 922374           |                                                                                                                                                                             |
>   |  1 | SelectKBest r�gression lin�aire     |   0.299405 |  0.338849    |     11927.2 | 10009.1         |     72.2332 |     68.5351      | f_regression,k=100,nb_cols=100                                                                                                                                              |
>   |  2 | SelectFromModel r�gression lin�aire |   0.068366 | -2.02101e+15 |     15860.5 |     3.05961e+19 |     89.8018 |      2.01978e+07 | nb_cols=111                                                                                                                                                                 |
>   |  3 | ElasticNetCV                        |   0.323789 |  0.355323    |     11512.1 |  9759.74        |     70.2753 |     67.4525      | alpha :  0.05 parmi alphas=(0.001, 0.01, 0.02, 0.025, 0.05, 0.1, 0.25, 0.5, 0.8, 1.0), l1_ratio :  0.75 parmi l1_ratio=(0.1, 0.25, 0.5, 0.7, 0.75, 0.8, 0.85, 0.9, 0.99)    |
>   |  4 | LassoCV                             |   0.32375  |  0.356218    |     11512.7 |  9746.19        |     70.1925 |     67.3646      | alpha=0.066393                                                                                                                                                              |
>   |  5 | RidgeCV                             |   0.324491 |  0.35625     |     11500.1 |  9745.71        |     70.1762 |     67.3651      | alpha=1 parmi alphas= (0.0001,0.0005,0.001, 0.005,0.01, 0.05,0.1,0.5,1)                                                                                                     |
>   |  6 | DecisionTree                        |   0.344382 |  0.347896    |     11161.5 |  9872.18        |     70.5671 |     67.6965      | max_depth=7 parmi [2, 3, 4, 5, 6, 7, 8], criterion=friedman_mse                                                                                                             |
>   |  7 | DecisionTree                        |   0.344382 |  0.347034    |     11161.5 |  9885.23        |     70.5671 |     67.7137      | max_depth=7 parmi [2, 3, 4, 5, 6, 7, 8], criterion=mse                                                                                                                      |
>   |  8 | HistGradientBoosting                |   0.391331 |  0.389738    |     10362.2 |  9238.74        |     66.6608 |     64.8576      | min_samples_leaf = 500, loss=least_squares parmi [least_squares,least_absolute_deviation], max_iter=250 parmi [50,70,100,120,150,170,200,250], max_depth=8 parmi range(3,9) |
> 
> Le mod�le le plus performant est le mod�le Hist Gradient Boosting quelque soit le crit�re de performance observ� : il pr�sente les R� les plus �lev�s ainsi que les MSE et MAE les plus faibles.
>   <br>
>   Pour cette premi�re it�ration, nous obtenons pour l�ensemble de nos tests, hormis pour le HistGradientBoosting :
> <ul><li> Des scores R� peu concluants</li>
> <li>Des MAE d'environ une minute et 10 secondes pour la plupart des mod�les.</li></ul>
>   
>   Suite � cette it�ration, nous avons essay� de renouveler l'exp�rience avec ces mod�les sur le dataset complet.

<br>
<h4> ii - Deuxi�me it�ration </h4> 

<h5><li> Objectifs </li></h5> 

>   Nous avons cr�� un script regroupant tous nos mod�les et produisant un fichier �Resultat.csv� de mani�re � pouvoir tester nos mod�les sur le dataset complet (tr�s lourd) sur une machine plus puissante. Nous avons �galement ajout� des hyper-param�tres que nous n�avions pas pu tester sur nos machines (par exemple des criterions pour les DecisionTree).

<h5><li> Mod�les entra�n�s et ajustement r�alis�s </li></h5> 

>   Nous avons utilis� les m�mes mod�les que pr�c�demment et y avons ajout� les mod�les GradientBoosting, HistGradientBoosting, LassoCV et Ridge sur le dataset pr�-format� gr�ce au transformateur PolynomialFeatures. Ce dernier permet de cr�er de nouvelles variables repr�sentant l'interaction des variables initiales (si on a un dataset avec les variables a et b, PolynomialFeatures renverra un nouveau dataset avec les variables 1, a, b et ab avec les param�tres degree=2 et interaction_only=True).


<h5><li> Contraintes rencontr�es </li></h5> 

>   Le mod�le DecisionTree a bloqu� le script qui ne s��tait toujours pas arr�t� apr�s plus de 24 heures.

<h5><li> R�sultats obtenus </li></h5> 

>   Nous n�avons pu recueillir aucun r�sultat au cours de cette tentative.

<br/>
<h4> iii - Troisi�me it�ration </h4> 

<h5><li> Objectifs </li></h5>

>   Suite � notre �chec pr�c�dent, nous avons repris notre dataset r�duit avec les 250 000 mobilisations les plus r�centes. Nous avons essay� d'am�liorer les premi�res performances obtenues gr�ce au mod�le HistGradientBoosting.
>   <br/><br/>
>   Nous avons d�cid� d�optimiser la recherche d�hyper-param�tres � l�aide du package Optuna. Optuna a le m�me objectif que la GridSearchCV&#8239;: il permet de trouver la combinaison d'hyper-param�tres la plus performante. Cependant, il n'op�re pas de la m�me mani�re. Tandis que la GridSearch �value toutes les combinaisons d'hyper-param�tres existantes parmi les valeurs qui lui ont �t� fournies, ce sont des plages de valeurs qui sont fournies � Optuna. Cela lui permet d'explorer l'ensemble de l'espace sans avoir � tester toutes les combinaisons pour un param�tre ayant peu d'influence par exemple.
>   <br>Nous avons �galement remplac� HistGradientBoosting par LightGBM qui est optimis� en temps de calcul.
>   Au cours des diff�rentes it�rations, il a fallu d�terminer si nous �tions en r�gime de sur ou sous-apprentissage et le combattre.

<h5><li> Mod�les entra�n�s et ajustement r�alis�s </li></h5>

>   Nous avons entra�n� le mod�le LGBMRegressor avec le package Optuna. Nous avons proc�d� en plusieurs it�rations pour trouver quels hyper-param�tres tester et sur quelles plages.

<h5><li> R�sultats obtenus au cours des diff�rentes �tapes </li></h5>

<u><em>Etape 1</em></u>
>   3 hyper-param�tres test�s avec 200 trials :
>   <br/>
>   
	learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
	max_depth = trial.suggest_int('max_depth', 2, 50)
	n_estimators = trial.suggest_int('n_estimators', 20,500)
>  
>   Best trial :

	learning_rate = 0.1012069771826192
	max_depth = 40
	n_estimators = 488
   
<br/>  

>   | model                                                                         |   R� train |   R� test |   mse train |   mse test |   mae train |   mae test |
>   |:------------------------------------------------------------------------------|-----------:|----------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor1 |   0.454652 |  0.409216 |     9284.22 |    8943.85 |     62.8125 |    63.2457 |
>   
>   Les performances sont plut�t satisfaisantes, la MAE s'est rapproch� d'une minute.
>   <br/>
>   Nous sommes en sur-apprentissage l�ger. 
>   Pour l��tape 2, nous essaierons d�ajouter d�autres hyper-param�tres afin de tenter de le r�duire.

<u><em>Etape 2</em></u>
>   6 hyper-param�tres test�s avec 200 trials :
>   <br/>
>   
	learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
	max_depth = trial.suggest_int('max_depth', 2, 80)
	n_estimators = trial.suggest_int('n_estimators', 20,800)
	reg_alpha = trial.suggest_loguniform('reg_alpha', 1e-5,10)
	reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-5,10)
	subsample_for_bin = trial.suggest_int('subsample_for_bin', 200000, 500000)
>   
>   Best trial :
  
	learning_rate = 0.0735978242412042
	max_depth = 76
	n_estimators = 737
	reg_alpha = 0.000987737786289064
	reg_lambda = 3.6393223694815996e-05
	subsample_for_bin = 226071

<br/> 

>   | model                                                                            |   R� train |   R� test |   mse train |   mse test |   mae train |   mae test |
>   |:---------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor2    |      0.459334 |     0.410594 |      9204.5 |       8923 |      62.532 |    63.1363 ||
>   
>   Les performances ont l�g�rement augment�. En examinant les essais, le param�tre subsample_for_bin ne semble pas avoir beaucoup d�influence, c�est pourquoi nous avons d�cid� de le laisser � sa valeur par d�faut et de tester d�autres param�tres connus pour agir contre le sur-apprentissage. Nous allons �galement r�duire les plages de max_depth et n_estimators pour essayer de limiter ce sur-apprentissage.

<u><em>Etape 3</em></u>
>   8 hyper-param�tres test�s avec 200 trials :
>   <br/>
>   
	learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
	max_depth = trial.suggest_int('max_depth', 2, 40)
	n_estimators = trial.suggest_int('n_estimators', 20,500)
	reg_alpha = trial.suggest_loguniform('reg_alpha', 1e-5,10)
	reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-5,10)
	num_leaves = trial.suggest_int('num_leaves', 10, 50)
	min_split_gain = trial.suggest_uniform('min_split_gain', 0,1)
	min_child_samples = trial.suggest_int('min_child_samples', 5, 50)
>   
>   Best trial :


	learning_rate = 0.08611376087571489
	max_depth = 28
	n_estimators = 467
	reg_alpha = 0.007369798680853325
	reg_lambda = 0.0002296807544488281
	num_leaves = 47
	min_split_gain = 0.5709551773016567
	min_child_samples = 32
   
<br/>

>   |model                                                                           |   R� train |   R� test |   mse train |   mse test |   mae train |   mae test |
>   |:--------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor3    |      0.463816 |     0.411167 |     9128.22 |    8914.33 |     62.1916 |     63.052 ||
>   
>   Le sur-apprentissage a l�g�rement augment�, nous allons essayer de le r�duire en diminuant les plages de test des hyper-param�tres.

<u><em>Etape 4</em></u>
>   8 hyper-param�tres test�s avec 400 trials :
> <br/>
>   
	learning_rate = trial.suggest_loguniform('learning_rate', 1e-5,10)
	max_depth = trial.suggest_int('max_depth', 2, 20)
	n_estimators = trial.suggest_int('n_estimators', 20,300)
	reg_alpha = trial.suggest_loguniform('reg_alpha', 1e-5,10)
	reg_lambda = trial.suggest_loguniform('reg_lambda', 1e-5,10)
	num_leaves = trial.suggest_int('num_leaves', 10, 35)
	min_split_gain = trial.suggest_uniform('min_split_gain', 0,1)
	min_child_samples = trial.suggest_int('min_child_samples', 40, 200)
>   
>   Best trial :


	learning_rate = 0.1512198354101122
	max_depth = 17
	n_estimators = 295
	reg_alpha = 0.0005383830447172724
	reg_lambda = 0.00011538095876075694
	num_leaves = 32
	min_split_gain = 0.473924522550586
	min_child_samples = 43
   


>   |model                                                                        |   R� train |   R� test |   mse train |   mse test |   mae train |   mae test |
>   |:-----------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   |LGBMRegressor4 |      0.445746 |     0.410001 |     9435.83 |    8931.97 |     63.1968 |    63.1481 ||
>   
>   Lors de cet essai, le sur-apprentissage est moins important qu�auparavant et la performance est quasiment identique (� peine moindre), c�est pourquoi cela nous para�t �tre un compromis acceptable.


<h3>C - Choix et interpr�tabilit� du mod�le</h3>


<h4> i - Mod�le retenu  </h4> 

>   | model                                                                            |   R� train |   R� test |   mse train |   mse test |   mae train |   mae test |
>   |:---------------------------------------------------------------------------------|--------------:|-------------:|------------:|-----------:|------------:|-----------:|
>   | LGBMRegressor1    |      0.454652 |     0.409216 |     9284.22 |    8943.85 |     62.8125 |    63.2457 ||
>   | LGBMRegressor2   |      0.459334 |     0.410594 |     9204.50  |    8923.00    |     62.5320  |    63.1363 ||
>   | LGBMRegressor3    |      0.463816 |     0.411167 |     9128.22 |    8914.33 |     62.1916 |    63.0520  ||
>   | LGBMRegressor4     |      0.445746 |     0.410001 |     9435.83 |    8931.97 |     63.1968 |    63.1481 ||            |
>   
>   Finalement, nous avons d�cid� de retenir le mod�le LGBMRegressor4 qui produit de bons r�sultats tout en exigeant un temps de calcul tr�s raisonnable (non seulement par rapport aux mod�les de la premi�re it�ration puisque LightGBM est optimis�, mais �galement par rapport aux 3 premiers LGBMRegressor car c'est celui qui pr�sente le n_estimators le plus faible). On pourra lui reprocher d��tre peu interpr�table mais nous allons essayer d�y rem�dier dans la partie suivante gr�ce aux packages Skater et Shap.

<br/>
<h4> ii - Interpr�tabilit� du mod�le  </h4> 

<h5><li> Visualisation g�ographique de l'erreur </li></h5>

>   Avant d'utiliser les packages d'interpr�tabilit�, nous allons visualiser g�ographiquement l'erreur sur le jeu de donn�es test, de mani�re � rep�rer d'�ventuelles anomalies ou bien � confirmer la performance du mod�le.
> <br>
>  voir figure Erreur.html
>
> On peut voir sur cette figure que les erreurs importantes (nous avons repr�sent� les erreurs de plus de 2 minutes en rouge) sont r�parties de mani�re � peu pr�s homog�nes sur la carte. On peut cependant rep�rer qu'elles sont un peu plus pr�sentes en p�riph�rie de la ville. Cela peut s�expliquer par le fait que les temps d�attente sont en moyenne plus importants lorsque l�on s��carte du centre de Londres car les distances ont plus de chance d��tre grandes entre les casernes et le lieu d�incident en p�riph�rie. Or, plus les temps sont importants, plus les erreurs risquent d'�tre �lev�es.

<h5><li> Features importance du mod�le LGBMRegressor </li></h5>

>   Voici les features importantes d'apr�s le mod�le :
><br><br>
>   <p align="center"><img src=figures\Feature_importance_LGBM.png></p>
>   
>   Ce graphique nous permet de hi�rarchiser les variables selon leur importance pour la d�termination du temps d�attente des pompiers d�apr�s notre mod�le. La variable la plus importante est la distance entre le lieu de l�incident et la station depuis laquelle est d�ploy� le v�hicule (distFromStation). 
<br/><br/>
Nous voyons ensuite que l�heure d�appel (TimeOfCall) est �galement d�terminante : en effet, on peut supposer que le trafic routier n�est pas le m�me en fonction de l�heure de la journ�e et que cela joue un r�le important. <br/>Le nombre de v�hicules d�ploy�s (NumPumpsAttending) est ensuite repr�sent�, on peut supposer que l�urgence de la situation impacte le nombre de v�hicules et le temps de d�ploiement, ce qui pourrait lier ces deux variables.
<br/><br/>
Le fait que l�incident ait lieu dans un logement (Property_Dwelling) et non � l'ext�rieur, sur la route ou autre, semble �galement �tre un crit�re important. On peut effectivement penser qu�il est plus facile de se rendre dans une habitation qu�en ext�rieur sans rep�re pr�cis, car le fait de conna�tre l'adresse r�duira le temps n�cessaire pour se rendre sur place.

<h5><li> Package Skater </li></h5>


>   Le package Skater nous permet �galement de faire �merger l'importance des features dans la d�termination du mod�le. Ci-dessous le top 10 des features les plus importants :
><br><br>
>   <p align="center"><img src=figures\Skater_top10.png width=700> </p>
>    
<br/>
>   Comme identifi� pr�c�demment avec les features_Importance du mod�le LGBM retenu, la distance entre le lieu de l�incident et la station depuis laquelle le v�hicule est d�ploy� (distFromStation) est � nouveau de le feature qui contribue de tr�s loin le plus au mod�le. 
> <br/>Nous voyons � nouveau ressortir le nombre de v�hicules d�ploy�s (NumPumpsAttending) ainsi que l'heure d'appel (TimeOfCall) et certains types de propri�t�s (Property_NonResidential et Property_Outdoor).
> <br/><br/>
>Le package Skater nous permet par ailleurs de disposer d'informations plus pr�cises sur l'impact de ces features dans la pr�diction du mod�le.
<br/>
>   
>   Ainsi, la distance (distFromStation) affiche une relation quasi lin�aire avec le temps d�attente pr�dit. Ceci para�t logique puisque plus la station est loin de l�incident, plus le temps de trajet a des chances d'�tre important.
<br/><br/>
>   <p align="center"><img src=figures\distFromStation.png width=500> </p>
>  
<br/>
>  S'agissant du nombre de v�hicules d�ploy�s (NumPumpsAttending), on constate que plus le nombre de camions qui interviennent est important, plus le temps d�attente pr�dit est court. Cela pourrait s'expliquer par le fait que les incidents nec�ssitant l'intervention de plusieurs v�hicules ont probablement un niveau de gravit� plus important et n�cessitent en cons�quence une r�activit� plus forte des secours.
<br/><br/> 
>   <p align="center"><img src=figures\NumPumpsAttending.png width=500> </p>
>   
<br/>
>   L'heure � laquelle est donn�e l'alerte (TimeOfCall) est ensuite le troisi�me feature en termes d'importance. Le temps d�attente pr�dit est plus long durant les heures de nuit qu�en journ�e. On peut supposer qu'il y a moins d'�quipes disponibles la nuit, ce qui allongerait les temps d'attente. 
<br/><br/>
>   <p align="center"><img src=figures\TimeOfCall.png width=500> </p>
>   
<br/>
>   Lorsqu�on compare cette courbe avec celle du temps d'attente r�el (ci-dessous), on se rend compte que le mod�le prend bien en compte les disparit�s observ�es selon les tranches horaires. 
<br/><br/>
>   <p align="center"><img src=figures\Temps_attente_par_heures_Xtrain.png width=500> </p>
>   
<br/> 
>   Enfin, parmi les autres facteurs qui contribuent le plus au mod�le, on retrouve diff�rents features issus de la variable PropertyType (Outdoor, NonResidential, Roadvehicle). Si Skater identifie la nature du lieu d'intervention parmi les facteurs les plus contributifs au mod�le, les graphiques ci-dessous ne montrent cependant pas de diff�rence marqu�e au niveau de la pr�diction. Nous pouvons en d�duire que ces crit�res, pris ind�pendamment, ne jouent pas un r�le important, mais que leur importance est conditionn�e par le fait d'�tre combin�e avec un ou plusieurs autres features.
>
>   
>   <p align="center"><img src=figures\Property_Outdoor.png width=500> </p>
>
>   <p align="center"><img src=figures\Property_NonResidential.png width=500> </p>
>
>   <p align="center"><img src=figures\Property_RoadVehicle.png width=500> </p>
> 



<h5><li> Package Shap </li></h5>

>   Le package Shap nous propose �galement une autre lecture de l'importance des features pour le mod�le. Celui-ci d�termine le classement suivant des 10 features les plus importants :
>   
>   <p align="center"><img src=figures\Shap_feature_importance.png width=700> </p>
>   
>   On retrouve � nouveau la distance entre la station et l�incident (distFromStation) comme �tant le facteur principal de la pr�diction. Nous trouvons ensuite le nombre de v�hicules d�ploy�s (NumPumpsAttending), l�heure d�appel (TimeOfCall) et le fait que le lieu de l'incident soit non r�sidentiel (Property_NonResidential).
>   
>   <p align="center"><img src=figures\Shap_value_feature.png width=700> </p>
>   
>   Sur ce second graphique, nous pouvons voir que plus la distance entre la station et l�incident est grande, plus elle influe positivement sur le temps d�attente. Et � l'inverse, une diminution de la distance tend � r�duire le temps d�attente&#8239;: cela confirme la relation forte existante entre la distance s�parant le lieu d'incident et la caserne avec le temps d'attente. 
<br><br> 
Concernant les deux variables suivantes, les diff�rentes valeurs sont moins dissoci�es, il est donc plus difficile de tirer des conclusions. On peut tout de m�me dire que lorsque peu de camions sont d�ploy�s (NumPumpsAttending), le temps d'attente augmente l�g�rement.
<br><br>
Lorsque l'incident a lieu dans un lieu non r�sidentiel (Property_NonResidential), le temps d'attente diminue l�g�rement.
<br><br> Les incidents en ext�rieur (Property_Outdoor) peuvent soit faire diminuer, soit faire augmenter le temps d'attente.
<br><br>Les incidents ayant lieu le dimanche semble b�n�ficier d'un temps d'attente l�g�rement inf�rieur comme nous l'avons vu lors de l'exploration de donn�es.
<br><br>Comme nous l�avions identifi� lors de l�analyse des donn�es, le mod�le a bien retranscrit le fait que lorsque l�incident est de type m�dical (IncidentType_MedicalIncident), le temps d�attente diminue grandement. C'est �galement le cas en moindre proportion pour les accidents de la route (IncidentType_RoadTrafficCollision).

<h3>D - Conclusion sur la partie mod�lisation</h3>

>  Notre mod�le pr�sente une pr�cision moyenne (MAE) d'environ 1 minute (63 secondes). Ceci semble �tre raisonnable lorsqu'on pense aux applications qui peuvent en �tre faites. En effet, si un op�rateur t�l�phonique des pompiers l'utilise pour annoncer un temps d'attente estim� aux victimes, une minute d'erreur semble �tre acceptable. D'autre part, le calcul de cette estimation par notre mod�le sera suffisament rapide pour cette utilisation.
<br><br>
Gr�ce � cette �tude d'interpr�tabilit�, nous avons pu voir que notre mod�le semble pr�senter une logique plut�t compr�hensible. Les variables utilis�es semblent logiquement influentes et correspondent globalement � ce que l'on avait pu identifier lors de l'analyse des donn�es.
<br/>
<h2>3 - BILAN</h2>
<br/>

>   Plus ou moins abstrait pour chacun des membres de notre groupe en d�but de formation, ce projet nous a permis de bien nous familiariser avec les principes de machine learning, tant du point de vue th�orique que pratique. Les travaux effectu�s dans le cadre de cette �tude ont en effet eu un r�le compl�mentaire aux apprentissages via les notebooks de la plateforme. Ils ont permis une r�flexion et une application au travers d'un cas concret.
<br/><br/>
Au-del�, c'est toute la cha�ne d'un projet de data analyse qu'il nous a �t� propos� de mettre en oeuvre : r�cup�ration des donn�es, compr�hension/interpr�tation des variables et de leurs modalit�s, cleaning et structuration des donn�es, transformation et cr�ation de nouvelles variables, analyse des donn�es et dataviz, preprocessing, entra�nement d'algorithmes, recherche d'hyperparam�tres optimaux, choix et interpr�tation d'un mod�le.
<br/><br/>
Autre d�couverte int�ressante dans la cadre de ce projet, impuls�e par notre mentor : la prise en main de diff�rentes plateformes collaboratives pour contribuer ensemble au projet : tout d'abord Google Colab, puis Datalore et enfin GitHub.
<br/><br/>
La phase d'exploration des donn�es nous a amen� � faire une recherche approfondie sur la signification des diff�rentes variables, issues des 3 sources de donn�es diff�rentes. Nous avons �galement d� traiter des donn�es de diverses natures (num�riques, cat�gorielles, temporelles, g�ographiques) nous permettant de faire une analyse des donn�es sous diff�rents angles : distribution, temporel, g�ographique.
<br/><br/>
Nous avons �galement �t� confront�s aux contraintes, notamment techniques, que pouvait engendrer le traitement d'un dataset volumineux (plus d'un million de lignes � la base) : des temps de calcul potentiellement tr�s longs, voire trop lourds pour pouvoir faire tourner certains mod�les sur nos ordinateurs personnels. Une difficult� qui nous a amen� � faire des choix (limitation du nombre d'observations, appui technique de notre mentor...). Une contrainte qui aurait �ventuellement pu �tre contourn�e avec l'utilisation d'outils pour le big data, comme Pyspark par exemple (que nous n'avions pas encore abord� dans le cadre de la formation lorsque nous aurions pu l'utiliser).
<br/><br/>
En d�pit de tr�s nombreux tests et recherches (tant en termes de mod�les que d'hyperparam�tres), notre meilleur mod�le enregistre des performances relativement modestes. Mais celui-ci a n�anmoins le m�rite d'afficher une interpr�tabilit� assez claire et plut�t logique compte tenu des variables explicatives inject�es dans le mod�le.
Quelques pistes pourraient n�anmoins permettre ult�rieurement d'optimiser notre mod�le :
>   <ul><li>Faire appel � des machines plus puissantes pour pouvoir faire tourner d'autres mod�les</li>
    <li>Utiliser des outils de big data plus performants dans le traitement de datasets volumineux</li>
    <li>Recueillir d'autres donn�es autour des interventions qui pourraient aider � mieux expliquer le mod�le</li>
