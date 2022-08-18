#step and sigmoid function
'''def step_function(x):
    if x>0:
        return 1
    else:
        return 0'''
import numpy as np
import matplotlib.pylab as plt
def step_function(x):
    return np.array(x>0,dtype=np.int)
def sigmoid(x):
    return 1/(1+np.exp(-x))
def relu(x):
    return np.maximum(0,x)

x=np.arange(-5.0,5.0,0.1)
y1=step_function(x)
y2=sigmoid(x)
y3=relu(x)
plt.plot(x,y1,label="Step_function(x)")
plt.plot(x,y2,linestyle="--",label="Sigmoid(x)")
plt.plot(x,y3,linewidth=2,label="RecLinearUnit(x)")
plt.ylim(-0.1,1.1)
plt.legend()
plt.show()
