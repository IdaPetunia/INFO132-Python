import json
import urllib.request

url_str = 'http://api.semanticscholar.org/v1/author/1739275'
response = urllib.request.urlopen(url_str)
print(response.status, response.msg)
data=response.read()
charles = json.loads(data)
print(charles)

with open('charles.json', 'w') as file:
 json.dump(charles, file)
