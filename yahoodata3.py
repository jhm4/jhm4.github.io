import sqlite3
import requests 
import re 


base_url = "https://ca.finance.yahoo.com/q/hp"

#prompts the user for symbol, start date and end date. 


symb = input ()

#start and end dates as strings
start_date = input ()
end_date = input ()
interval_period = input ()

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

def process_Time(var1):
    to_Return = ""
    months = {}
    months["Jan"] = "01"
    months["Feb"] = "02"
    months["Mar"] = "03"
    months["Apr"] = "04"
    months["May"] = "05"
    months["Jun"] = "06"
    months["Jul"] = "07"
    months["Aug"] = "08"
    months["Sep"] = "09"
    months["Oct"] = "10"
    months["Nov"] = "11"
    months["Dec"] = "12"

    var1 = re.sub(",", "", var1)
    split = re.split(" ", var1)

    to_Return = to_Return + split[2] + "-"
    to_Return = to_Return + months[split[0]] + "-"
    if len(split[1]) < 2:
        to_Return = to_Return + "0" + split[1]
    else:
        to_Return = to_Return + split[1]
    return to_Return

texts = []
u = requests.get(base_url, params = specifications).text 
data = []

###############################################################
print("Date, Open, High, Low, Close, Volume, Adj Close, Dividend, Stock Split")

massaged = datamassage(u, data)

while True:
    split = re.split(" nowrap align=\"right\">", massaged, maxsplit=1)
    if not len(split) == 2:
        break
    massaged = split[1]
    search = re.search("</td><td", massaged)
    substring = search.string[:search.start()]
    substring2 = process_Time(substring)
    print(substring2 + ", ", end="")

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
            split = re.split(" Dividend", substring)
            substring = split[0]
            print(", " + substring + ", ", end="") # added
        else:
            print(",, ", end="")


        #Check if it's a Stock Split
        searchSpl = re.search(" Stock Split", substring)
        if not searchSpl == None:
            split = re.split(" Stock Split", substring)
            substring = split[0]
            split2 = re.split(":\n            ", substring)
            substring = int(split2[0])/int(split2[1])
            print(str(substring), end="")
       # commented out print(", " + str(substring), end = "")
    else:
        print(",,", end="")
    print()

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
        massaged = datamassage(s, data)
        while True:
            split = re.split(" nowrap align=\"right\">", massaged, maxsplit=1)
            if not len(split) == 2:
                break
            massaged = split[1]
            search = re.search("</td><td", massaged)
            substring = search.string[:search.start()]
            substring2 = process_Time(substring)
            print(substring2 + ", ", end="")

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
                    split = re.split(" Dividend", substring)
                    substring = split[0]
                    print(", " + substring + ", ", end="") # added
                else:
                    print(",, ", end="")

                #Check if it's a Stock Split
                searchSpl = re.search(" Stock Split", substring)
                if not searchSpl == None:
                    split = re.split(" Stock Split", substring)
                    substring = split[0]
                    split2 = re.split(":\n            ", substring)
                    substring = int(split2[0])/int(split2[1])
                    print(str(substring), end="")
            # commented out print(", " + str(substring), end = "")
            else:
                print(",,", end="")
            print()

        texts.append(datamassage(s, data2))
        x = x + 66
    else: 
        break
