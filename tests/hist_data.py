"""Fitting a 4param logistic eq to ELISA data
f(x)=\frac{A-D}{1+(x/C)^B}+D
where x is the concentration, A min asymptote,
B is the steepness, C inflection point and D max asymp"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def logistic4(x,A,B,C,D):
    #4PL logistic eq
    return ((A-D)/(1.0+((x/C)**B)))+D

def residuals(p,y,x):
    #Deviations of data from fitted 4PL curve
    A,B,C,D=p
    err=y-logistic4(x,A,B,C,D)
    return err

def peval(x,p):
    #Evaluated value at x w/current params
    A,B,C,D=p
    return logistic4(x,A,B,C,D)
#Make up some data for fitting and add noise.
x=np.linspace(0,20,20)
A,B,C,D=0.5,2.5,8,7.3
y_true=logistic4(x,A,B,C,D)
y_meas=y_true+0.2*npr.randn(len(x)) #it can be data from a file
#initial params
p0=[0,1,1,1]
#fit eq using least squares optimization
plsq=leastsq(residuals,p0,args=(y_meas,x))
#plotting
plt.plot(x,peval(x,plsq[0]),x,y_meas,'o',x,y_true)
plt.title('Leastsq 4PL fit to noisy data')
plt.legend(['Fit','Noisy','True'],loc='upper left')
for i, (param,actual,est) in enumerate(zip('ABCD',[A,B,C,D],plsq[0])):
    plt.text(10,3-i*0.5,'%s=%.2f,est(%s)=%.2f'%(param,actual,param,est))
plt.show()
