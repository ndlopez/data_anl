import os,sys
sys.path.append(os.pardir)
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.util import smooth_curve
from common.multi_layer_net import MultiLayerNet
from common.optimizer import SGD
#def relu(x):
#    return np.maximum(0,x)
#reading MNIST data
(x_train,t_train),(x_test,t_test)=load_mnist(normalize=True)
train_size=x_train.shape[0]
batch_size=128
max_iter=1000
weight_init={'std=0.01':0.01,'Xavier':'sigmoid','He':'relu'}
optimizer=SGD(lr=0.01)
networks={}
train_loss={}
activ={}
for key,weight_type in weight_init.items():
    networks[key]=MultiLayerNet(input_size=784,hidden_size_list=[100,100,100],output_size=10,weight_init_std=weight_type)
    train_loss[key]=[]
for i in range(max_iter):
    batch_mask=np.random.choice(train_size,batch_size)
    x_batch=x_train[batch_mask]
    t_batch=t_train[batch_mask]
    for key in weight_init.keys():
        grads=networks[key].gradient(x_batch,t_batch)
        optimizer.update(networks[key].params,grads)
        loss=networks[key].loss(x_batch,t_batch)
        train_loss[key].append(loss)

    if i%100==0:#activating layers
        print("=="+"iter:"+str(i) +"==")
        for key in weight_init.keys():
            loss=networks[key].loss(x_batch,t_batch)
            #activ[i]=loss
            #print(i,activ[i])
            print(i,key+":"+str(loss))

#histograms
'''for i,a in activ.items():
for key in train_loss[key]:

    plt.subplot(1,len(activ),i+1)#1x5
    plt.title(str(i+1)+"-layer")
    plt.hist(a.flatten(),30,range=(0,1))
    plt.ylim(0,5000)
plt.show()'''

#Graph
markers = {'std=0.01': 'o', 'Xavier': 's', 'He': 'D'}
x = np.arange(max_iter)
for key in weight_init.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 2.5)
plt.legend()
plt.show()

'''activ={} #number of activations
for i in range(hidden_layer_size):
    if i!=0:
        x=activ[i-1]
    #w=np.random.randn(node_num,node_num)*1 #He
    #w=np.random.randn(node_num,node_num)*0.01#Gauss distb
    w=np.random.randn(node_num,node_num)/np.sqrt(node_num)#Xavier
    z=np.dot(x,w)
    a=sigmoid(z)
    activ[i]=a
#histograms
for i,a in activ.items():
    plt.subplot(1,len(activ),i+1)
    plt.title(str(i+1)+"-layer")
    plt.hist(a.flatten(),30,range=(0,1))
plt.show()'''

