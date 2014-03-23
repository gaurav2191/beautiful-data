"""
First line of the text file will be where is the data from, city,state, lat, long
After the first line, the rest will be data collected. Everyline will be an update
We will collect data every 2 hours
The other lines will be like, all separated by comma
time of data collected, time when the data is updated in the website, sunrise, sunset,
temp,condition,huminity,pressure,rising,visibility, wind chill,direction,speed
"""
import os
import time
import WebWeatherCollection as wwc
#Yeah, I know, I need to work on the naming convention
data = {}

def saveDataIntoText(name):
    try:
      text_file = open(getFileName(name), "a")
      text_file.write(time.strftime("%c")+","+data['condition']['date'][-24:]+","+data['astronomy']['sunrise']+","+data['astronomy']['sunset']+","+data["condition"]["temp"]+","+data["condition"]["text"]+","+data["atmosphere"]["humidity"]+","+data["atmosphere"]["pressure"]+","+data["atmosphere"]["rising"]+","+data["atmosphere"]["visibility"]+","+data["wind"]["chill"]+","+data["wind"]["direction"]+","+data["wind"]["speed"]+"\n")
      text_file.close()
    except :
      print "Error on the zipcode " ,name
    
def readSourceFile(name,date):
    tmp = []
    hum = []
    pre = []
    f = open(getFileName(name), "r")
    for lines in f.readlines():
      line = lines.split(',')
      if date in line[0]:
        tmp.append(line[2])
        hum.append(line[3])
        pre.append(line[10])
    return tmp
      

def readTextFile(name):
    dataList = []
    
    firstL = {}
    firstL['location'] = {}
    f = open(getFileLocation(name), "r")
    
    firstLine = f.readline().split(',')
    firstL['location']['provider'] = firstLine[0]
    firstL['location']['city'] = firstLine[1]
    firstL['location']['state'] = firstLine[2]
    firstL['location']['latitud'] = firstLine[3]
    firstL['location']['longitud'] = firstLine[4]
    firstL['location']['distancefromsource'] = firstLine[8]
    dataList.append(firstL)
    
    for lines in f.readlines():
        rData = {}
        rData['condition'] = {}
        rData['astronomy'] = {}
        rData['wind'] = {}
        line = lines.split(',')
        rData['condition']['dateCollected'] = line[0]
        rData['condition']['dateUpdated'] = line[1]
        rData['astronomy']['sunrise'] = line[2]
        rData['astronomy']['sunset'] = line[3]
        rData['condition']['temp'] = line[4]
        rData['condition']['text'] = line[5]
        rData['condition']['huminity'] = line[6]
        rData['condition']['preassure'] = line[7]
        rData['condition']['rising'] = line[8]
        rData['condition']['visibility'] = line[9]
        rData['wind']['chill'] = line[10]
        rData['wind']['direction'] = line[11]
        rData['wind']['speed'] = line[12][:-1]
        dataList.append(rData)
        

    f.close()
#Yeah.... It return a list of dictionaries with dictionary
    return dataList
    
def makeNewTextFile(name):
    nameofData = getFileName(name)
    if(os.path.exists(nameofData)):
#        print "File Already Exist"
        saveDataIntoText(name)
    else:
        open(nameofData,"w")
        makefirstline(name)
        saveDataIntoText(name)
#        print "File Created"

def makefirstline(name):
    try:
      text_file = open(getFileName(name), "a")
      text_file.write(data["title"][:14]+","+data["title"][17:-4]+","+data["title"][-2:]+","+data["geo"]["lat"]+","+data["geo"]["long"]+"\n")
      text_file.close()
    except:
      print 'Error making the file ', name

def getFileName(name):
    workingpath = os.getcwd()[:-3]
    nameofData = workingpath+name+".txt"
    return nameofData
  
def getFileLocation(name):
    workingpath = os.getcwd()[:-3]
    nameofData = workingpath+"web_data\\"+name+".txt"
    return nameofData

def main(zipcode):
    global data
    print 'Collecting Data from ', zipcode
    data = wwc.getWeatherData(zipcode)
    makeNewTextFile(zipcode)
    
    
#tes = main('91780')
tes = wwc.getWeatherData('91780')