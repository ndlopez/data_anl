import numpy as np
import matplotlib.pyplot as plt
def relu(x):
    return np.maximum(0,x)
def sigmoid(x):
    return 1/(1+np.exp(-x))
x=np.random.randn(1000,100) #1000data
node_num=100 #number of neurons
hidden_layer_size=5
activ={} #number of activations
#weight_init={'std=0.01':0.01,'Xavier':'sigmoid','He':'relu'}
for i in range(hidden_layer_size):
    if i!=0:
        x=activ[i-1]
    #w=np.random.randn(node_num,node_num)*1.0
    #w=np.random.randn(node_num,node_num)*0.01#Gauss distb
    w=np.random.randn(node_num,node_num)/np.sqrt(node_num)
    z=np.dot(x,w)
    #a=sigmoid(z)
    a=relu(z)
    activ[i]=a
#histograms
for i,a in activ.items():
    plt.subplot(1,len(activ),i+1)
    plt.title(str(i+1)+"-layer")
    plt.ylim(0,7000)
    plt.hist(a.flatten(),30,range=(0,1))
plt.show()

