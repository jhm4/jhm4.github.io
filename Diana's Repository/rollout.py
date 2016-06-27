#have a list of all Dow Jones companies. Will access one entry and will pull out relevant information 

import sqlite3
import requests 

DowJones = {}

DowJones["Apple Inc"] = "AAPL"
DowJones["American Express Company"] = "AXP"
DowJones["The Boeing Company"] = "BA"
DowJones["Caterpillar Inc."] = "CAT"
DowJones["Cisco Systems, Inc."] = "CSCO"
DowJones["Chevron Corporation"] = "CVX"
DowJones["E. I. du Pont de Nemours and Company"] = "DD"
DowJones["The Walt Disney Company"] = "DIS"
DowJones["General Electric Company"] = "GE"
DowJones["The Goldman Sachs Group, Inc."] = "GS"
DowJones["The Home Depot, Inc."] = "HD"
DowJones["International Business Machines Corporation"] = "IBM"
DowJones["Intel Corporation"] = "INTC"
DowJones["Johnson & Johnson"] = "JNJ"
DowJones["JPMorgan Chase & Co."] = "JPM"
DowJones["The Coca-Cola Company"] = "KO"
DowJones["McDonald's Corp."] = "MCD"
DowJones["3M Company"] = "MMM"
DowJones["Merk & Co. Inc."] = "MRK"
DowJones["Microsoft Corporation"] = "MSFT"
DowJones["NIKE, Inc."] = "NKE"
DowJones["Pfizer Inc."] = "PFE"
DowJones["The Procter & Gamble Company"] = "PG"
DowJones["The Travelers Companies, Inc."] = "TRV"
DowJones["UnitedHealth Group Incorporated"] = "UNH"
DowJones["United Technologies Corporation"] = "UTX"
DowJones["Visa Inc."] = "V"
DowJones["Verizon Communications Inc."] = "VZ"
DowJones["Wal-Mart Stores Inc."] = "WMT"
DowJones["Exxon Mobil Corporation"] = "XOM"

search_choice = "The Coca-Cola Company"

# print (search_choice) 
#this marks a couple of errors 

#make a request 

#post 

#this is building the url 
base_url = "http://dev.markitondemand.com/Api/v2/Quote/xml"
extra = {"symbol": DowJones[search_choice], "Content-Length": 25}
#r = requests.post(base_url, search_choice : DowJones[search_choice])

#using the two sections that build the hyperlink that searches
#for specified company, the 'requests' command meshes them 
#together. 
r = requests.get(base_url, params=extra)
print(r.url)
#print(r.text)

#Now I will try to put it in a database

#establish a connection object to database 
#conn = sqlite3.connect('ex1.db')

#build a cursor object and call its execute() method to perform SQL commands
#c = conn.cursor()
#c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')

#Insert row of data 
#c.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35)")

#save (commit) the changes 
#conn.commit()

#conn.close()


