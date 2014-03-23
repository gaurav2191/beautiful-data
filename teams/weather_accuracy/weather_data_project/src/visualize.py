#!/usr/bin/env python
import matplotlib.pyplot as plt
import DistanceFunction as df
import numpy  as np
import pylab as pl

def plotData():    
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    print "printing out dictionary"

    ## the data
    x,y = df.getData()
    tempX = []
    tempY = []
    i = 0
    for temp in x:
      for j in range (len(x[temp])):
#        print temp
        tempX.insert(i, x[temp][j])
        i = i + 1
        
    for temp in y:
      for j in range (len(x[temp])):
#          print temp
          tempY.insert(i, y[temp])
          i = i + 1
    ## left panel
    tempX = np.asarray(tempX)
    tempY = np.asarray(tempY)
    print type(tempX), type(tempY), 'ok'
#    ax1.scatter(tempY,tempX,color='blue',s=5,edgecolor='none')
#
#    plt.show()
    
    T = np.arctan2(tempY, tempX)

    n = 1024
#    tempX = np.random.normal(0, 1, n)
#    tempY = np.random.normal(0, 1, n)
#    pl.axes([0.025, 0.025, 0.95, 0.95])
    pl.scatter(tempX, tempY, s=30, c=T, alpha=.5)

#    pl.xlim(-1.5, 1.5)
    pl.xticks(())
#    pl.ylim(-1.5, 1.5)
    pl.yticks(())

    pl.show()