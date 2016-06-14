import urllib.request

req = urllib.request.Request('http://dev.markitondemand.com/Api/v2/Lookup')
with urllib.request.urlopen(req) as response:
   the_page = response.read()

print(the_page)