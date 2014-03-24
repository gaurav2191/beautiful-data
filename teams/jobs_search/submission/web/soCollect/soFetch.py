import urllib
import sys

######################
#Author: Ummata
######################
#This program downloads xml from Stackoverflow xml feed by keywords.
#input: keyword
#output: keyword.xml
##### How to run #####
#>python soFetch.py keyword
# 
#Example
#>python soFetch.py 'big data'
#######################
if __name__ == '__main__':
	cmdargs = sys.argv

	search_term = cmdargs[1]
	url = 'http://careers.stackoverflow.com/jobs/feed?searchTerm='+search_term+'&location=usa'
	filename = search_term+'.xml'
	urllib.urlretrieve (url, filename)