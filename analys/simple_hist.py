import numpy as np
zh=np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
xh=np.histogram(np.arange(4), bins=np.arange(5), density=True)
yh=np.histogram([[1, 2, 1], [1, 0, 1]], bins=[0,1,2,3],weigths=[1,2,1])
print(xh,'\n',yh,'\n',zh)
a = np.arange(5)
hist, bin_edges = np.histogram(a, density=True)
#hist array([ 0.5,  0. ,  0.5,  0. ,  0. ,  0.5,  0. ,  0.5,  0. ,  0.5])
print(hist.sum())
zz=np.sum(hist * np.diff(bin_edges))
print(zz)
import matplotlib.pyplot as plt
plt.style.use('ggplot')
rng = np.random.RandomState(10)  # deterministic random data
a = np.hstack((rng.normal(size=1000),rng.normal(loc=5, scale=2, size=1000)))
plt.hist(a, bins='auto',histtype='step')  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()
