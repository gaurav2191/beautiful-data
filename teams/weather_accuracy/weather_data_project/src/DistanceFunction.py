import webDataHandler as wd
import Collect
import math
import math


def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc
    
def getResultinMiles(arc):
  return arc * 3960.0

def getResultinKm(arc):
  return arc * 6373.0
  
  
  

def getDataForMap(zipcode,radius,date):
  #zipcode:String radius:int day:String <25 Feb 2014>
  #name lat long acc
  wholedata = {}
  alldis = {}
  sd = wd.readTextFile('91701')
  slon = float(sd[0]['location']['longitud'])
  slat = float(sd[0]['location']['latitud'])
  cname = sd[0]['location']['city']

  zipcodes = Collect.ZipcodeScraper.getZipCodes(zipcode, radius)
  asd = 0;
  for zipcode in zipcodes:
    
    d = wd.readTextFile(zipcode)
    data = {}
    k = 0
    for i in range (len(d)-1):
      #'28 Feb 2014'
      if date in d[i+1]['condition']['dateUpdated']:
        data[k] = d[i+1]['condition']['temp']
        k = k+1
        
        
    lon = float(d[0]['location']['longitud'])
    lat = float(d[0]['location']['latitud'])
    dis = df.getResultinMiles(df.distance_on_unit_sphere(slat, slon, lat, lon))
      
    for j in range (len(data)):
      data[j] = float(data[j])
        
    wholedata[asd] = data
    alldis[asd] = dis
    asd = asd+1
    
  return wholedata, alldis
  
  def getData():
  wholedata = {}
  alldis = {}
  sd = wd.readTextFile('91701')
  slon = float(sd[0]['location']['longitud'])
  slat = float(sd[0]['location']['latitud'])

  zipcodes = Collect.ZipcodeScraper.getZipCodes('91701', 10)
  asd = 0;
  for zipcode in zipcodes:
    
    d = wd.readTextFile(zipcode)
    data = {}
    k = 0
    for i in range (len(d)-1):

      if '28 Feb 2014' in d[i+1]['condition']['dateUpdated']:
        data[k] = d[i+1]['condition']['temp']
        k = k+1
        
        
    lon = float(d[0]['location']['longitud'])
    lat = float(d[0]['location']['latitud'])
    dis = getResultinMiles(distance_on_unit_sphere(slat, slon, lat, lon))
      
    for j in range (len(data)):
      data[j] = float(data[j])
        
    wholedata[asd] = data
    alldis[asd] = dis
    asd = asd+1
    
  return wholedata, alldis

sd = wd.readTextFile('91701')
slon = float(sd[0]['location']['longitud'])
slat = float(sd[0]['location']['latitud'])
cname = sd[0]['location']['city']
  