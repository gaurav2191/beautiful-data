import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas
import math
import numpy
import pylab as pl
import matplotlib.image as mpimg
import matplotlib.artist as art
from matplotlib import pyplot as plt
from operator import *
import matplotlib.mlab as mlab
def summy(h):
    sumt=0
    for x in h:
        sumt += x
    print sumt
    return sumt
y=[]
x=[]
z=[]
population=[]
data = np.genfromtxt('sales.csv',delimiter=',',dtype = float)
a = [row[0] for row in data]#year
b = [row[1] for row in data]#Sale
c = [row[2] for row in data]#CD
d = [row[3] for row in data]#Cassettes
e = [row[4] for row in data]#LP/EP
f = [row[5] for row in data]#Internet
g = [row[6] for row in data]#Music Videos
h = [row[7] for row in data]#8 Tracks
population = [row[8] for row in data]#Pop
len= population.__len__()
adpopulation=np.multiply(population,10)
sum=map(truediv,b,adpopulation)
sum=np.multiply(sum,5000)
lenwidth=map(truediv,b,a)
summ=summy(b)
average=(summ/41)
for x in b:
    if x<average :
        variance= (average-float(x))
print average
print sum[2 ],lenwidth
print a
print b
print population
population=np.multiply(population,10)
#considering m=(Number Of Units Sold/Population)
musicRatio = [(float(x) / float(y)*1000)for x,y in zip(b, population)]
print musicRatio
i=1973
xi=[]
nppl=0
for noOfPeople in musicRatio:
    print noOfPeople
    print i
    rad=noOfPeople*10.3
    N=20
    x = np.random.rand(N)
    y = np.random.rand(N)
    print rad
    area = (noOfPeople*0.9)
    plt.scatter(i, noOfPeople, s=20, alpha=0.8,color="red",label=noOfPeople)
    i=i+1
    xi.append(noOfPeople)
plt.xlabel('Year')
plt.ylabel('Number Of People')
plt.title('For Every Thousand People How Many Own the a Valid Music')
plt.show()
print "Maximum Reached",max(musicRatio),"people carry music unit Out of One Thousand In the World in",maxYear
print "1973",musicRatio[1],"1993",musicRatio[21],"2013",musicRatio[40]
print "1999 max",max(musicRatio)










