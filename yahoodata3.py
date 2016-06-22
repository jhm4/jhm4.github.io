import sqlite3
import requests 
import re 


base_url = "https://ca.finance.yahoo.com/q/hp"

#prompts the user for symbol, start date and end date. 

<<<<<<< HEAD
filename = input ()

symb = input ()

#start and end dates as strings
start_date = input ()
end_date = input ()
interval_period = input ()
=======
filename = input ("File on which you want data saved (i.e output.txt) : ")

symb = input ("Enter desired symbol (i.e MSFT) : ")

#start and end dates as strings
start_date = input ("Enter start-date (i.e 03-24-2004) : ")
end_date = input ("Enter end-date (i.e 04-24-2004): ")
interval_period = input ("Enter 'd' for daily data, 'w' for weekly, or 'm' for monthly: " )
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e

#use RE to put start and end dates as lists 
start_datelist = re.split('\-', start_date)
end_datelist = re.split('\-', end_date)

#modify month values as Yahoo takes 00 to be January and thus 04 to be May and so forth. 

#monthmodify() takes in an integer value indicating month number and returns a string suited to Yahoo. 

def monthmodify (month): 
<<<<<<< HEAD
    if month <= 10: 
        return("0" + str(month - 1))
    else:
        return(str(month - 1))
=======
	if month <= 10: 
		return("0" + str(month - 1))
	else:
		return(str(month - 1))
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e


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
<<<<<<< HEAD
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
=======
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
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e


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
<<<<<<< HEAD
    substring = search.string[:search.start()]
    substring2 = re.sub(",", "", substring)
    print(substring2 + ", ", end="")
=======
    print(search.string[:search.start()] + ", ", end="")
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e

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
<<<<<<< HEAD

    
#Check for a Dividend or Stock Split
    searchTest = re.search("</td></tr><tr><td  nowrap align=\"right\">" + substring, massaged)
    if not searchTest == None:
        split = re.split("</td></tr><tr><td  nowrap align=\"right\">", massaged, maxsplit=1)
        massaged = split[1]
        search1 = re.search("colspan=\"6\">", massaged)
        search2 = re.search("</td></tr><tr><td", massaged)
        substring = search1.string[search1.end():search2.start()]

        #Check if it's a Dividend
        searchDiv = re.search("Dividend", substring)
        if not searchDiv == None:
            split = re.split("Dividend", substring)
            substring = split[0]
        else:
            print(",", end="")


        #Check if it's a Stock Split
        searchSpl = re.search(" Stock Split", substring)
        if not searchSpl == None:
            split = re.split(" Stock Split", substring)
            substring = split[0]
            split2 = re.split(":\n            ", substring)
            substring = int(split2[0])/int(split2[1])
        print(", " + str(substring), end = "")

=======
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e
    print()

    #split = re.split("</td></tr><tr><td ", massaged, maxsplit=1)
    #massaged = split[1]
    


###############################################################
texts.append(datamassage(u, data))



#if page contains relevant information I want to append the text to my texts[]
#and continue travelling to subsequent pages. If it doesn't, then stop. 

x = 66

while True:
<<<<<<< HEAD
    specificationsnext = {"s" : symb, "a" : start_datelist[0] , "b" : start_datelist[1], "c" : start_datelist[2], "d" : end_datelist[0], "e" : end_datelist[1] , "f" : end_datelist[2], "g" : interval_period, "z" : "66", "y"  : str(x)}
    r = requests.get(base_url, params = specificationsnext)
    s = r.text 
    if re.search('\Historical quote data is unavailable for the specified date range.', s) == None : 
        data2 = []
        massaged = datamassage(s, data)
        while True:
            split = re.split(" nowrap align=\"right\">", massaged, maxsplit=1)
            if not len(split) == 2:
                break
            massaged = split[1]
            search = re.search("</td><td", massaged)
            substring = search.string[:search.start()]
            substring2 = re.sub(",", "", substring)
            print(substring2 + ", ", end="")

           # massaged = split[1]
           # search = re.search("</td><td", massaged)
           # print(search.string[:search.start()] + ", ", end ="")

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
            search = re.search("</td><td", massaged)
            string = search.string[:search.start()]
            string = re.sub(",", "", string)
            print(string + ", ", end ="")


            split = re.split("align=\"right\">", massaged, maxsplit=1)
            massaged = split[1]
            search = re.search("</td></tr", massaged)
            print(search.string[:search.start()], end ="")

            #Check for a Dividend or Stock Split
            searchTest = re.search("</td></tr><tr><td  nowrap align=\"right\">" + substring, massaged)
            if not searchTest == None:
                split = re.split("</td></tr><tr><td  nowrap align=\"right\">", massaged, maxsplit=1)
                massaged = split[1]
                search1 = re.search("colspan=\"6\">", massaged)
                search2 = re.search("</td></tr><tr><td", massaged)
                substring = search1.string[search1.end():search2.start()]

                #Check if it's a Dividend
                searchDiv = re.search("Dividend", substring)
                if not searchDiv == None:
                    split = re.split("Dividend", substring)
                    substring = split[0]
                else:
                    print(",", end="")


                #Check if it's a Stock Split
                searchSpl = re.search(" Stock Split", substring)
                if not searchSpl == None:
                    split = re.split(" Stock Split", substring)
                    substring = split[0]
                    split2 = re.split(":\n            ", substring)
                    substring = int(split2[0])/int(split2[1])
                print(", " + str(substring), end = "")

            print()

        texts.append(datamassage(s, data2))
        x = x + 66
    else: 
        break
=======
	specificationsnext = {"s" : symb, "a" : start_datelist[0] , "b" : start_datelist[1], "c" : start_datelist[2], "d" : end_datelist[0], "e" : end_datelist[1] , "f" : end_datelist[2], "g" : interval_period, "z" : "66", "y"  : str(x)}
	r = requests.get(base_url, params = specificationsnext)
	s = r.text 

	if re.search('\Historical quote data is unavailable for the specified date range.', s) == None : 
		data2 = []
		texts.append(datamassage(s, data2))
		x = x + 66
	else: 
		break
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e


# I have all the data in my texts[] list. I just need to iterate through it and save it on the file. 

#file = open(filename, 'w')

#for text in texts: 

<<<<<<< HEAD
#   for listitem in text: 
#       file.write(listitem)
=======
#	for listitem in text: 
#		file.write(listitem)
>>>>>>> f70d70a6186e07a947d4ceaa91aebe3a0a4f432e

#file.close()