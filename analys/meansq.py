import numpy as np
def mean_sq_error(y,t):
    return 0.5*np.sum((y-t)**2)
def cross_entropy(y,t):
    delta=1e-7
    return -np.sum(t*np.log(y+delta))
    
def cross_entropy2(y,t):
    if y.ndim==1:
        t=t.reshape(1,t.size)
        y=y.reshape(1,y.size)
    batch_size=y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size),t]))/batch_size
y=[.1,.05,.6,.0,.05,.1,0.0,.1,0.0,0.0]
t=[0,0,1,0,0,0,0,0,0,0]
dell=mean_sq_error(np.array(y),np.array(t))
entr=cross_entropy(np.array(y),np.array(t))
print(dell,entr)
entr=cross_entropy2(np.array(y),np.array(t))
print(entr)
