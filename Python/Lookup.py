# Call the Lookup API from Markit On Demand for the Search Box

import urllib2

url = 'http://dev.markitondemand.com/Api/v2/Lookup'
response = urllib2.urlopen(url).read()
