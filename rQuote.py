import requests
import re
import time
import sys
from datetime import datetime

def get_Price(var1):
    match = re.search("<LastPrice>", var1)
    if not match:
    	return "Error"
    match2 = re.search("</LastPrice>", var1)
    if not match2:
    	return "Error"
    return match.string[match.end():match2.start()]

def get_Volume(var1):
	match = re.search("<Volume>", var1)
	if not match:
	    return "Error"
	match2 = re.search("</Volume>", var1)
	if not match2:
	    return "Error"
	return match.string[match.end():match2.start()]

def get_Cap(var1):
	match = re.search("<MarketCap>", var1)
	if not match:
	    return "Error"
	match2 = re.search("</MarketCap>", var1)
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

def check_Time(times):
    split = re.split(" ", times)
    times = split[1]
    split = re.split(":", times)
    if split[0] == "15" and split[1] == "59" and split[2] == "59":
        return 0
    else: return 1



tickers = {}

tickers[5] = "CKEC" #**
tickers[6] = "SRPT"
tickers[7] = "TK"
tickers[8] = "HRG" #***
tickers[9] = "CJES"
tickers[10] = "CIT"
tickers[11] = "TUP" #***
tickers[12] = "BC" #***
tickers[13] = "FITB"
tickers[14] = "LNC"
tickers[15] = "LUK"
tickers[16] = "TRCO"
tickers[17] = "DOX" #***
tickers[18] = "PDLI"
tickers[19] = "XL"
tickers[20] = "CSCO"
tickers[21] = "DIS"
tickers[22] = "DVN"
tickers[23] = "HD"
tickers[24] = "JPM"
tickers[25] = "PFE"
tickers[26] = "S"
tickers[27] = "V"
tickers[28] = "WMT"
tickers[29] = "XOM"


#total_data = {}

#j = 0
#while j < 30:
#	pd_pairs = {}
#	prices = []
#	dates = []
#	pd_pairs = {'Prices' : prices, 'Dates' : dates}
#	total_data[tickers[j]] = pd_pairs
#	j += 1


while True:
    i = 5
    while i < 30: 
        url = 'http://dev.markitondemand.com/Api/v2/Quote/xml'
        data = {}
        data['Content-Length'] = 25
        data['symbol'] = tickers[i]
        r = requests.get(url, params = data)
        output = r.text
 
       # pairs = total_data[tickers[i]]
       # price = pairs['Prices']
       # times = pairs['Dates']

        times = get_Time(output)
        check = check_Time(times)
        if check == 0:
            time.sleep(63000)
            continue
        print(tickers[i] + ", ", end="")
        print(times + ", ", end="")
        sys.stdout.flush()

        print(get_Price(output) + ", ", end="")
        sys.stdout.flush()

        print(get_Cap(output) + ", ", end="")
        sys.stdout.flush()

        print(get_Volume(output), end="")
        sys.stdout.flush()

        if not i == 29:
            print(", ", end="")
            sys.stdout.flush()
       # price.append(get_Price(output))
       # times.append(get_Time(output))
       # pairs['Prices'] = price
       # pairs['Dates'] = times
       # total_data[tickers[i]] = pairs
       # print(total_data[tickers[i]])
        i += 1
        time.sleep(12)  ### change back to 10
    print()
	




#print(match.group(0))



