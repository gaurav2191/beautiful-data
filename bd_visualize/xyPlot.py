import pylab as plt

def plotgraph(args, data):
	n = args.scale
	array3=data
   
  if n == 0:
    for i in range(0,len(array3)):
      plt.plot(array3[0], array3[i], lw=1)  
  elif n== 1:
      for i in range(0,len(array3)):
        plt.semilogx(array3[0], array3[i], lw=1)
  elif n == 2:
      for i in range(0,len(array3)):
        plt.semilogy(array3[0], array3[i], lw=1)
  elif  n== 3:
      for i in range(0,len(array3)):
        plt.loglog(array3[0], array3[i], lw=1)
  
  plt.show() 
  return plt