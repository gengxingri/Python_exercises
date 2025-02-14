#The program will prompt for a location, contact a web service and retrieve JSON 
#for the web service and parse that data, and retrieve the first place_id from the JSON. 
#A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://py4e-data.dr-chuck.net/json?

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: 
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

  
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    place_id = js['results'][0]['place_id']
    print(place_id)
