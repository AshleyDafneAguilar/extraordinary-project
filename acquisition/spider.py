#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import mariadb
import sys
import requests
import db_config
from colorama import Fore
from time import sleep
import json



# Connect to MariaDB

def main(url: str):

	print(Fore.RED + 'Connecting to the database...')
	
	try:
		conn = mariadb.connect(
		user = db_config.setting['user'],
		password = db_config.setting['password'],
		host = db_config.setting['host'],
		port = db_config.setting['port'],
		database = db_config.setting['database']
		)
	
		
		
	except mariadb.Error as e:
	
		print(f"Error connecting to MariaDB Platform: {e}")
		sys.exit(1)
	
	
	# Get the cursor
	cur = conn.cursor()

	# End part of code

	print(Fore.GREEN + 'Connection successfully completed')
	
	
	print(Fore.BLUE + 'Getting data...')
	
	# Check the response of the get function
	response_get_data = get_data(url)
	
	# We finish the spider if we do not have data
	if response_get_data == None:
		return
		
	# If we have data, we assign it to the data variable
	
	data = response_get_data
	
	
	# Save only the results
	dictionary_list = data['results']
	
	
	# We obtain the sql instruction for each data
	for i, dic in enumerate(dictionary_list):
	
		sql_instruction = "INSERT INTO Movies (id, original_language, title, vote_average, vote_count) VALUES " + '(' + str(dic['id']) + ', ' + "'" + str(dic['original_language'])+ "'" + ', ' + "'" + str(dic['title']) + "'" + ', ' + str(dic['vote_average']) + ', ' + str(dic['vote_count']) + ');'
		
		
		# We wait a second to not exceed API time limit
		sleep(1)
		
		
		# References https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
		# For this part of the code
		
		# Insert the information
		
		try:
		
			cur.execute(sql_instruction)
			print(sql_instruction)
			
		except mariadb.Error as e:
		
			continue
			
			
		# End part of code
		
		
	# Commited the insertions on the db
			
	conn.commit()
	print(Fore.GREEN + 'Data successfully obtained')
	
	
	# Close Connection
	conn.close()	
		
	return 

        	
               
def get_data(url: str, attempts = 5):
    response = requests.get(url)
    status_code = response.status_code

    for attempt in range(attempts):

        # References https://oxylabs.io/blog/python-requests
        # For this part of the code
        if status_code == 200:
            data = response.json()
            return data

        else:
            sleep(90)
            response = requests.get(url)
            status_code = response.status_code

        # End part of code
    
    return




if __name__ == '__main__':

	api_key = 'e2f7301d6aa0af870a21056549625d2c'
	url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1"
	#url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=e2f7301d6aa0af870a21056549625d2c&language=en-US&page=1'
	main(url)
