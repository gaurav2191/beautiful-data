#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from BeautifulSoup import BeautifulSoup

from pandas import *
from pandas.tools.plotting import scatter_matrix


#df = DataFrame(randn(1000, 4), columns=['a', 'b', 'c', 'd'])
c=['amazon','ebay','google','yahoo']
for item in c :
	seconds = []
	cnt = []
	s = []

	f = open("part-00000_"+item+"_tweetpersec","r").readlines()


	for line in f:
		data = line.rstrip().split('\t')
		seconds.append(float(data[0]))
		cnt.append(float(data[1]))
		s.append(float(data[1]))
	plt.scatter(seconds, cnt, s=s)
	plt.grid(True)
	plt.suptitle("Tweets per second")
	plt.show()
    
