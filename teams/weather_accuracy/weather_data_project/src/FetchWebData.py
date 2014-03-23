import nltk   
from urllib import urlopen
import Collect

zipcodes = Collect.zipcodeScraper.getZipCodes(91701, 150)

for zipcode in zipcodes:
    try:
        name = zipcode+".txt"
        url = "http://75.140.9.154/Collection/WebDataHandler/"+name    
        html = urlopen(url).read()    
        raw = nltk.clean_html(html)  
        f = open(name,"w")
        f.write(raw)
        f.close
    except:
        print name,'not fetch'