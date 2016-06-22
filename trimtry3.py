import sqlite3
import requests 
import re 


base_url = "https://ca.finance.yahoo.com/q/hp"

#prompts the user for symbol, start date and end date. 

filename = input ("File on which you want data saved (i.e output.txt) : ")

symb = input ("Enter desired symbol (i.e MSFT) : ")

#start and end dates as strings
start_date = input ("Enter start-date (i.e 03-24-2004) : ")
end_date = input ("Enter end-date (i.e 04-24-2004): ")
interval_period = input ("Enter 'd' for daily data, 'w' for weekly, or 'm' for monthly: " )

#use RE to put start and end dates as lists 
start_datelist = re.split('\-', start_date)
end_datelist = re.split('\-', end_date)

#modify month values as Yahoo takes 00 to be January and thus 04 to be May and so forth. 

#monthmodify() takes in an integer value indicating month number and returns a string suited to Yahoo. 

def monthmodify (month): 
	if month <= 10: 
		return("0" + str(month - 1))
	else:
		return(str(month - 1))


startmonth = monthmodify(int(start_datelist[0]))
endmonth = monthmodify(int(end_datelist[0]))

#sub in the correct month values as Yahoo needs them 

start_datelist[0] = startmonth
end_datelist[0] = endmonth

specifications = {"s" : symb, "a" : start_datelist[0] , "b" : start_datelist[1],
                   "c" : start_datelist[2], "d" : end_datelist[0], "e" : end_datelist[1] , 
                   "f" : end_datelist[2], "g" : interval_period}

t = requests.get(base_url, params = specifications).text 


a = re.split('\>Adj Close*', t)
	# list a has two components. 

b = re.split('\colspan="7"', a[1])

list = re.split('\class="yfnc_tabledata1" nowrap align="right">', b[0])

#get rid of the first item in list 

list = list[1:]

#function splits based on </td><td class="yfnc_tabledata1" align="right"> 
# accomodates entries in a SQLite table 

#use cleardata(), stocksplit(i), dividend(i) to insert rows into existing database. 


def dividend(b): 


	#extract the date in data4p[0] and the dividend in data4p[1], ultimately 

	date4p = []
	data4p = re.split('\</td><td class="yfnc_tabledata1" align="center" colspan="6">', b)
	date = data4p[0]
	dividendlist = re.split('\ Dividend', data4p[1])
	dividend = dividendlist[0]

	print(date)
	print("la")
	print(dividend)


dividend(list[len(list) - 1])

#magic start date 	is august 7, 2014 for testing. 
