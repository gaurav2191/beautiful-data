#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2
import pydoop.hdfs as hdfs

cmd = raw_input('input URL : ')
response = urllib2.urlopen(cmd);
html = response.read()
soup = BeautifulSoup(html)

''' for open the file '''
outputFile = open("/home/suren/Documents/Workspace/Python/BigData/out.txt", "w");
text_file = open("/home/suren/Documents/Workspace/Python/BigData/techList.txt",'r')
line = text_file.read().split(':')

outputLine = "";
''' for get all the links '''
for anchor in soup('a'):
    if "/careers/department" in anchor.get('href'):
        career_link = "https://www.facebook.com"+anchor.get('href')
        response = urllib2.urlopen(career_link);
        html = response.read()
        soup2 = BeautifulSoup(html)
        
        ''' for get the data '''
        outputLine += str()
        print("- Job Title -")
        print("     " +soup2.h3.get_text())
        print("- Job Skills -")
        for c in soup2.find_all("span"):
            if c.parent.parent.parent.previous_sibling != None:
                if c.parent.parent.parent.previous_sibling.string == "Requirements":
                    for word in line:
                        if word in c.get_text():
                            print("     " + word + " : " + c.get_text() )
        print("---------------------------------------------------------")
        
        
        
        
text_file.close()




    