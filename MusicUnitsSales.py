import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import scipy
import pandas
import pylab as pl
import matplotlib.image as mpimg
import matplotlib.artist as art
from matplotlib import pyplot as plt
from operator import *
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
#Add Extra Parameter
population=np.multiply(population,10)
sum=map(truediv,b,population)
sum=np.multiply(sum,5000)
lenwidth=map(truediv,b,a)
print sum[2],lenwidth
fig = plt.figure()
ax = fig.add_subplot(111, axisbg = 'w')
fig.set_facecolor('1')
# img=mpimg.imread('jp.png')
# print img
# imgplot = plt.imshow(img)  
plt.grid(True)
total=plt.plot(a,b, "s-" ,label="Total Units Sales",lw="4")
cd=plt.plot(a,c, "v-" ,label="CD's Sales",lw="2.4")
# plt.plot(a,sum, "o-",label="Analysis(Population/Units Sold)",lw="3")
plt.plot(a,d, "p-",label="Cassettes Sales",lw="1.2")
plt.plot(a,e, "h-",label="LP/EP",lw="0.7")
plt.plot(a,f, "d-",label="Internet Sales",lw="1.27")
plt.plot(a,g, "8-",label="Music Videos",lw=".23")
plt.plot(a,h, "o-",label="8 Tracks",lw=".20")
ax.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.) 
plt.title('40 years Revenue Flow')             
plt.ylabel('Number of Units Sold in Millions', fontsize=15)
plt.xlabel('Years', fontsize=15)
plt.show()

