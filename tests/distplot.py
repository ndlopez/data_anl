import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white",palette="muted",color_codes=True)
rs=np.random.RandomState(10)
#set up matplotlib fig
f,axes=plt.subplots(2,2,figsize=(7,7),sharex=True)
sns.despine(left=True)
#gen a random univar dataset
d=rs.normal(size=100)
#plot a simple hist with binsize det auto
sns.distplot(d,kde=False,color="b",ax=axes[0,0])
#plot a kernel density estimate and rug plot
sns.distplot(d,hist=False,rug=True,color="r",ax=axes[0,1])
#plot a filled kernel desnsity estimate
sns.distplot(d,hist=False,color="g",kde_kws={"shade":True},ax=axes[1,0])
#plot a hist and kernel density estimate
sns.distplot(d,color="m",ax=axes[1,1])

plt.setp(axes,yticks=[])
plt.tight_layout()
plt.show()
