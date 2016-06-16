import urllib.parse
import urllib.request
import re
import os

os.environ["QUERY_STRING"] = "file:///C:/Users/John/jhm4.github.io/TestQuote.py?symbol=AAPL"

first = os.environ["QUERY_STRING"]

first_split = re.split('\?', first)
print(first_split)
second_split = re.split('=', first_split[1])
print(second_split)
symbol = second_split[1]
print(symbol)

url = 'http://dev.markitondemand.com/Api/v2/Quote/xml'
data = {}
data['Content-Length'] = 25
data['symbol'] = symbol


url_values = urllib.parse.urlencode(data)
print(url_values)
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)
the_page = data.read()
print(the_page)