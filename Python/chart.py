import urllib.parse
import urllib.request

from datetime import date

date = date.today()
year_replace = date.year - 5
date2 = date.replace(year = year_replace)


end = str(date)
start = str(date2)

to_append = 'T00:00:00-00'
end = end + to_append
start = start + to_append
print(start)
print(end)

url = 'http://dev.markitondemand.com/Api/v2/InteractiveChart/json'
data = {}

data['Content-Length'] = 25
data['Normalized'] = False
data['EndDate'] = end
data['StartDate'] = start
data['DataPeriod'] = 'Day'
data['DataInterval'] = 7
data['LabelPeriod'] = 'Month'
data['LabelInterval'] = 1
elements = {}
elements['Symbol'] = 'AAPL'
elements['Type'] = 'price'
data['Elements'] = elements


url_values = urllib.parse.urlencode(data)
print(url_values)
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)
the_page = data.read()
print(the_page)