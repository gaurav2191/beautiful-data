import Collect
class Driver():
    def run(self, path):
        print "Reading config.txt file"
        info = Driver.readConfigFile(path)
        source = info[0]
        radius = info[1]
        print "Source zipcode is: " + source
        print "Radius around source is " + radius
        print "Collect data from source weather station start..."
        Collect.getSensorData
        print "Collect data finished"
        print "Gathering zipcodes from around source with radius " + str(radius)
        zipcodes = Collect.zipcodeScraper.getZipCodes(source, radius)
        print zipcodes
        print "Zipcode gathering complete"
        print "Getting weather data for each zipcode..."
        for zipcode in zipcodes:
            Collect.getWeatherData(zipcode)
            
    @staticmethod        
    def readConfigFile(path):
        info = []
        count = 0
        f = open(path, 'r')
        for line in f:
            stringArray = line.split()
            info.insert(count, stringArray[2])
            count += 1
        f.close()
        return info
#Driver()
