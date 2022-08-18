import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import linspace
from mpl_toolkits.mplot3d import Axes3D

mu = 1
# r0 = [-149.6 * 10 ** 6, 0.0, 0.0]  #  Initial position
# v0 = [29.9652, -5.04769, 0.0]      #  Initial velocity
u0 = [-1, 0.0, 0.0, 0.000448907, -0.0000756192, 0.0]


def deriv(u, dt):
    n = -mu / np.sqrt(u[0] ** 2 + u[1] ** 2 + u[2] ** 2)
    return [u[3],     #  dotu[0] = u[3]'
            u[4],     #  dotu[1] = u[4]'
            u[5],     #  dotu[2] = u[5]'
            u[0] * n,       #  dotu[3] = u[0] * n
            u[1] * n,       #  dotu[4] = u[1] * n
            u[2] * n]       #  dotu[5] = u[2] * n

dt = np.arange(0.0, 20, .0001)   #  Time to run code in seconds'
u = odeint(deriv, u0, dt)
x, y, z, x2, y2, z2 = u.T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x2, y2, z2)
plt.show()

##Second option
#!/usr/bin/env python
#  This program solves the 3 Body Problem numerically and plots the
#  trajectories

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import linspace
from mpl_toolkits.mplot3d import Axes3D

mu = 132712000000.0
# r0 = [-149.6 * 10 ** 6, 0.0, 0.0]  #  Initial position
# v0 = [29.9652, -5.04769, 0.0]      #  Initial velocity
u0 = [-149.6 * 10 ** 6, 0.0, 0.0, 29.9652, -5.04769, 0.0]


def deriv(u, dt):
    n = -mu / np.sqrt(u[0] ** 2 + u[1] ** 2 + u[2] ** 2)
    return [u[3],     #  dotu[0] = u[3]'
            u[4],     #  dotu[1] = u[4]'
            u[5],     #  dotu[2] = u[5]'
            u[0] * n,       #  dotu[3] = u[0] * n
            u[1] * n,       #  dotu[4] = u[1] * n
            u[2] * n]       #  dotu[5] = u[2] * n

dt = np.linspace(0.0, 86400 * 700, 5000)  #  Time to run code in seconds'
u = odeint(deriv, u0, dt)
x, y, z, x2, y2, z2 = u.T

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()
