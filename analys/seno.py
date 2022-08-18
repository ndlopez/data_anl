import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.2)
y=np.sin(x)
fig=plt.figure()
ax=plt.subplot()
ax.plot(x,y)
ax.set_xlabel('x')
plt.show()
