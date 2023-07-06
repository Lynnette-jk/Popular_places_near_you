
import pandas as pd # for data processing
import folium #for creating maps
import requests #for retreiving Information
from geopy.geocoders import Nominatim #converting address to cordinates
from pandas import json_normalize #converting json to DataFrame 
import requests

CLIENT_ID = '20MSDIPB3TUMEUCH2AXPSNZRB4D2WDFTKR34MQJOVK502TTO' # replace it with your Client id
CLIENT_SECRET = 'VJE4HLLWZZNEPNKGKHKO32NNMTLYOZRULHCLUDOPRC514NBO' # replace it with your client secret
VERSION = '20230704'

address = input("Enter address : ")
pincode = input("Enter postal code : ")

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
if(location == None):
    location = geolocator.geocode(pincode)
    if(location == None):
        print("Address not Found............")
    else:
        print(location)
else:
    print(location)
    truth = input("Is this address nearly accurate.....(y/n) : ")
    if truth == 'n' or truth =='N':
        print("searching based on pincode .........")
        location = geolocator.geocode(pincode)
        if(location == None):
            print("No location found based on pincode..")
        else:    
            print(location)
latitude = location.latitude
longitude = location.longitude
print(latitude,longitude)


radius = input("Enter the radius for searching : ")
Limit = input("enter the Limit for Results to display : ")
#url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius, Limit)

url = "https://api.foursquare.com/v3/places/search?ll={},{}&radius={}&limit={}".format(latitude, longitude, radius, Limit)
url
headers={"Accept":"application/json", "Authorization":"fsq33+c74Isma7+mZ8TumcIFc5NCK6pkUD/Bwty1TY26Vok="}
response = requests.request("GET", url, headers=headers)

print(response.text)
#results = requests.get(url, headers={"Accept":"application/json", "Authorization":"20MSDIPB3TUMEUCH2AXPSNZRB4D2WDFTKR34MQJOVK502TTO"})

#results = requests.get(url).json()
#url provided by your providers.
#print(results.json()['results'][0])

#items=results.json()['results'][0]
#items[0]
#results = results.json()
#items = ['results'][0]


#results = requests.get(url).json()
#results
#items = results['response']['groups'][0]['items']
#items[0]
#print(results)
