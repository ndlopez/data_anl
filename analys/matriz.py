import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))
def id_func(x):
    return x

'''A=np.array([[1,2,3],[4,5,6]])
B=np.array([[1,2],[3,4],[5,6]])
print(A.shape,B.shape)
print(np.dot(A,B))
C=np.array([[1,2],[3,4]])
print(C.shape)
A=np.array([[1,2],[3,4],[5,6]])
B=np.array([7,8])
print(A.shape,B.shape)
print(np.dot(A,B))'''
'''X=np.array([1,2])
W=np.array([[1,3,5],[2,4,6]])
Y=np.dot(X,W)
print(Y)'''
X=np.array([1.0,0.5])
W1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1=np.array([0.1,0.2,0.3])
#print(W1.shape)print(X.shape)print(B1.shape)
A1=np.dot(X,W1)+B1
Z1=sigmoid(A1)
print(A1,Z1)
W2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2=np.array([0.1,0.2])
#print(Z1.shape,W2.shape,B2.shape)
A2=np.dot(Z1,W2)+B2
Z2=sigmoid(A2)
print(Z2)
W3=np.array([[0.1,0.3],[0.2,0.4]])
B3=np.array([0.1,0.2])
A3=np.dot(Z2,W3)+B3
Y=id_func(A3)#moushikuha Y=A3
print(A3,Y)
