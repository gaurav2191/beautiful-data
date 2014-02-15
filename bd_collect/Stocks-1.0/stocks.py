import urllib
import json
import re 
import os


symbolslist = open("symbols.txt").read()
symbolslist = symbolslist.split("\n")
dirpath = "stocks_data"
if not os.path.exists(dirpath):
	os.makedirs(dirpath)
for symbol in symbolslist:
	myfile = open("stocks_data/"+symbol + ".txt", "w+")
	myfile.close()
	htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
	data = json.load(htmltext)
	datapoints = data["data_values"]
	
	myfile = myfile = open("stocks_data/"+symbol + ".txt", "a")
	for point in datapoints:
		myfile.write(str(symbol +","+ str(point[0])+","+str(point[1]) + "\n" ))
	myfile.close()	