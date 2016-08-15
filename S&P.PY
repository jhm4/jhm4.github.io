import sqlite3
import requests 
import re 


base_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

#prompts the user for symbol, start date and end date. 
specifications = {}
t = requests.get(base_url, params = specifications).text 

print(t)
