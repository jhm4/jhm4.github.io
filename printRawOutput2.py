import sqlite3
import requests 
import re 
from time import strptime
 
#this program takes in data from Yahoo Finance Canada website in html form and accomodates it into an SQLite table. 

base_url = "https://ca.finance.yahoo.com/q"

symb = input ("Symbol: ")

#start and end dates as strings
#start_date = input ("Start-date (i.e 03-24-2004) : ")
#end_date = input ("End-date (i.e 04-24-2004): ")
#interval_period = input ("'d' for daily data, 'w' for weekly, or 'm' for monthly: " )

#use RE to put start and end dates as lists 
#start_datelist = re.split('\-', start_date)
#end_datelist = re.split('\-', end_date)

#modify month values as Yahoo takes 00 to be January and thus 04 to be May and so forth. 

#monthmodify() takes in an integer value indicating month number and returns a string suited to Yahoo. 

def monthmodify (month): 
	if month <= 10: 
		return("0" + str(month - 1))
	else:
		return(str(month - 1))


#startmonth = monthmodify(int(start_datelist[0]))
#endmonth = monthmodify(int(end_datelist[0]))

#sub in the correct month values as Yahoo needs them 

#start_datelist[0] = startmonth
#end_datelist[0] = endmonth

specifications = {"s" : symb, "ql" : "1"}

#grab the text online 
t = requests.get(base_url, params = specifications).text 

print(t)