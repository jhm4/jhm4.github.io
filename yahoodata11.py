import sqlite3
import requests 
import re 

#this program takes in data from Yahoo Finance Canada website in html form and accomodates it into an SQLite table. 

base_url = "https://ca.finance.yahoo.com/q/hp"

symb = input ("Symbol: ")

#start and end dates as strings
start_date = input ("Start-date (i.e 03-24-2004) : ")
end_date = input ("End-date (i.e 04-24-2004): ")
interval_period = input ("'d' for daily data, 'w' for weekly, or 'm' for monthly: " )

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

#grab the text online 
t = requests.get(base_url, params = specifications).text 


#create the SQLite taable I will be putting my data on. 

#establish a connection object to database 
identity = symb + "v" + start_date + "v" + end_date + "v" + interval_period
conn = sqlite3.connect(identity + ".db")

#build a cursor object and call its execute() method to perform SQL commands
c = conn.cursor()

c.execute('BEGIN TRANSACTION')
c.execute('''CREATE TABLE Stocks (Date text, Open real , High real, Low real, Close real, Volume integer, Adj Close real, Dividend real, Split text)''')
#conn.commit()

#here I will introduce 3 functions that take in 3 different types of text data and insert it into the table. 


#Function 1 takes in a normal data point for a day. 
def cleardata(b, conn, c): 
	#split data to have it as entries on a list 

	data4 = re.split('\</td><td class="yfnc_tabledata1" align="right">', b)

	#clean up the last element 

	last = data4[len(data4) - 1]

	lastlist = re.split('\</td>', last)
	data4[len(data4) - 1] = lastlist[0]
	
	#Insert row of data 
	c.execute("INSERT INTO Stocks VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)", data4)



#Function 2 takes in a stock split data point 
def stocksplit(b, conn, c): 


	#extract the date in data4o[0], and the ratio in data4o[1], ultimately. 
	data4o = re.split('\</td><td class="yfnc_tabledata1" align="center" colspan="6">', b)
	date = data4o[0]
	d = re.split('\ Stock Split', data4o[1])
	ratio = d[0]
	ratio = re.sub(r'\s+', '', ratio)

	#now insert the info in table

	c.execute("UPDATE Stocks SET Split = ? WHERE Date = ?", (ratio, date))


#Function 3 takes in a dividend data point 
def dividend(b, conn, c): 


	#extract the date in data4p[0] and the dividend in data4p[1], ultimately 

	date4p = []
	data4p = re.split('\</td><td class="yfnc_tabledata1" align="center" colspan="6">', b)
	date = data4p[0]
	dividendlist = re.split('\ Dividend', data4p[1])
	dividend = dividendlist[0]

	#insert the info in table 

	c.execute("UPDATE Stocks SET Dividend = ? WHERE Date = ?", (dividend, date))


#Now that I have the 3 Functions needed to insert every type of data, I will have my datamassage() function that uses them. 
#Note that datamassage() does the most rudimentary managing of the html text obtained from online. For further work it refers to
#one of the three functions. 


def datamassage(t, conn, c):

	a = re.split('\>Adj Close*', t)
	# list a has two components. 

	b = re.split('\colspan="7"', a[1])

	list = re.split('\class="yfnc_tabledata1" nowrap align="right">', b[0])

	#get rid of the first item in list 

	list = list[1:] 

	for i in list: 
		
		#if align="right" is found I will clean item as a cleardata point. 
		if re.search('"right"', i) != None: 
			cleardata(i, conn, c)
	
		#if 'Stock' is found I will clean item as a split data point. 
		elif re.search('\Stock', i) != None:
			stocksplit(i, conn, c)
		
		#else I will treat it as a dividend data point. 
		else:
			dividend(i, conn, c)


#back to my text retrieved from yahoo finance. 

datamassage(t, conn, c)


#after this first call, I need to search the other pages in yahoo finance see if there is remaining information... 

x = 66

while True:
	specificationsnext = {"s" : symb, "a" : start_datelist[0] , "b" : start_datelist[1], "c" : start_datelist[2], "d" : end_datelist[0], "e" : end_datelist[1] , "f" : end_datelist[2], "g" : interval_period, "z" : "66", "y"  : str(x)}
	r = requests.get(base_url, params = specificationsnext)
	s = r.text 

	#is there a way to make this statement more logical? More logical for the user? 
	#if this message is not found anywhere in the html text then add the data to the SQLite table and continue searching. 
	if re.search('\Historical quote data is unavailable for the specified date range.', s) == None : 
		datamassage(s, conn, c)
		x = x + 66

	else: 
		break 

#commit changes. 
conn.commit()
#c.execute('COMMIT') <--- did not need this . 
#close connection to SQLite table, finally. 
conn.close()



#feedback: to retrieve data for 10 years, the program took about 5 minutes to run, almost 10. So before I commit the changes I will 
#include a couple of moves in one transaction 
