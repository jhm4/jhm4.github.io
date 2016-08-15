import sqlite3
import requests 
import re 
import time

base_url = "https://ca.finance.yahoo.com/q?s="

f = open('SP500_tickersNAS.txt', 'r')
g = open('SP500_PE3.txt', 'w')
tickers = f.read()
array = str.split(tickers)
length = len(array)
i = 0
while i < length:
	url = base_url+array[i]
	specifications = {}
	t = requests.get(url, params=specifications).text 
	#grab P/E ratio
	search = re.split('P/E ', t)
	t = search[1]
	search = re.split('yfnc_tabledata1\">', t, maxsplit=1)
	t = search[1]
	search = re.split('</td></tr><tr><th scope=', t, maxsplit=1)
	pe = search[0]
	g.write(array[i])
	g.write(" ")
	g.write(pe)
	g.write('\n')
	time.sleep(1)
	print(array[i])
	i = i+1
