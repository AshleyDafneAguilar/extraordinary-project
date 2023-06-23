#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier


# Load training data

PATH = './dataset/'
data = pd.read_csv(PATH + 'themovietopdb.csv')


#  We do the cleaning for the training data

df = data.copy()


# We delete Data that we will not use

df.drop('Unnamed: 0', axis = 1, inplace = True)
df.drop('id', axis = 1, inplace = True)
df.drop('original_language', axis = 1, inplace = True)
df.drop('title', axis = 1, inplace = True)
df.drop('vote_count', axis = 1, inplace = True)


# Data partition

y = list(map(str,(df['vote_average'])))
X = df.drop(['vote_average'], axis=1)


# Training

modelo =  DecisionTreeClassifier(criterion = 'entropy')
modelo.fit(X, y)


# Here should go the data entered by the user

# this is just an example

X_pred = pd.DataFrame({'Acción': [0], 'Animación': [1], 'Aventura': [1], 'Bélica':[0], 'Ciencia ficción': [0], 'Comedia': [0], 
          'Crimen':[1],'Documental': [1], 'Drama': [1], 'Familia': [0], 'Fantasía': [0], 'Historia': [0], 'Misterio': [0],
          'Música': [1], 'Película de TV': [0], 'Romance':[0], 'Suspenso': [0], 'Terror': [1], 'Western': [0]})


y_pred = str(modelo.predict(X_pred)[0])


# Save prediction

with open(PATH + 'vote_average.txt', 'w') as f:
    f.write(y_pred)








