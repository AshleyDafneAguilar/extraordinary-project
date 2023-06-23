#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import pandas as pd
import db_config
import mariadb

# DB connector settings
# References https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# For this part of the code

#Connect to MariaDB
try:
    conn = mariadb.connect(
        user = db_config.setting['user'],
        password = db_config.setting['password'],
        host = db_config.setting['host'],
        port = db_config.setting['port'],
        database = db_config.setting['database']
    )

except mariadb.Error as e:
    sys.exit(1)

# Get the cursor
cur = conn.cursor()

# End part of code



# Collect all data from the db
cur.execute("SELECT * FROM Movies;")

# Dictionary for the data frame creation
dictDf = {'id':[], 'original_language':[], 'title': [], 'vote_average': [], 'vote_count': [] } 



# we iterate over each tuple (row) in the database

for data in cur:

	# data  is a tuple (database row) with 'len(dictDf.keys()' attributes (database columns)
	for i, llave in enumerate(dictDf.keys()):
		# Appending data to the data frame
	
		dictDf[llave].append(data[i])
	

# Creating the data frame
df = pd.DataFrame(dictDf)


# We add more information

#Dictionary for the data frame creation
gender = {'Acción': [], 'Animación': [], 'Aventura': [], 'Bélica':[], 'Ciencia ficción': [], 'Comedia': [], 
	'Crimen':[],'Documental': [], 'Drama': [], 'Familia': [], 'Fantasía': [], 'Historia': [], 'Misterio': [],
	'Música': [], 'Película de TV': [], 'Romance':[], 'Suspenso': [], 'Terror': [], 'Western': []}


# We get the genres of each movie.

gender_list = [['Comedia', 'Drama', 'Romance'], ['Aventura', 'Fatasía', 'Acción'], ['Animación', 'Familia', 'Fantasía'],
              ['Acción','Crimen','Drama', 'Suspenso'], ['Crimen', 'Drama'], ['Crimen', 'Drama'], ['Crimen', 'Drama'],
              ['Drama'], ['Western'], ['Crimen', 'Drama', 'Fantasía'], ['Crimen', 'Suspenso'], ['Crimen', 'Drama'],
              ['Drama', 'Romance'], ['Comedia', 'Drama', 'Romance'], ['Animación', 'Drama', 'Romance'],
              ['Comedia', 'Drama', 'Suspenso'], ['Acción', 'Animación', 'Aventura', 'Ciencia ficción'], 
              ['Acción', 'Animación', 'Aventura', 'Drama'], ['Comedia', 'Fantasía']]


# We introduce the information to the dictionary

for i, info in enumerate(gender_list):

	for i, key in enumerate(gender.keys()):
	
	
		# 1 if it is of gender "key"
		# 0 if it is not of that gender
		
		if key in [x for x in gender.keys() if not x in info]:
			
			gender[key].append(0)
		
		elif key in info:
		
			gender[key].append(1)


# Creating the data frame
df_gender = pd.DataFrame(gender)

# We concatenate the two dataframes df + df_gender
dataset = pd.concat([df, df_gender], axis=1)



# We declare the route
PATH = './dataset/'

# Data frane to csv
dataset.to_csv(PATH + "themovietopdb.csv")

# Close Connection
conn.close()
