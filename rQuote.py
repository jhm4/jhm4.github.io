import requests

url = 'http://dev.markitondemand.com/Api/v2/Quote/xml'
data = {}
data['Content-Length'] = 25
data['symbol'] = 'AAPL'

r = requests.get(url, params = data)

print()
print(r.text)