import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s=pd.Series([1,3,5,np.nan,6,8])
print(s)
dates=pd.date_range('20171020',periods=10)
print(dates)
df=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
print(df)
print('Printing ~5 items:\n',df.head())
print('Printing 3 tail items\n:',df.tail(3))
#Describe shows a quick statistic summary of your data
print(df.describe())
#Transposing the data
print(df.T)
#Sorting by an axis
df.sort_index(axis=1,ascending=False)
#Selecting a list from the data
print(df['A']) #or df.A
#Getting a cross section using a label
print(df.loc[dates[0]])
#Selecting on a multi-axis by label
print(df.loc[:,['A','B']])
print(df.loc[dates[0],'A']) or print(df.at[dates[0],'A'])
#Selecting values from a DataFrame where a boolean cond is meet
print(df[df>0])
df2=df.copy()
df2['E']=['one','two','three','one','two','three','three','one','two','three']
print(df2)
print(df2[df2['E'].isin(['two','four'])])
s1=pd.Series([1,2,3,4,5,6,7,8,9,0],index=pd.date_range('20171020',periods=10))
print(s1)
#Adding a new column to our dataframe 'df'
df['F']=s1
df.at[dates[0],'A']=0
df.iat[0,1]=0
df.loc[:,'D']=np.array([1.414]*len(df))
print(df)#column E is suppressed
#Now, a 'where' op with setting
df2=df.copy()
df2[df2>0]=-df2
#Missing data
df1=df.reindex(index=dates[0:9],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E']=1
print(df1)
#To drop any rows that have missing data
print(df1.dropna(how='any'))
#Filling missing data
print(df1.fillna(value='3.141592'))
#To confirm if any values are NaN
#print(pd.isna(df1)) #pd has no attribute 'isna'!
print(df.mean())#descriptive statistic per columns
print(df.mean(1))#descriptive statistic per rows
'''df2=pd.DataFrame({'A':1.,'B':pd.Timestamp('20171029'),'C':pd.Series(1,index=list(range(4)),dtype='float32'),'D':np.array([3]*4,dtype='int32'),'E':pd.Categorical(["Test","Train","test","train"]),'F':'foo'})
print('Calculating...')
print(df2)'''
s=pd.Series([0,2,4,np.nan,8,np.nan,10,12,14,16],index=dates).shift(2)
print(s)
print(df.sub(s,axis='index'))
print(df.apply(np.cumsum))#cumulative sum
print(df.apply(lambda x:x.max()-x.min()))
s=pd.Series(np.random.randint(0,7,size=10))
print(s.value_counts())
s=pd.Series(['A','B','C','Aaab','BAab',np.nan,'CabA','dog','cat','mouse',np.nan])
print(s.str.lower())#Lowercase
print(df)
pieces=[df[:3],df[3:7],df[7:]]
kat=pd.concat(pieces)
test_file=open('test_panda.txt','w')#option 'a' to append
df=pd.DataFrame(np.random.randn(10,4))
test_file.write(str(df))
test_file.write(str(kat))
test_file.flush()
test_file.close()

