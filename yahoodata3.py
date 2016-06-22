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


# this function takes in the messy text data retrieved from web (t) and saves the numerical data necessary.
# the data is saved in a list form (list)

def datamassage(t, list): 
	del list[:]   # make sure I have a clear list. 
	string = ""
	datalist = re.split('\class="yfnc_tabledata1"', t)
	i = 1 
	#The items 1 - len(var2) - 2 are the items of interest.

	while i < len(datalist) - 1 : 
		list.append(datalist[i])
		string = string + datalist[i]
		i = i + 1

	return string


texts = []
u = requests.get(base_url, params = specifications).text 
data = []

###############################################################
print()

massaged = datamassage(u, data)

while True:
    split = re.split(" nowrap align=\"right\">", massaged, maxsplit=1)
    if not len(split) == 2:
        break
    massaged = split[1]
    search = re.search("</td><td", massaged)
    print(search.string[:search.start()] + ", ", end="")

    split = re.split("align=\"right\">", massaged, maxsplit=1)
    massaged = split[1]
    search = re.search("</td><td", massaged)
    print(search.string[:search.start()] + ", ", end ="")

    split = re.split("align=\"right\">", massaged, maxsplit=1)
    massaged = split[1]
    search = re.search("</td><td", massaged)
    print(search.string[:search.start()] + ", ", end ="")

    split = re.split("align=\"right\">", massaged, maxsplit=1)
    massaged = split[1]
    search = re.search("</td><td", massaged)
    print(search.string[:search.start()] + ", ", end ="")

    split = re.split("align=\"right\">", massaged, maxsplit=1)
    massaged = split[1]
    search = re.search("</td><td", massaged)
    print(search.string[:search.start()] + ", ", end ="")

    split = re.split("align=\"right\">", massaged, maxsplit=1)
    massaged = split[1]
    search = re.search("</td><td", massaged)
    string = search.string[:search.start()]
    string = re.sub(",", "", string)
    print(string + ", ", end ="")

    split = re.split("align=\"right\">", massaged, maxsplit=1)
    massaged = split[1]
    search = re.search("</td></tr", massaged)
    print(search.string[:search.start()], end ="")
    print()

    #split = re.split("</td></tr><tr><td ", massaged, maxsplit=1)
    #massaged = split[1]
    


###############################################################
texts.append(datamassage(u, data))



#if page contains relevant information I want to append the text to my texts[]
#and continue travelling to subsequent pages. If it doesn't, then stop. 

x = 66

while True:
	specificationsnext = {"s" : symb, "a" : start_datelist[0] , "b" : start_datelist[1], "c" : start_datelist[2], "d" : end_datelist[0], "e" : end_datelist[1] , "f" : end_datelist[2], "g" : interval_period, "z" : "66", "y"  : str(x)}
	r = requests.get(base_url, params = specificationsnext)
	s = r.text 

	if re.search('\Historical quote data is unavailable for the specified date range.', s) == None : 
		data2 = []
		texts.append(datamassage(s, data2))
		x = x + 66
	else: 
		break


# I have all the data in my texts[] list. I just need to iterate through it and save it on the file. 

#file = open(filename, 'w')

#for text in texts: 

#	for listitem in text: 
#		file.write(listitem)

#file.close()