import sqlite3
import requests 
import re 


base_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

#prompts the user for symbol, start date and end date. 
specifications = {}
t = requests.get(base_url, params = specifications).text 
half = re.split("<td>Pharmaceuticals</td>\n<td><a href=\"/wiki/Florham_Park,_New_Jersey\" title=\"Florham Park, New Jersey\">Florham Park, New Jersey</a></td>", t)
body = half[0]
while re.search("http://www.nasdaq.com/symbol/", body) != None:
	firstsplit = re.split("http://www.nasdaq.com/symbol/", body, maxsplit=1)
	body = firstsplit[1]
	secondsplit = re.split("\">", body, maxsplit=1)
	body = secondsplit[1]
	ticker = secondsplit[0]
	print(ticker)


#print(half[0])
