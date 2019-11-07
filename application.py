import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
try:
   url[-4:] == "json"

except: 
   print("Please check your request type")

# Json response
response = urlopen(url)

# Parse response - conver json into python(dictionary)
data = json.load(response)

# Accessing items from dictionary using key( get method)
Response_IP=data.get("ip")
Response_city=data.get("city")
Response_region=data.get("region")
Response_country= data.get("countryi")
Response_org=data.get("orgi")
Response_postal=data.get("postali")

print('Application Response IP detail\n') 
print('Response_IP : {0}'.format(Response_IP))
