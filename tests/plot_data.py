import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import pandas as pd
from pandas import Series,DataFrame,Panel
dat=np.loadtxt('/home/diego/Dropbox/data/NM_data/20031104/20031104_haleakala_NM_1min.dat')
#print(dat.shape)
dates=pd.date_range('2003-11-04 18:00:00',periods=dat.shape[0],freq='min')
#print(dates,dates.shape) #Generating x-axis time
#Using Series to work with data
A=Series(dat[:,1],index=dates)
B=Series(dat[:,1],index=dates)
#print(A[A>56000])
#print(A.index)
#using DataFrame to work with data
#NEUT=DataFrame({'datA':A})#,'datB':B})
#N1=B.resample("5T").apply(np.max)#5min counts
#kind=line,bar,barh,kde,area,scatter,hexbin,pie,hist
#NEUT.plot(kind='hist',histtype='step')
#NEUT.plot(legend=False)
#N2=NEUT.rolling(window=11,center=False).mean().plot(style='-g')
#NN.plot(subplots=True)
plt.show()
#Correlations
#NEUT.datA.rolling(window=10).corr(other=NEUT.datB).plot(style='-g')
#plt.show()
#print(NEUT.describe())#NEUT.mean()
#print(NEUT.corr())
