import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import scipy
import csv
import pandas
import pylab as pl
import matplotlib.image as mpimg
import matplotlib.artist as art
from matplotlib import pyplot as plt
from operator import *
data = np.genfromtxt('2012.csv',delimiter=',',dtype = float)
a = [row[16] for row in data]
data1 = np.genfromtxt('2012.csv',delimiter=',')
name=[row[0] for row in data1]
b = [row[17] for row in data]
sum=map(truediv,a,b)
array=[]
y=[]
data=[]
color=[]
z=[]
with open('2012.csv', 'rb') as f:
    reader = csv.reader(f)
    for row, long in zip(reader, sum):
            print row[0],"per Year"
            print long,"$ Spent by 1 person in"  
            data.append((long*40))
            y.append(int(long))
            z.append(int(long))
            if(long<5):
                color.append('red')
            if(5<long<10):
                color.append('blue')
            if(10<long<15):
                color.append('green')
            if(15<long<20):
                color.append('yellow')
            if(20<long<30):
                color.append('grey')
N=len(data)
n=[]
f = open('1999.csv')
lines = f.readlines()
f.close()
for line in lines:
        ta = line.rstrip().split(',')
        n.append(ta[0]) 
fig, ax = plt.subplots()
a=np.random.random(N)
b=np.random.random(N)
area = data
ax.scatter(b, a, s=area, alpha=0.5,color=color)

for i, txt in enumerate(n):
    ax.annotate(txt, (a[i],b[i]))
plt.show()       

# print "Zimbabwe per Year"
# print sum.index(max(sum))
# print sum.index(min(sum))
        


