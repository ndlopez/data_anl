import numpy as np
a=np.array([0.3,2.9,4.0])
'''exp_a=np.exp(a)
print(exp_a)
s_expa=np.sum(exp_a)
print(s_expa)
y=exp_a/s_expa
print(y)'''

def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp=np.sum(exp_a)
    y=exp_a/sum_exp
    return y
#a=np.array([1010,1000,990])
#print(np.exp(a)/np.sum(np.exp(a)))e^1000=?overflow!
#c=np.max(a)print(c,a-c)
#print(np.exp(a-c)/np.sum(np.exp(a-c)))
y=softmax(a)
print(y,np.sum(y))
