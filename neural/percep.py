#perceptron model
'''def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    tmp=x1*w1+x2*w2
    if tmp<=theta:
        return 0
    elif tmp > theta:
        return 1
'''
import numpy as np
x=np.array([0,1])
w=np.array([0.5,0.5])
b=-0.7
print('weight*x',w*x)
print('sum(w+x)',np.sum(w*x))
print('sum +b',np.sum(w*x)+b)
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(w*x) +b
    if tmp<=0:
        return 0
    else:
        return 1
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y
def main():
    print(AND(3,0.7))

main()
