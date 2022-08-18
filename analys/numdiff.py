#Let y=0.01x^2+0.1x
import numpy as np
import matplotlib.pylab as plt
def num_diff(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)
def func_1(x):
    return 0.01*x**2+0.1*x
def diff_1(x):
    return 2*0.01*x+0.1
def tan_line(f, x):
    d = num_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

x=np.arange(0.0,20.0,0.1)
y=func_1(x)
#print(num_diff(func_1,5))
#print(num_diff(func_1,10))
tf = tan_line(func_1, 10)
y2 = tf(x)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.plot(x, y)
plt.plot(x, y2)
plt.show()
