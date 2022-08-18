import matplotlib.pyplot as plt
from numpy.random import normal
gaussian_numbers=normal(size=1000)
plt.hist(gaussian_numbers,bins=20,histtype='step')#defaut 10bins
plt.title("Gaussian Hist")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
'''plotting a ProbDist function: 
matplotlib will integrate the total area of the histogram 
(this is just the total number in the array feeded to matplotlib) 
and scale the values appropriately so that rather that showing 
how many numbers in each bin(frequency), instead a probability 
of finding a number in that bin will be calculated. The total 
area of the hist in this curve will be 1.'''
plt.hist(gaussian_numbers,bins=20,normed=True)
plt.xlabel("Value")
plt.ylabel("Probability")
plt.show()

'''cumulative dist function
This shows the prob of finding a number in a bin or any lower bin.
Making this as simple as throwing a single argument flag to hist()'''
plt.hist(gaussian_numbers,bins=20,normed=True,cumulative=True)
plt.show()
