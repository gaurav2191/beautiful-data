#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in sys.stdin:
    data = line.strip().split("\t")
    count =1
    if len(data)==5:
	date, tweet, location, timestamp, language = data
	print "{0}\t{1}".format(language,count)	
    
