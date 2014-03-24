import urllib
import sys

##### How to run #####
#>python soFetch.py search_term
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