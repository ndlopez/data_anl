"""Permutation-resampling is a form of simualation-based statistical calc, 
and is often used to eval the p-value for the diff between 2 groups, under 
the null hyp that the groups are invariant under label permut. 
"""
import numpy as np
import numpy.random as npr
import pylab

def permut_res(case,control,num_samples,statistic):
    #Ret p-value that stat for case is diff drom stat for control
    obs_diff=abs(statistic(case)-statistic(control))
    num_case=len(case)
    combi=np.concatenate([case,control])
    diffs=[]
    for i in range(num_samples):
        xs=npr.permutation(combi)
        diff=np.mean(xs[:num_case])-np.mean(xs[num_case:])
        diffs.append(diff)
    pval=(np.sum(diffs>obs_diff)+np.sum(diffs<-obs_diff))/float(num_samples)
    return pval,obs_diff,diffs

if __name__=='__main__':
    #making up some data
    case=[94,38,23,197,99,16,141]
    control=[52,10,40,104,51,27,146,30,46]
    #find p-value by permut-resampling
    pval,obs_diff,diffs=permut_res(case,control,10000,np.mean)
    #plotting
    pylab.title('empirical null distro for diffs in mean')
    pylab.hist(diffs,bins=100,histtype='step',normed=True)
    pylab.axvline(obs_diff,c='red',label='diff')
    pylab.axvline(-obs_diff,c='green',label='-diff')
    pylab.text(60,0.01,'p=%.3f'%pval,fontsize=16)
    pylab.legend()
    pylab.savefig('permut-res.png')
    
