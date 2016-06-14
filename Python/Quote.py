import urllib.parse
import urllib.request

url = 'http://dev.markitondemand.com/Api/v2/Quote/xml'
data = {}
data['Content-Length'] = 25
data['symbol'] = 'AAPL'


url_values = urllib.parse.urlencode(data)
print(url_values)
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)
the_page = data.read()
print(the_page)