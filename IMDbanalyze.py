import re
import operator
from numpy import arange,array,ones,linalg
from pylab import plot,show
from scipy.stats.stats import pearsonr
from scipy import stats
def mean(numberList):
    return float(sum(numberList)) / len(numberList)


def linearRegression(xi,y):
    A = array([ xi, ones(len(xi))])
    # linearly generated sequence
    #w = linalg.lstsq(A.T,y)[0] # obtaining the parameters
    # plotting the line
    #line = w[0]*xi+w[1] # regression line
    #plot(xi,line,'r-',xi,y,'o')
    #show()
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
    print 'r value', r_value
    print  'p_value', p_value
    print 'standard deviation', std_err

    line = slope*xi+intercept
    print " Average rating of 2013 Prediction is ",line
    plot(xi,line,'r-',xi,y,'o')
    show()

f=open('ratings.list')
lines=f.readlines() 
data=lines[27:433870]
f.close()
lis={}
lis1={}
tmplis={}
forReg={}
correlation={}
regx='\s+([\d+.*]+)\s+(\d+)\s+([\d+.+]+)\s+(.*)\((\d+)\)\s(.*)'
#regx='\s+(\d+\.+)'
writer = open('IMDB.csv', 'wb')
writer.write('New Distribution,'+'Votes,'+'Rating,'+'Movie/TV,'+'Year,'+"\n")
i=0
for txt in data:
    m = re.search(regx,txt)
    if m:
      newDistribution=m.group(1)
      votes=m.group(2)
      rating=m.group(3)
      movie=m.group(4)
      year=m.group(5)
      extend=m.group(6)
     # print year," ------------- ",extend
      e=movie.replace(',',' ')+extend
      s=''
      s=newDistribution+","+votes+","+rating+","+e+","+year+"\n"
      writer.write(s)
      if float(votes) > 1000 and 'TV' not in e and 'V' not in e and '{' not in e and '"' not in e:
              if year in forReg:
                temp=forReg[year]
                temp=temp+","+rating
                forReg[year]=temp
              else:
                 forReg[year]=rating
      if float(year) >=2000 and float(year) <=2009 and 'TV' not in e and 'V' not in e and '{' not in e and '"' not in e:
         lis[e]=float(rating)
         tmplis[e]=float(votes)
      if float(year)>=1900 and float(year)<2000 and float(votes) > 1000 and 'TV' not in e and 'V' not in e and '{' not in e and '"' not in e:
          if year in lis1:
              temp=lis1[float(year)]
              temp=temp+","+rating
              lis1[float(year)]=temp
          else:
              lis1[float(year)]=rating
      if float(year)>=1900 and float(year)<2000 and 'TV' not in e and 'V' not in e and '{' not in e and '"' not in e:
               if float(year) in correlation:
                 corrlis=correlation[float(year)]         
                 corrlis=corrlis+(rating,votes)
                 correlation[float(year)]=corrlis
               else:
                 correlation[float(year)]=(rating,votes)
      corrlis=()







for key in lis1:
    l=lis1[key].split(',')
    for i in range(0,len(l)):
        l[i]=float(l[i])
    avg=mean(l)
    lis1[key]=avg


for key in forReg:
    l=forReg[key].split(',')
    for i in range(0,len(l)):
        l[i]=float(l[i])
    avg=mean(l)
    forReg[key]=avg
################# Year with highest Average###############################################


sortedAvg=sorted(lis1.items(), key=operator.itemgetter(0),reverse=False)
avger=0
for yr in range(1900,1999):
    if yr in lis1 and yr+1 in lis1:
       if lis1[yr]<lis1[yr+1]:
          avger=yr
         # print yr

print yr," is Year with highest Average is ",lis1[yr] 

################# Average of Top 10 Most Popular Movies ###############################################
pop_list=sorted(lis.items(), key=operator.itemgetter(1),reverse=True)
pop_list1=sorted(tmplis.items(), key=operator.itemgetter(1),reverse=True)
avg=0
i=1
for key in pop_list1:

    print lis[key[0]]," ------ ",key[1]," --- ",key[0]
    avg=avg+lis[key[0]]
    #print i
    if i>9:
       break
    i=i+1

print "Average of Top 10 Most popular movies is ",avg/10
################# Expected Average rank for 2013 using linear regression #########################################################################
ylis=[]
xi=[]
for key in forReg:
    ylis.append(float(forReg[key]))
    xi.append(float(key))

print linearRegression(array(xi),array(ylis))
################# Correlation between Rating and votes #########################################################################
j=0
rating=[]
votes=[]
for k in correlation:
    #print k,correlation[k]
    for i in correlation[k]:
        if j==0:
           rating.append(float(i))
           j=1
        elif j==1:
           votes.append(float(i))
           j=0
    tmp=pearsonr(array(rating),array(votes))  
    correlation[k]=tmp[0]

pop_list=sorted(correlation.items(), key=operator.itemgetter(0),reverse=False)

for i in pop_list:
    print i  
#######################################
