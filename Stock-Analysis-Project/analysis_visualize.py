import time
import datetime 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
'''matplotlib.rcParams.update({'font.size': 9})'''
from matplotlib.finance import candlestick

def movingavg(values,window):
	weights = np.repeat(1.0,window)/window
	smas = np.convolve(values, weights, 'valid')
	return smas


def sentiment_analysis(sym):
	linecount = 0
	symbol = ''
	y_l = ''
	y_h = ''
	c_p = ''
	year_low = 1
	year_high = 1
	current_rate = 1
	not_found = 1
	suggest_for = sym
	file = open('data_set_1/Company_Info_numbers.txt', 'r+')
	for line in file:
	    key_val = line.split('#')
	    symbol = key_val[1].split(' ')[3]
	    if (suggest_for.upper() == symbol):
	        y_l = y_l + "#" + key_val[6].split(' ')[3]
	        y_h = y_h + "#" + key_val[7].split(' ')[3]
	        c_p = c_p + "#" + key_val[9].split(' ')[3]
	        not_found = 0
	        break;
	    linecount = linecount + 1

	yl = y_l.split('#')
	if len(yl) > 1:
	    year_low =  float(yl[1])
	#print year_low

	yh = y_h.split('#')
	if len(yh) > 1:
	    year_high =  float(yh[1])
	#print year_high

	cp = c_p.split('#')
	if len(cp) > 1:
	    current_rate =  float(cp[1])
	    print symbol
	#print current_rate


	percent_down = year_low*100/current_rate
	percent_decrease = 100 - percent_down
	#print percent_decrease

	percent_high = year_high*100/current_rate
	percent_increase = percent_high - 100
	#print percent_increase

	if(100 < percent_increase):
	    suggestion = 'Never purchase this'

	elif (25 < percent_increase < 100):
	    suggestion = 'Not a good investment'
	elif (50 < percent_decrease):
	    suggestion = 'Very good to take'
	elif (10 < percent_decrease < 50):
	    suggestion = 'Good to take'
	else:
	    suggestion = 'Moderate kind'


	if not_found == 1:
	    print "Symbol not found"
	else:
	    print suggestion




def draphData(stock, MA1, MA2):
	try:
		stockFile = 'data_set_2/'+stock+'.txt'
		date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack=True,converters={0: mdates.strpdate2num('%Y%m%d')})
		
		x = 0
		y = len(date)
		candleAr = []
		while x < y:
			appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
			candleAr.append(appendLine)
			x+=1

		av1 = movingavg(closep, MA1)
		av2 = movingavg(closep,MA2)

		sp = len(date[MA2-1:])	
		label1 = str(MA1)+'SMA'
		label2 = str(MA2)+'SMA'
		




		fig = plt.figure(facecolor='#07000d')
		ax1 = plt.subplot2grid((5,4), (0,0), rowspan = 4, colspan = 4 , axisbg='#07000d')
		candlestick(ax1, candleAr[-sp:], width = 1, colorup='#9eff15', colordown='#ff1717')
		ax1.plot(date[-sp:],av1[-sp:],'#5998ff', label= label1,linewidth=1.5)
		ax1.plot(date[-sp:],av2[-sp:],'#e1edf9', label= label2,linewidth=1.5)
		
		ax1.grid(True, color = 'w')
		ax1.yaxis.label.set_color('w')
		ax1.spines['bottom'].set_color("#5998ff")
		ax1.spines['top'].set_color("#5998ff")
		ax1.spines['left'].set_color("#5998ff")
		ax1.spines['right'].set_color("#5998ff")
		ax1.tick_params(axis='y' , colors = 'w')
		plt.ylabel('Stock Price')
		plt.legend(loc=0, prop={'size':10},fancybox=True)

		volumeMin = 0

		ax2 = plt.subplot2grid((5,4),(4,0),sharex=ax1, rowspan=1,colspan=4, axisbg='#07000d')
		ax2.plot(date, volume, '#00ffeb', linewidth=.8)
		ax2.fill_between(date,volumeMin,volume,facecolor='#00ffeb', alpha = .5)
		'''ax2.axes.yaxis.set_visible(False)'''
		ax2.axes.yaxis.set_ticklabels([])
		
		ax2.grid(False)
		ax2.spines['bottom'].set_color("#5998ff")
		ax2.spines['top'].set_color("#5998ff")
		ax2.spines['left'].set_color("#5998ff")
		ax2.spines['right'].set_color("#5998ff")
		ax2.tick_params(axis='x' , colors = 'w')
		ax2.tick_params(axis='y' , colors = 'w')
		plt.ylabel('Volume', color='w')


		ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
		for label in ax2.xaxis.get_ticklabels():
			label.set_rotation(45)
		
		
		'''plt.xlabel('Date', color = "w")'''
		'''plt.ylabel('Stock Price')'''
		plt.suptitle(stock+' Stock Price', color="w")
		plt.setp(ax1.get_xticklabels(),visible=False)
		plt.subplots_adjust(left=.09,bottom=.18, right= .94,top=.94,wspace=.20,hspace=0)
		plt.show()
		fig.savefig(stock+'.png', facecolor = fig.get_facecolor())

	except Exception, e:
		print 'failed main loop', str(e)

var = raw_input("Please enter a stock symbol \n").upper()
sentiment_analysis(var)
draphData(var, 12, 26)
