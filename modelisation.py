# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 14:12:44 2021

@authors: Elora, Marie, Nicolas
"""

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from joblib import load

import streamlit as st


@st.cache
def get_model(choix, X_train, y_train, X_test, y_test):

    options = ['Regression Logistique', 'KNN', 'Decision Tree']
    if choix == options[0]:
        model = load("models/logreg.joblib")
        
        score = model.score(X_test, y_test)
        
    if choix == options[1]:
        model = load("models/knn.joblib")
        
        score = model.score(X_test, y_test)
        
    if choix == options[2]:
        model = load("models/tree.joblib")
        
        score = model.score(X_test, y_test)
        
    return model, score