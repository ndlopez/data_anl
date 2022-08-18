import pandas as pd
import numpy as np
#import cufflinks as cf
#cf.set_config_file(offline=False,world_readable=False,theme='pearl')
df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000)-1})
df.head(2)
df.plot(kind='histogram',subplots=True,shape=(3,1))#,filename='cufflinks/histogram-subplots')
