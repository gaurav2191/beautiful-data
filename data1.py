import sys
import csv
import operator 
from operator import itemgetter, attrgetter
import re
f=open('ratings.list')
lines=f.readlines()
data=lines[27:433870]
f.close()

count=0
regx='(\(20..\))'
lis=[]   
for txt in data:
    m = re.search(regx,txt)
    if m: 
        try:     
            l=txt.split()
            if float(l[1]) > 40000:
                lis.append([float(l[1]),txt])
        except:
            count=0
           
          
lis.sort(key = itemgetter(0), reverse = True)

for i in range(0,2000):
    print lis[i]  
