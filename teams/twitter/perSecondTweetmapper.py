#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")
    created_at, tweet, location, timezone, language = data
    c1 = created_at
    i = c1.index('+')
    sec = c1[:i-1]
    maxSec = datetime.strptime(sec, "%a %b %d %H:%M:%S").second
    #i = c1.index('+')
    #hr = c9[1:i]
    #maxHour = datetime.strptime(hr, "%Y-%m-%d %H:%M:%S.%f").hour
    print "{0}\t{1}".format(maxSec, 1)

