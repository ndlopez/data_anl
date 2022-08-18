import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import pandas as pd
from pandas_datareader import data
goog=data.DataReader('GOOG',start='2004',end='2016',data_source='google')
#print(goog.head())
goog=goog['Close']
#import seaborn;seaborn.set()
goog.plot(alpha=0.5,style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--');
plt.legend(['input','resample','asfreq'],loc='upper left');
plt.show()
rolling=goog.rolling(365,center=True)#moving average
data=pd.DataFrame({'input':goog,'1yr rolling_mean':rolling.mean(),'1yr rolling_std':rolling.std()})
ax=data.plot(style=['-','--',':'])
ax.lines[0].set_alpha(0.3)
plt.show()

