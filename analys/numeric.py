import numpy as np
#x=np.array([1.0,2.0,3.0])
#print(x)
#print(type(x))
#y=np.array([2.0,4.0,6.0])
'''print(x+y)
print(x-y)
print(x*y) # element-wise product
print(x/y)
print(x/2.0)'''
'''A=np.array([[1,2],[3,4]])
print(A.shape)
print(A.dtype)
B=np.array([[3,0],[0,6]])'''
#print(A,B)
#print(A+B)
#print(A*B)
#print(A*10)
A=np.array([[1,2],[3,4]])
B=np.array([10,20])
#print(A*B)
X=np.array([[51,55],[14,19],[0,4]])
print(X) #also X[0] 1st row vector,X[0][1]=55 element(0,1)
for row in X:
    print(row)
X=X.flatten()
print(X)
#print(X[np.array([0,2,4])])
print(X>15) #bool answer
print(X[X>15]) #math answer

