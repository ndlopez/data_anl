"""use of bootstrap to calc 95% confidence interval of a random
sample based on the mean and the std"""
import numpy as np
import numpy.random as npr
import pylab

def bootstrap(data,num_samples,statistic,alpha):
    #Returns bootstrap estimate of 100*(1-alpha) CI for stat
    n=len(data)
    idx=npr.randint(0,n,(num_samples,n))
    samples=data[idx]
    stat=np.sort(statistic(samples,1))
    return (stat[int((alpha/2.0)*num_samples)],stat[int((1-alpha/2.0)*num_samples)])

if __name__=='__main__':
    #data of interest is bimodal and not normal
    x=np.concatenate([npr.normal(3,1,100),npr.normal(6,2,200)])
    #find mean 95% CI and 10^5 bootstrap samples
    low,high=bootstrap(x,100000,np.std,0.05)
    #low,high=bootstrap(x,100000,np.mean,0.05)
    #plotting
    pylab.figure(figsize=(8,4))
    pylab.subplot(121)
    pylab.hist(x,50,histtype='step')
    pylab.title('Hist of data')
    pylab.subplot(122)
    pylab.plot([-0.03,0.03],[np.mean(x),np.mean(x)],'r',linewidth=2)
    pylab.scatter(0.1*(npr.random(len(x))-0.5),x)
    pylab.plot([0.19,0.21],[low,low],'r',linewidth=2)
    pylab.plot([0.19,0.21],[high,high],'r',linewidth=2)
    pylab.plot([0.2,0.2],[low,high],'r',linewidth=2)
    pylab.xlim([-0.2,0.3])
    pylab.title('Bootstrap 95% CI for mean')#95%confidence interval
    pylab.savefig('data_anl.png')
    
