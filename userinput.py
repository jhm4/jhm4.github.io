import re

response = input ("Please name:")
response1 = input ("Age:")
response2 = input ("Enter start-date in month-day-year format (i.e 03-24-2004): " )

date = re.split('\-', response2)


def monthmodify (month): 
	if month <= 10: 
		return("0" + str(month - 1))
	else:
		return(str(month - 1))


startmonth = monthmodify(int(date[0]))


print (startmonth)



