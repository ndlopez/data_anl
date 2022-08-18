#Scatter 3D plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
xs=[1,2,3,4,5,6,7,8,9,0]
ys=[5,6,2,3,13,4,1,2,4,8]
zs=[2,3,3,3,5,7,9,11,9,10]

xt=[-1,-2,-3,-4,-5,-6,-7,-8,-9,0]
yt=[-5,-6,-2,-3,-13,-4,-1,2,-4,-8]
zt=[-2,-3,-3,-3,-5,-7,-9,-11,-9,-10]

ax.scatter(xs,ys,zs,c='r',marker='o')
ax.scatter(xt,yt,zt,c='b',marker='*')

ax.set_xlabel('Xlb')
ax.set_ylabel('Ylb')
ax.set_zlabel('Zlb')
plt.show()
