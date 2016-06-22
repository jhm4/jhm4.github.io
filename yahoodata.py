#fetches historical data from Yahoo Finance, 

import sqlite3
import requests 
import re 


base_url = "https://ca.finance.yahoo.com/q/hp"

#prompts the user for symbol, start date and end date. 


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

texts = []


texts.append(requests.get(base_url, params = specifications).text)



#if page contains relevant information I want to append the text to my texts[]
#and continue travelling to subsequent pages. If it doesn't, then stop. 

x = 66

while True:
	specificationsnext = {"s" : symb, "a" : start_datelist[0] , "b" : start_datelist[1], "c" : start_datelist[2], "d" : end_datelist[0], "e" : end_datelist[1] , "f" : end_datelist[2], "g" : interval_period, "z" : "66", "y"  : str(x)}
	r = requests.get(base_url, params = specificationsnext)
	s = r.text 

	if re.search('\Historical quote data is unavailable for the specified date range.', s) == None : 
		texts.append(s)
		x = x + 66
	else: 
		break


# I have all the data in my texts[] list. I just need to manage this data. 

target = open('out7.txt', 'w')

for text in texts: 

	var2 = re.split('\class="yfnc_tabledata1"', text)
	var3 = []
	i = 1; 

	#The items 1 - len(var2) - 2 are the items of interest. 
	while i < len(var2) - 1: 
		var3.append(var2[i])
		i = i + 1

	for var in var3: 

		#print data in a text file
		target.write(var)


target.close()
