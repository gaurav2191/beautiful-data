import urllib
import sys

######################
#Author: Ummata
######################
#This program downloads xml from Stackoverflow xml feed by tags.
#input: keyword
#output: keyword.xml
##### How to run #####
#>python soFetchTag.py keyword
# 
#Example
#>python soFetchTag.py 'big data'
#######################
if __name__ == '__main__':
	cmdargs = sys.argv

	search_term = cmdargs[1]
	url = 'http://careers.stackoverflow.com/jobs/feed?tags='+search_term
	filename = search_term+'.xml'
	urllib.urlretrieve (url, filename)