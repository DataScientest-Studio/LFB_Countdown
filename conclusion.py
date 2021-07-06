# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""
import streamlit as st



def affichage_conclu():
    st.markdown("""
                >   Plus ou moins abstrait pour chacun des membres de notre groupe en début de formation, ce projet nous a permis de bien nous familiariser avec les principes de machine learning, tant du point de vue théorique que pratique. Les travaux effectués dans le cadre de cette étude ont en effet eu un rôle complémentaire aux apprentissages via les notebooks de la plateforme. Ils ont permis une réflexion et une application au travers d'un cas concret.
                <br/><br/>
                
                > Au-delà, c'est toute la chaîne d'un projet de data analyse qu'il nous a été proposé de mettre en oeuvre : récupération des données, compréhension/interprétation des variables et de leurs modalités, cleaning et structuration des données, transformation et création de nouvelles variables, analyse des données et dataviz, preprocessing, entraînement d'algorithmes, recherche d'hyperparamètres optimaux, choix et interprétation d'un modèle.
                <br/><br/>

                > Autre découverte intéressante dans la cadre de ce projet, impulsée par notre mentor : la prise en main de différentes plateformes collaboratives pour contribuer ensemble au projet : tout d'abord Google Colab, puis Datalore et enfin GitHub.
                <br/><br/>

                > La phase d'exploration des données nous a amené à faire une recherche approfondie sur la signification des différentes variables, issues des 3 sources de données différentes. Nous avons également dû traiter des données de diverses natures (numériques, catégorielles, temporelles, géographiques) nous permettant de faire une analyse des données sous différents angles : distribution, temporel, géographique.
                <br/><br/>
                
                > Nous avons également été confrontés aux contraintes, notamment techniques, que pouvait engendrer le traitement d'un dataset volumineux (plus d'un million de lignes à la base) : des temps de calcul potentiellement très longs, voire trop lourds pour pouvoir faire tourner certains modèles sur nos ordinateurs personnels. Une difficulté qui nous a amené à faire des choix (limitation du nombre d'observations, appui technique de notre mentor...). Une contrainte qui aurait éventuellement pu être contournée avec l'utilisation d'outils pour le big data, comme Pyspark par exemple (que nous n'avions pas encore abordé dans le cadre de la formation lorsque nous aurions pu l'utiliser).
                <br/><br/>
                
                > En dépit de très nombreux tests et recherches (tant en termes de modèles que d'hyperparamètres), notre meilleur modèle enregistre des performances relativement modestes. Mais celui-ci a néanmoins le mérite d'afficher une interprétabilité assez claire et plutôt logique compte tenu des variables explicatives injectées dans le modèle.
                                                               
                > Quelques pistes pourraient néanmoins permettre ultérieurement d'optimiser notre modèle :

                >   <ul><li>Faire appel à des machines plus puissantes pour pouvoir faire tourner d'autres modèles</li>
                    <li>Utiliser des outils de big data plus performants dans le traitement de datasets volumineux</li>
                    <li>Recueillir d'autres données autour des interventions qui pourraient aider à mieux expliquer le modèle</li>
                """,unsafe_allow_html = True)
                
                
