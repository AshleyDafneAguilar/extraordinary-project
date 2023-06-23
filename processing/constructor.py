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

# We declare the route
PATH = './dataset/'

# Data frane to csv
df.to_csv(PATH + "themoviedb.csv")

# Close Connection
conn.close()
