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

def cleardata(b, conn, c): 
	#split data to have it as entries on a list 

	data4 = re.split('\</td><td class="yfnc_tabledata1" align="right">', b)

	#clean up the last element 

	last = data4[len(data4) - 1]

	lastlist = re.split('\</td>', last)
	data4[len(data4) - 1] = lastlist[0]
	
	#Insert row of data 
	c.execute("INSERT INTO Stocks VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)", data4)

	#save (commit) the changes 
	conn.commit()
	#conn.close()  # not sure if closing it every time is the most efficient way of doing this 


def stocksplit(b, conn, c): 


	#extract the date in data4o[0], and the ratio in data4o[1], ultimately. 
	data4o = re.split('\</td><td class="yfnc_tabledata1" align="center" colspan="6">', b)
	date = data4o[0]
	d = re.split('\ Stock Split', data4o[1])
	ratio = d[0]
	ratio = re.sub(r'\s+', '', ratio)

	#now insert the info in table

	c.execute("UPDATE Stocks SET Split = ? WHERE Date = ?", (ratio, date))
	conn.commit()



def dividend(b, conn, c): 


	#extract the date in data4p[0] and the dividend in data4p[1], ultimately 

	date4p = []
	data4p = re.split('\</td><td class="yfnc_tabledata1" align="center" colspan="6">', b)
	date = data4p[0]
	dividendlist = re.split('\ Dividend', data4p[1])
	dividend = dividendlist[0]

	#insert the info in table 

	c.execute("UPDATE Stocks SET Dividend = ? WHERE Date = ?", (dividend, date))
	conn.commit()


def createtable(conn, c): 
	

	#creates the table, an sqlite command
	c.execute('''CREATE TABLE Stocks (Date text, Open real , High real, Low real, Close real, Volume integer, Adj Close real, Dividend real, Split text)''')
	conn.commit()




#establish a connection object to database 
identity = symb + "v" + start_date + "v" + end_date + "v" + interval_period
conn = sqlite3.connect(identity + ".db")

#build a cursor object and call its execute() method to perform SQL commands
c = conn.cursor()

createtable(conn, c)

for i in list: 


	#if align="right" is found I will clean item as a normal piece of data. 
	if re.search('"right"', i) != None: 
		cleardata(i, conn, c)
	
	#if 'Stock' is found I will clean item as a stock split data
	elif re.search('\Stock', i) != None:
		stocksplit(i, conn, c)
		
	else:
		dividend(i, conn, c)

conn.close()


#file1.close()









#file1 = open('trial29.txt', 'w')



#for item in list: 
	#file1.write(item)
	#file1.write('\n' + '\n')

#file1.close()

  