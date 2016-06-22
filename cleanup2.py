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

def stocksplit(b): 

	#extract the date in data4o[0], and the ratio in data4o[1], ultimately. 
	data4o = re.split('\</td><td class="yfnc_tabledata1" align="center" colspan="6">', b)
	ratio = re.sub('\Stock Split</td></tr><tr><td', "", data4o[1])
	#ratio = re.sub(" ", "", ratio)
	ratio.strip()
	data4o[1] = ratio

	print(data4o[0])
	print('\n' '\n')
	print(data4o[1])




stocksplit(list[46])
