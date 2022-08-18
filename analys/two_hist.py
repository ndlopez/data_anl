import matplotlib.pyplot as plt
from numpy.random import normal, uniform
gauss_numbers=normal(size=1000)
unif_numbers=uniform(low=-3,high=3,size=1000)
plt.hist(gauss_numbers,bins=20,histtype='step',normed=True,color='b',label='Gaussian')#also stepfilled
plt.hist(unif_numbers,bins=20,histtype='step',normed=True,color='r',alpha=0.5,label='Uniform')
#alpha=0.5 option is the transparency of the color
plt.title("Gaussian / Uniform Hist")
plt.xlabel("Value")
plt.ylabel("Probability")
plt.legend()
plt.show()
