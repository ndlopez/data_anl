import numpy as np
def num_grad(f,x):
    h=1e-4
    grad=np.zeros_like(x)
    for idx in range(x.size):
        tmp_val=x[idx]
        x[idx]=tmp_val+h #f(x+h) calc
        fxh1=f(x)
        x[idx]=tmp_val-h #f(x-h) calc
        fxh2=f(x)
        grad[idx]=(fxh1-fxh2)/(2*h)
        x[idx]=tmp_val
    return grad
def grad_desc(f,init_x,lr=0.01,step_num=100):
    x=init_x
    for i in range(step_num):
        grad = num_grad(f,x)
        x-=lr*grad
    return x
        
def func_2(x):
    return x[0]**2+x[1]**2
init_x=np.array([-3.0,4.0])
print(num_grad(func_2,np.array([3.0,4.0])))
print(num_grad(func_2,np.array([0.0,2.0])))
print(num_grad(func_2,np.array([3.0,0.0])))
#z=grad_desc(func_2,init_x=init_x,lr=0.1,step_num=100)
#print(z)
#lr is learning risk number gakushuritsu
z=grad_desc(func_2,init_x=init_x,lr=1e-10,step_num=100)
print(z)

