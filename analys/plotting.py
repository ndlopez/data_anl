import numpy as np
import matplotlib.pyplot as plt
#building data
x=np.arange(0,6,0.1) #from 0 to 6
'''y=np.sin(x)
plt.plot(x,y)
plt.show()'''
'''y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,label="sin(x)")
plt.plot(x,y2,linestyle="--",label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin(x) & cos(x)')
plt.legend()
plt.show()'''
from matplotlib.image import imread
img=imread('/home/diego/Dropbox/GOES/sdo_20110924_2029.png')
plt.imshow(img)
plt.show()
