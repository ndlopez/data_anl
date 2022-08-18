#1/20 x^2+y^2 plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
def func(x,y):
    return x**2+y**2
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
xs=np.arange(-10,10)
ys=np.arange(-10,10)
zs=func(xs,ys)
#ax.scatter(xs,ys,zs,c='r')
ax.plot(xs,ys,zs)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
