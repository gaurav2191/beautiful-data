import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
c = ['amazon','ebay','google','yahoo']
for item in c:
	labels = []
	sizes = []
	other=0
	f = open('part-00000_'+item, 'r')
	lines = f.readlines()    
	f.close()
	#i=0
	for line in lines:
		data =line.strip().split('\t') 
		if int(data[1]) < int(100) :
			other=other+ int(data[1])
		else :
			labels.append(data[0])
			sizes.append(data[1])
	print other
	print labels
	sizes.append(other)
	labels.append('other')
	#a=np.random.random(40)
	#cs = cm.Set2(np.arange(40)/40.)
	colors = ['red','orange','blue','yellow','green', 	'lightskyblue','lightcoral','purple']
	plt.pie(sizes,  labels=labels, colors=colors, autopct='%1.1f%%')
	plt.axis('equal')
	plt.suptitle('Languages used in tweets')
	plt.show()
