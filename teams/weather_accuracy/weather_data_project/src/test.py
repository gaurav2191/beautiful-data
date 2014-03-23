import webDataHandler as wdh
import Collect


def getwebdataavg():
  web = []
  zipcodes = Collect.zipcodeScraper.getZipCodes(91701, 50)
  for zipcode in zipcodes:
    try:
      accuracy = 0.0;
      tmpdata = []
      totalnumber = 0
      d = wdh.readTextFile(zipcode)
      asd = 1
      for j in range (len(d)-1):
        if('09 Mar 2014' in d[asd]['condition']['dateUpdated']):
          tmpdata.append(d[asd]['condition']['temp'])
        asd += 1
      for k in range (len(tmpdata)):
        accuracy = accuracy + float(tmpdata[totalnumber])
        totalnumber += 1
        
      average = accuracy/totalnumber
#  print average
      web.append(average)
    except:
      print zipcode, " has some errors"
    
  return web

def readsensordata():
  d = wdh.readSourceFile('Mar14log')
  accuracy = 0
  index = 0
  for i in range (len(d)):
    accuracy = accuracy + float(d[index])
    index += 1
  average = accuracy / index
  return average
  
def getaccuracy():
  x = readsensordata()
  y = getwebdataavg()
  index = 0
  avg = []
  for i in y:
    avg.append((1-(y[index]-x)/x)*100)
    index +=1
  return avg
  