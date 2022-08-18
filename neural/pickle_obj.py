import sys,os
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist
def get_data():
    (x_train,t_train),(x_test,t_test)=load_mnist(normalize=True,flatten=True,one_hot_label=False)
    return x_test,t_test

def init_network():
    with open("../deep-learning-from-scratch/ch03/sample_weight.pkl",'rb') as f:
        network=pickle.load(f)
    return network

def predict(network,x):
    W1,W2,W3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']
    a1=np.dot(x,W1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1,W2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2,W3)+b3
    y=softmax(a3)
    return y

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    if x.ndim==2:
        x=n.T
        x=x-np.max(x,axis=0)
        y=np.exp(x)/np.sum(np.exp(x),axis=0)
        return y.T
    x=x-np.max(x)
    return np.exp(x)/np.sum(np.exp(x))

x,t=get_data()
network=init_network()
acc_cnt=0 #accuracy
for i in range(len(x)):
    y=predict(network,x[i])
    p=np.argmax(y)
    if p==t[i]:
        acc_cnt+=1

print("Accuracy:" +str(float(acc_cnt)/len(x)))
