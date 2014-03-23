import urllib2
import time
import datetime
import os

dirpath = "data_set_2"
if not os.path.exists(dirpath):
	os.makedirs(dirpath)
def pullData(stock):
	try:
		print 'Currently Pulling', stock
		print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		urlToViist = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=3y/csv'
		saveFileLine = 'data_set_2/'+stock+'.txt'

		try:
			readExistingData = open(saveFileLine,'r').read()
			splitExisting = readExistingData.split('\n')
			mostRecentLine = splitExisting[-2]
			lastUnix = int(mostRecentLine.split(',')[0])
		except Exception,e:
			'''print str(e)
			time.sleep(0)'''
			lastUnix = 0
			


		saveFile = open(saveFileLine,'a')
		sourceCode = urllib2.urlopen(urlToViist).read()
		splitSource = sourceCode.split('\n')

		for eachLine in splitSource:
			if 'values' not in eachLine:
				splitLine = eachLine.split(',')
				if len(splitLine) == 6:
					if int(splitLine[0]) > int(lastUnix):
						lineToWrite = eachLine+'\n'
						saveFile.write(lineToWrite)
		saveFile.close()
		print 'Pulled, ', stock
		print 'Sleeping........'
		print str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
		'''time.sleep(300)'''
	except Exception,e:
		#print 'main loop', str(e)
		str(e)



symbolslist = open("symbols.txt").read()
symbolslist = symbolslist.split("\n")
for symbol in symbolslist:
	pullData(symbol)
