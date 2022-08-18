#Let f(x0,x1)=x_0^2+x_1^2 Derive
import numpy as np
import matplotlib.pylab as plt
def function_2(x):
    return np.sum(x**2)
    #return x[0]**2+x[1]**2
x0=np.arange(-3.0,3.0,0.1)
x1=np.arange(-3.0,3.0,0.1)
y=function_2(x0)
print(x0.shape,x1.shape,y.shape)
plt.plot(x0,y)
y2=function_2(x1)
plt.plot(x1,y2)
plt.show()

