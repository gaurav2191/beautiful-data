# -*- coding: utf-8 -*-
"""
Created on Tue Mar 8 21:32:41 2014

@author: Tim
"""

# HOLY CRAP THIS TOOK FOREVER TO MAKE

import math
import Collect
import Driver
import webDataHandler as wdh
import time
import urllib
import fileinput

# constants, apparently python doesnt understand constants
sourceAlt = 1787
sourceLat = 34.1421
sourceLon = -117.6227
pointSource = [sourceLon,sourceLat]

def main():
    config = Driver.Driver.readConfigFile('../config.txt')
    zipcodes = Collect.zipcodeScraper.getZipCodes(config[0],config[1])
    for zipcode in zipcodes:
        print('================ LOCATION '+str(zipcode)+' ================')
        zipfile = open('../'+zipcode+'.txt','r')
        line = zipfile.readlines()
        firstLine = (line[0].rstrip().split(','))
        locLat = float(firstLine[3])
        locLon = float(firstLine[4])
        pointOrigin = [locLon,locLat]
        print('Coordinates >>> '+str(pointOrigin[0])+' W, '+str(pointOrigin[1])+' N')
        heading = calcHeading(locLon,locLat)
        print('Calculated Heading >>> '+str(heading))
        distance = calcDistance(pointSource,pointOrigin)
        print('Calculated Distance >>> '+str(distance))
        altitude = findAltitude(locLat,locLon)
        print('Altitude >>> '+str(altitude))
        deltaAlt =altitude-sourceAlt
        print('Altitude Difference >>> '+str(deltaAlt))
        dto = calcOceanDistance(pointOrigin)
        print('Distance to the Ocean >>> '+str(dto))
        print('\nZIPCODE '+zipcode+' UPDATED\n')
        zipfile.close()
        overwrite(zipcode,heading,altitude,deltaAlt,distance,dto)
        time.sleep(0.25)
        
# formula for heading: θ = atan2( sin(Δλ).cos(φ2), cos(φ1).sin(φ2) − sin(φ1).cos(φ2).cos(Δλ) )
def calcHeading(locLon,locLat):
    y=math.sin(locLon-sourceLon)*math.cos(locLat)
    x=math.cos(sourceLat)*math.sin(locLat)- math.sin(sourceLat)*math.cos(locLat)*math.cos(locLon-sourceLon)
    heading =math.degrees(math.atan2(y,x))
    return heading

# distance formula: √([x2-x1]²+[y2-y1]²)
def calcDistance(point1,point2):
    try:
        distance = (math.sqrt(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2)))*57.296
        return distance
    except:
        print("method calcDistance says: arguments must be passed in an array/list or tuple")

# a formula too long to type
def calcOceanDistance(pointOrigin):
    coast=open('../OceanPoints.txt')
    print (coast)
    coastline=coast.readlines()
    shoreMatrix=range(len(coastline))
    for lines in range(0, len(coastline)):
        shoreMatrix[lines]=(coastline[lines].rstrip().split(','))
    print('\nDistance to Points, Longitude, Latitude:')
    for i in range(0,len(coastline)):
        # find distance
        oceanLon=float(shoreMatrix[i][1])
        oceanLat=float(shoreMatrix[i][2])
        pointOcean=[(oceanLon),(oceanLat)]
        cdist = calcDistance(pointOrigin,pointOcean)
        shoreMatrix[i][0]=cdist
        shoreMatrix[i][1]=oceanLon
        shoreMatrix[i][2]=oceanLat
    for j in range(0,len(coastline)):
        for k in range(0,len(coastline)-1):
            if shoreMatrix[k][0]>shoreMatrix[k+1][0]:
                shoreMatrix[k][:],shoreMatrix[k+1][:]=shoreMatrix[k+1][:],shoreMatrix[k][:]
    sortedMatrix=shoreMatrix
    pointClosest=[sortedMatrix[0][1],sortedMatrix[0][2]]
    distancePC=calcDistance(pointOrigin,pointClosest)
    pointN1=[sortedMatrix[1][1],sortedMatrix[1][2]]
    pointN2=[sortedMatrix[2][1],sortedMatrix[2][2]]
    vCO=createVectors(pointClosest,pointOrigin)
    vCN1=createVectors(pointClosest,pointN1)
    vCN2=createVectors(pointClosest,pointN2)
    theta1=calcAngle(vCO,vCN1)
    theta2=calcAngle(vCO,vCN2)
    pointIntersect=[]
    if(theta1>=90 and theta2>=90):
        return distancePC
    elif(theta1<theta2):
        distanceToOcean=(distancePC*math.sin(theta1))/(math.sin(90))
        return distanceToOcean
    elif(theta2<theta1):
        distanceToOcean=(distancePC*math.sin(theta2))/(math.sin(90))
        return distanceToOcean
        
# vector = < x2-x1, y2-y1 >
def createVectors(point1,point2):
    try:
        vector = [point2[0]-point1[0],point2[1]-point1[1]]
        return vector
    except:
        print("method createVectors says: arguments must be passed in an array/list or tuple")
    
# finds the dot product of two vectors: a · b = ax × bx + ay × by
def calcDotProduct(vector1,vector2):
    try:
        dotProduct = (vector1[0]*vector2[0]+vector1[1]*vector2[1])
        return dotProduct
    except:
        print("method calcDotProduct says: arguments must be passed in an array/list or tuple")

# finds the angle between two vectors i and j: θ = arcos([i₁·j₁ + i₂·j₂]÷[√{i₁²+i₂²}·√{j₁²+j₂²}])
def calcAngle(vAB,vAC):
    theta = math.degrees(math.acos((vAB[0]*vAC[0]+vAB[1]*vAC[1])/(math.sqrt(vAB[0]**2+vAB[1]**2)*math.sqrt(vAC[0]**2+vAC[1]**2))))
    return theta

# this method is suppose to take the lat/long as argumetns and look up their elevation and return it as an int
def findAltitude(locLat,locLon):
    lati = locLat
    lngi = locLon
    ALT_URL_P1 = 'http://maps.googleapis.com/maps/api/elevation/json?'
    ALT_URL_P2 = "locations=%s,%s&sensor=%s" % (lati, lngi, "false")
    url= ALT_URL_P1 + ALT_URL_P2
    rpage=urllib.urlopen(url)
    rline=(rpage.readlines())
    rlines=(rline[3].rstrip().split(' '))
    rlinesc=(rlines[11].split(','))
    elevation = (float(rlinesc[0])*3.28084)
    return elevation
    
def overwrite(zipcode,a,b,c,d,e):
    f = open("../"+zipcode+".txt", "r")
    lines = f.readlines()
    line1=lines[0]
    line1s=line1.rstrip().split(",")
    line1s.append(str(a)+','+str(b)+','+str(c)+','+str(d)+','+str(e)+'\n')
    line1s=",".join(line1s)
    line1s="".join(line1s)
    lines[0]=line1s
    lines = "".join(lines)
    f = open("../91701.txt", "w")
    f.write(lines)
    f.close()

main()
time.sleep(10)