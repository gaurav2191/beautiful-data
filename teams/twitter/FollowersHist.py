import sys
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from pandas import *

f = open('followers.txt', 'r')
lines = f.readlines()    
f.close()
i=1
j=1
google=[]
amazon=[]
yahoo=[]
ebay=[]
for line in lines:
	data =line.strip().split('\t') 
	if j%4 == 1 :
		google.append(int(data[1]))
		j+=1
	elif j%4 == 2 :
		yahoo.append(int(data[1]))
		j+=1
	elif j%4 == 3 :
		amazon.append(int(data[1]))
		j+=1
	else :
		ebay.append(int(data[1]))
		j+=1
print google
print yahoo
print amazon
print ebay
df = DataFrame({'Google':google,'Yahoo':yahoo,'eBay':ebay,'Amazon':amazon})
df.plot(kind='bar', color='rbmcy')
plt.show()
