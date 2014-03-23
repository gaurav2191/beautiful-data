import zipcodeScraper
import webDataHandler as wdh

def getSensorData():
    f = open('../Jan14log.txt', 'r')
    for line in f:
        print(line)
    f.close()
    
def getZipCodesAroundRadius(source, radius):
    zipcodeScraper.getZipCodes(source, radius)
    
def getWeatherData(zipcode):
    wdh.main(zipcode)
