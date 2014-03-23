# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Gayaneh\.spyder2\.temp.py
"""
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt


s_row = 0
s_col = 0
w_row = 0
w_col = 0
r=0

#for plot data individually. Not called
def plot_X_Y(X,Y,Title,image,par):
    plt.plot(X,Y,'bo')
    plt.xlabel('Date')
    plt.ylabel('Temprature')
    plt.title(Title)
    plt.savefig(image+'.png')
   
if __name__ == "__main__":
    f=open('c:\users\gayaneh\.spyder2\data\sensor-data.txt','r')
    lines=f.readlines()
    f.close();
    array=[]
    x=[]
    y=[]
    for line in lines:
        ta=line.rstrip().split(',')
        array.extend(ta)
        s_col = len(ta)
        s_row += 1
        
    array2 = np.array(array).reshape((s_row,s_col))
    
    #reading web data
    f=open('c:\users\gayaneh\.spyder2\data\web-data.txt','r')
    lines=f.readlines()
    f.close();
    array3=[]
    x2=[]
    y2=[]
    for line in lines:
        ta=line.rstrip().split(',')
        array3.extend(ta)
        w_col = len(ta)
        w_row += 1
    
    array4 = np.array(array3).reshape((w_row,w_col))
    r=0
    while r < s_row:
           s=0
           x.append(array2[r+s,0])
           x.append(array2[r+s,1])
           temp =.0
           for s in range(59):
              r=r+1
              if r < s_row:
                temp= temp + np.float(array2[r,2])
       
           y.append(temp/60)
           r=r+1
    date_formatter="%m/%d/%y %H:%M:%S"
    n0=0
    n1=0
    n2=0
    n3=0
    agr_temp0=0.0
    agr_temp1=0.0
    agr_temp2=0.0
    agr_temp3=0.0
    time0=datetime.time(datetime(2014,1,1,6,0,0))
    time1=datetime.time(datetime(2014,1,1,12,0,0))
    time2=datetime.time(datetime(2014,1,1,18,0,0))
    time3=datetime.time(datetime(2014,1,1,23,59,59))
    t0=[]
    t1=[]
    t2=[]
    t3=[]
    r=1
    datetime_object=datetime.strptime(str(array4[0,0]),date_formatter)
    time_value_1=datetime_object.time()
    date_value_1=datetime_object.date()
    if  time_value_1 <= time0:
        agr_temp0=agr_temp0+np.float(array4[0,4])
        n0 +=1
    else:
        if time_value_1 <= time1:
            agr_temp1=agr_temp1+np.float(array4[0,4])
            n1 +=1
        else:
            if time_value_1 <= time2:
                agr_temp2=agr_temp2+np.float(array4[0,4])
                n2 +=1
            else:
                agr_temp3=agr_temp3+np.float(array4[0,4]) 
                n3 +=1
    while r < w_row:
         datetime_object=datetime.strptime(str(array4[r,0]),date_formatter)
         time_value_2=datetime_object.time()
         date_value_2=datetime_object.date()
         if date_value_2 == date_value_1: # still in the same day
            if  time_value_2 <= time0:
                agr_temp0=agr_temp0+np.float(array4[r,4])
                n0 +=1
            else:
                if time_value_2 <= time1:
                    agr_temp1=agr_temp1+np.float(array4[r,4])
                    n1 +=1
                else:
                    if time_value_2 <= time2:
                        agr_temp2=agr_temp2+np.float(array4[r,4])
                        n2 +=1
                    else:
                        agr_temp3=agr_temp3+np.float(array4[r,4])
                        n3 +=1
         else: #next day. calculate average temp for each time bucket and save to array
             if n0>0:
               t0.append([datetime.combine(date_value_1,time0),agr_temp0/n0])  #array saves date and time as 6:00  and average temp
             if n1>0:
                 t1.append([datetime.combine(date_value_1,time1),agr_temp1/n1])  #array saves date and time as 12:00  and average temp
             if n2>0:
                 t2.append([datetime.combine(date_value_1,time2),agr_temp2/n2])  #array saves date and time as 18:00  and average temp
             if n3>0:
                 t3.append([datetime.combine(date_value_1,time3),agr_temp3/n3])   #array saves date and time as 24:00  and average temp
             agr_temp0=0.0
             agr_temp1=0.0
             agr_temp2=0.0
             agr_temp3=0.0
             n0=0
             n1=0
             n2=0
             n3=0
             date_value_1 = date_value_2 #save new date as current date
             time_value_1 = time_value_2
             if  time_value_1 <= time0:
                  agr_temp0=agr_temp0+np.float(array4[r,4])
                  n0 +=1
             else:
                 if time_value_1 <= time1:
                     agr_temp1=agr_temp1+np.float(array4[r,4])
                     n1 +=1
                 else:
                     if time_value_1 <= time2:
                         agr_temp2=agr_temp2+np.float(array4[r,4])
                         n2 +=1
                     else:
                         agr_temp3=agr_temp3+np.float(array4[r,4]) 
                         n3 +=1
             
         r=r+1
    
    if n0>0:
        t0.append([datetime.combine(date_value_1,time0),agr_temp0/n0])  #array saves date and time as 6:00  and average temp
    if n1>0:
        t1.append([datetime.combine(date_value_1,time1),agr_temp1/n1])  #array saves date and time as 12:00  and average temp
    if n2>0:
        t2.append([datetime.combine(date_value_1,time2),agr_temp2/n2])  #array saves date and time as 18:00  and average temp
    if n3>0:
        t3.append([datetime.combine(date_value_1,time3),agr_temp3/n3])   #array saves date and time as 24:00  and average temp
    T= np.array(t0+t1+t2+t3)
    XY1=np.hsplit(T,2)
    X1=XY1[0]
    Y1=XY1[1]
 
    #plot_X_Y(X1,Y1,'Yahoo Data','web','ro')
    
   
    date_formatter="%d/%m/%y %H:%M"
    while r < s_row:
           s=0
           x.append(array2[r+s,0])
          ## print 'Time:',array2[r+s,1]
           x.append(array2[r+s,1])
           temp =.0
           for s in range(59):
              r=r+1
              if r < s_row:
                temp= temp + np.float(array2[r,2])
           ##print 'Mean Temp:', temp/60
           y.append(temp/60)
           r=r+1
    r=0
    n0=0
    n1=0
    n2=0
    n3=0
    agr_temp0=0.0
    agr_temp1=0.0
    agr_temp2=0.0
    agr_temp3=0.0
    time0=datetime.time(datetime(2014,1,1,6,0,0))
    time1=datetime.time(datetime(2014,1,1,12,0,0))
    time2=datetime.time(datetime(2014,1,1,18,0,0))
    time3=datetime.time(datetime(2014,1,1,23,59,59))
    t0=[]
    t1=[]
    t2=[]
    t3=[]
    r=1
    datetime_object=datetime.strptime(str(array2[0,0]+' '+array2[0,1]),date_formatter)
    time_value_1=datetime_object.time()
    date_value_1=datetime_object.date()
    if  time_value_1 <= time0:
        agr_temp0=agr_temp0+np.float(array2[0,2])
        n0 +=1
    else:
        if time_value_1 <= time1:
            agr_temp1=agr_temp1+np.float(array2[0,2])
            n1 +=1
        else:
            if time_value_1 <= time2:
                agr_temp2=agr_temp2+np.float(array2[0,2])
                n2 +=1
            else:
                agr_temp3=agr_temp3+np.float(array2[0,2]) 
                n3 +=1
    while r < s_row:
         datetime_object=datetime.strptime(str(array2[r,0]+' '+array2[r,1]),date_formatter)
         time_value_2=datetime_object.time()
         date_value_2=datetime_object.date()
         if date_value_2 == date_value_1: # still in the same day
            if  time_value_2 <= time0:
                agr_temp0=agr_temp0+np.float(array2[r,2])
                n0 +=1
            else:
                if time_value_2 <= time1:
                    agr_temp1=agr_temp1+np.float(array2[r,2])
                    n1 +=1
                else:
                    if time_value_2 <= time2:
                        agr_temp2=agr_temp2+np.float(array2[r,2])
                        n2 +=1
                    else:
                        agr_temp3=agr_temp3+np.float(array2[r,2])
                        n3 +=1
         else: #next day. calculate average temp for each time bucket and save to array
             if n0>0:
               t0.append([datetime.combine(date_value_1,time0),agr_temp0/n0])  #array saves date and time as 6:00  and average temp
             if n1>0:
                 t1.append([datetime.combine(date_value_1,time1),agr_temp1/n1])  #array saves date and time as 12:00  and average temp
             if n2>0:
                 t2.append([datetime.combine(date_value_1,time2),agr_temp2/n2])  #array saves date and time as 18:00  and average temp
             if n3>0:
                 t3.append([datetime.combine(date_value_1,time3),agr_temp3/n3])   #array saves date and time as 24:00  and average temp
             agr_temp0=0.0
             agr_temp1=0.0
             agr_temp2=0.0
             agr_temp3=0.0
             n0=0
             n1=0
             n2=0
             n3=0
             date_value_1 = date_value_2# save new date as current date
             time_value_1 = time_value_2
             if  time_value_1 <= time0:
                  agr_temp0=agr_temp0+np.float(array2[r,2])
                  n0 +=1
             else:
                 if time_value_1 <= time1:
                     agr_temp1=agr_temp1+np.float(array2[r,2])
                     n1 +=1
                 else:
                     if time_value_1 <= time2:
                         agr_temp2=agr_temp2+np.float(array2[r,2])
                         n2 +=1
                     else:
                         agr_temp3=agr_temp3+np.float(array2[r,2]) 
                         n3 +=1
             
         r=r+1
    
    if n0>0:
        t0.append([datetime.combine(date_value_1,time0),agr_temp0/n0])  #array saves date and time as 6:00  and average temp
    if n1>0:
        t1.append([datetime.combine(date_value_1,time1),agr_temp1/n1])  #array saves date and time as 12:00  and average temp
    if n2>0:
        t2.append([datetime.combine(date_value_1,time2),agr_temp2/n2])  #array saves date and time as 18:00  and average temp
    if n3>0:
        t3.append([datetime.combine(date_value_1,time3),agr_temp3/n3])   #array saves date and time as 24:00  and average temp
    T= np.array(t0+t1+t2+t3)
    XY2=np.hsplit(T,2)
    X2=XY2[0]
    Y2=XY2[1]
    plt.figure(1)
    plt.subplot(111)
    ax = plt.subplot(111)
    for label in ax.get_xticklabels():
     label.set_fontsize(6)
     label.set_horizontalalignment('center')
    plt.plot(X1,Y1,'ro')
    plt.xlabel('Date')
    plt.ylabel('Average Temprature')
    plt.title('Sensory and Web Data Comparision')
    plt.plot(X2,Y2,'go')
    #plt(x, 50-x, 'o', label='y=1')
    #plt(x, x-50, 'o', label='y=-1')
    legend=plt.legend
    legend( ('web', 'sensor', ), loc='upper left')
    plt.savefig('web_sensor_temps'+'.png')
   
    
    
    
    
    
   
      
    
        
        