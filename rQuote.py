import requests
import re
import time
from datetime import datetime

def get_Price(var1):
    match = re.search("<LastPrice>", var1)
    if not match:
    	return "Error"
    match2 = re.search("</LastPrice>", var1)
    if not match2:
    	return "Error"
    return match.string[match.end():match2.start()]

def get_Time(var1):
    match = re.search("<Timestamp>", var1)
    if not match:
    	return "Error"
    match2 = re.search("</Timestamp>", var1)
    if not match2:
    	return "Error"
    unprocessed = match.string[match.end():match2.start()]
    processed = process_Time(unprocessed)
    return processed

def process_Time(var1):
    to_Return = ""
    months = {}
    months["Jan"] = "1"
    months["Feb"] = "2"
    months["Mar"] = "3"
    months["Apr"] = "4"
    months["May"] = "5"
    months["Jun"] = "6"
    months["Jul"] = "7"
    months["Aug"] = "8"
    months["Sep"] = "9"
    months["Oct"] = "10"
    months["Nov"] = "11"
    months["Dec"] = "12"

    split = re.split(" ", var1)
    to_Return = to_Return + split[5] + "-"
    to_Return = to_Return + months[split[1]] + "-" + split[2]
    to_Return = to_Return + " " + split[3]
    return to_Return

tickers = {}
tickers[0] = "AAPL"
tickers[1] = "AXP"
tickers[2] = "BA"
tickers[3] = "CAT"
tickers[4] = "CSCO"
tickers[5] = "CVX"
tickers[6] = "DD"
tickers[7] = "DIS"
tickers[8] = "GE"
tickers[9] = "GS"
tickers[10] = "HD"
tickers[11] = "IBM"
tickers[12] = "INTC"
tickers[13] = "JNJ"
tickers[14] = "JPM"
tickers[15] = "KO"
tickers[16] = "MCD"
tickers[17] = "MMM"
tickers[18] = "MRK"
tickers[19] = "MSFT"
tickers[20] = "NKE"
tickers[21] = "PFE"
tickers[22] = "PG"
tickers[23] = "TRV"
tickers[24] = "UNH"
tickers[25] = "UTX"
tickers[26] = "V"
tickers[27] = "VZ"
tickers[28] = "WMT"
tickers[29] = "XOM"


total_data = {}

j = 0
while j < 30:
	pd_pairs = {}
	prices = []
	dates = []
	pd_pairs = {'Prices' : prices, 'Dates' : dates}
	total_data[tickers[j]] = pd_pairs
	j += 1

z = 0
while True:
    i = 0
    while i < 30:
        url = 'http://dev.markitondemand.com/Api/v2/Quote/xml'
        data = {}
        data['Content-Length'] = 25
        data['symbol'] = tickers[i]
        r = requests.get(url, params = data)
        output = r.text

        pairs = total_data[tickers[i]]
        price = pairs['Prices']
        times = pairs['Dates']
        price.append(get_Price(output))
        times.append(get_Time(output))
        pairs['Prices'] = price
        pairs['Dates'] = times
        total_data[tickers[i]] = pairs
        print(total_data[tickers[i]])
        i += 1
        time.sleep(30)
    z += 1
	




#print(match.group(0))



