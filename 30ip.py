
# # import geo 
# import geopandas as geo
# ip=geo.getIP()
# print(ip)


# country=geo.getCountry(ip,'plain')
# print(country)



# country=geo.getCountry(ip,'json')
# print(country)


# geoData=geo.getGeoData(ip)
# print(geoData)


# ptrData=geo.getPTR(ip)
# print(ptrData)


# geo.showIpDetails('216.239.32.0')
# geo.showCountryDetails('216.239.32.0')






import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance



# def printDetails(ip):
#     res = DbIpCity.get(ip, api_key="free")
#     print(res)
#     print(f"IP Address: {res.ip_address}")
#     print(f"Location: {res.city}, {res.region}, {res.country}")
#     print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


# # ip_add = input("Enter IP: ")  # 198.35.26.96
# # printDetails(ip_add)  
# url ='https://blog.code4me.co.in/'  # www.youtube.com
# ip_add = socket.gethostbyname(url)
# printDetails(ip_add)



# import requests

# # sample API address
# ip = '192.168.0.178'

# # parameters to retrieve from API
# params = ['query', 'status', 'country', 'countryCode', 'city', 'timezone', 'mobile']

# # make the response 
# resp = requests.get('http://ip-api.com/json/' + ip, params={'fields': ','.join(params)})

# # read response as JSON (converts to Python dict)
# info = resp.json()

# # display the response
# print(info)

import requests
import json

# IP address to test
ip_address = '127.0.1.1'


request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result  = json.loads(result)
print(result)


## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")