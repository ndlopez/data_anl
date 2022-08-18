import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")
#load the example dataset for Anscombe's quartet
#data repository is at http://github.com/mwaskom/seaborn-data/
df=sns.load_dataset("anscombe")#\sim panda DataFrame
#df2=pd.read_csv('/home/diego/Dropbox/data/anscombe.csv')
#show the results of a linear regression within each dataset
sns.lmplot(x="x",y="y",col="dataset", hue="dataset", data=df, col_wrap=2, ci=None, palette="muted", size=4, scatter_kws={"s":50,"alpha":1})
plt.show()
