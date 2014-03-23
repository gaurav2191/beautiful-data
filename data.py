import re
import sys
import csv
import operator 
from operator import itemgetter, attrgetter
f=open('ratings.list')
lines=f.readlines()
data=lines[27:433870]
f.close()
regx='([+-]?\d*\.\d+)'

count=0
regx='(\(20..\))'
lis=[]

for lines in data:
        match = re.search(regx, lines)
        if match:           
                p=match.group(1) 
                l=lines.split()
                if float(l[2])>2.0  and l[3][0]!="\"":
                   if l[len(l)-1]!="(TV)" and l[len(l)-1]!="(V)":
                    lis.append(l)
        count=count+1   
               
           


lis.sort(key = itemgetter(2), reverse = False)

for l in range(0,5000):
    print lis[l],"\n"
