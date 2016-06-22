from time import strptime
import re

def monthformat(a): 

	def monthconvert(monthy): 
		return(strptime(monthy, '%b').tm_mon)

	b = re.split('\,', a)
	year = b[1].replace(" ", "")
	c = re.split('\s+', b[0])
	day = c[1]

	if (int(day) < 10): 
		day = '0' + day

	month = monthconvert(c[0])
	if(int(month) < 10):
		month = '0' + str(month)

	datestring = year +'-' + month + '-' + day

	return(datestring)

print(monthformat("Apr 13, 1994"))