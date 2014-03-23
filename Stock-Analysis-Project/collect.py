import urllib
import json
import os
import datetime

symbolslist = open("symbols.txt").read()
symbolslist = symbolslist.split("\n")
dirpath = "data_set_1"
if not os.path.exists(dirpath):
	os.makedirs(dirpath)
filename = "Company_Info_numbers"

myfile = open("data_set_1/"+ filename + ".txt", "w+")
myfile.close()

for sym in symbolslist:
	htmltext = urllib.urlopen("http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quote%20where%20symbol%20in%20(%22"+sym+"%22)&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")
	data = json.load(htmltext)
	if len(data["query"]["results"]["quote"]) != None:
		if len(data["query"]["results"]["quote"]) == 14:
			cname = data["query"]["results"]["quote"]["Name"]
			symbol = data["query"]["results"]["quote"]["symbol"]
			avgdvol = data["query"]["results"]["quote"]["AverageDailyVolume"]
			change = data["query"]["results"]["quote"]["Change"]
			daylow = data["query"]["results"]["quote"]["DaysLow"]
			dayhigh = data["query"]["results"]["quote"]["DaysHigh"]
			yearlow = data["query"]["results"]["quote"]["YearLow"]
			yearhigh = data["query"]["results"]["quote"]["YearHigh"]
			marketcapital = data["query"]["results"]["quote"]["MarketCapitalization"]
			lasttradeprice = data["query"]["results"]["quote"]["LastTradePriceOnly"]
			daysrange = data["query"]["results"]["quote"]["DaysRange"]
			volume = data["query"]["results"]["quote"]["Volume"]
			stockexg = data["query"]["results"]["quote"]["StockExchange"]
			myfile = open("data_set_1/"+ filename + ".txt", "a")
			myfile.write("Name = " +str(cname)+"# Symbol = "+str(symbol)+"# AverageDailyVolume = "+str(avgdvol)+"# Change = "+str(change)+"# DaysLow = "+str(daylow)+"# DaysHigh = "+str(dayhigh)+"# YearLow = "+str(yearlow)+"# YearHigh = "+str(yearhigh)+"# MarketCapitalization = "+str(marketcapital)+"# LastTradePriceOnly = "+str(lasttradeprice)+"# DaysRange = "+str(daysrange)+"# Volume = "+str(volume)+"# StockExchange = "+str(stockexg)+"\n");
myfile.close()