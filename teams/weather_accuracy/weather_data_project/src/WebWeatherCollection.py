"""
This require you to get the pywapi library in order to execute this code.
To download the library go to ->
https://code.google.com/p/python-weather-api/
-> Downloads -> Downloads
And download the pywapi-0.3.7.tar.gz and install it
If you are using linux, download the other one
"""

#hi
#hola
#91701 The area Code for Rancho Cucamonga

import pywapi
import pprint
def getWeatherData(zipcode):
    pp = pprint.PrettyPrinter(indent=4)
    
    #pp.pprint(result)
    
    #data that will be used in the code, location that will look into and unit system
#    location = 'Rancho Cucamonga'
    unitsys = 'imperial'
    
#    location = str(pywapi.get_location_ids(location))
#    location_id = location[3:11]
    
    rs = pywapi.get_weather_from_yahoo(zipcode, unitsys)
#    No need to print for now
#    print pp.pprint(rs)
    
    #test = str(rs['location']['city'])
    return rs
