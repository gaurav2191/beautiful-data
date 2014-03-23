import webDataHandler as wdh
import Collect
import os


def getwebdataavg(zipcode,radius,date):
  web = []
  distance = []
  name = []
  lat = []
  lon = []
  dic = {}
  zipcodes = Collect.ZipcodeScraper.getZipCodes(zipcode, radius)
  for zipcode in zipcodes:
    try:
      accuracy = 0.0
      tmpdata = []
      totalnumber = 0
      d = wdh.readTextFile(zipcode)
      asd = 1
      if float(d[0]['location']['distancefromsource']) < 180:
        distance.append(d[0]['location']['distancefromsource'])
      else:
        distance.append(0)
      for j in range (len(d)-1):
        if(date in d[asd]['condition']['dateUpdated']):
          tmpdata.append(d[asd]['condition']['temp'])
          
        asd += 1
        
      name.append(d[0]['location']['city'])
      lon.append(d[0]['location']['longitud'])
      lat.append(d[0]['location']['latitud'])
        
      for k in range (len(tmpdata)):
        accuracy = accuracy + float(tmpdata[totalnumber])
        totalnumber += 1
      ddd = 0

      for a in range (len(distance)):
        distance[ddd] = float(distance[ddd])
        ddd += 1
      average = accuracy/totalnumber
#  print average
      web.append(average)
      
      print zipcode, " read in"
    except:
      print zipcode, " didnt read in"
    
    dic['name']=name
    dic['lon']=lon
    dic['lat']=lat
  return web , distance , dic , zipcodes

def readsensordata(filename):
  d = wdh.readSourceFile(filename,'09/03/14')
  accuracy = 0
  index = 0
  for i in range (len(d)):
    accuracy = accuracy + float(d[index])
    index += 1
  average = accuracy / index
  return average
  
def getaccuracy():
  x = readsensordata('Mar14log')
  y,distance,dic,zipcodes = getwebdataavg('91701',120,'09 Mar 2014')
  index = 0
  avg = []
  for i in y:
    avg.append(abs((y[index]-x)/x)*-100)
    index +=1
  return avg, distance, dic , zipcodes
  
def writeOutData():
  nameofData = getFileName('data')
  f = open(nameofData,"w")
  a,b,data,z = getaccuracy()
  for i in range(len(data['name'])):
    f.write(str(data['name'][i]) + "," + str(data['lat'][i])  + "," +  str(data['lon'][i])  + "," +  str(a[i]) + "," + str(b[i])+","+str(z[i])+"\n")
  f.close
  

def getFileName(name):
  workingpath = os.getcwd()[:-3]
  nameofData = workingpath+name+".txt"
  return nameofData
  
writeOutData()