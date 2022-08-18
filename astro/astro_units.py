from __future__ import print_function,division
import math
import numpy as np
np.random.seed(276453)
import matplotlib.pyplot as plt
import astropy.units as u
from astropy.constants import G,h,k_B

Reff=29*u.pc #galaxy's effective radius
Reff=u.Quantity(29,unit=u.pc)
print("""half light radius value: {0} unit:{1}""".format(Reff.value,Reff.unit))
print("{0:.3g}".format(Reff.to(u.m)))
vmean=206
sigin=4.3 #dispersion velocity
v=np.random.normal(vmean,sigin,500)*u.km/u.s
print("Gravitational constant",G)
print("""First 10 radial velocity measure {0}{1}""".format(v[:10],v.to(u.m/u.s)[:10]))
'''plt.figure()
plt.hist(v, bins=20,histtype="step")
plt.xlabel("Velocity (km/s)")
plt.ylabel("N")
plt.show()'''
sigma=np.sqrt(np.sum((v-np.mean(v))**2)/np.size(v))
print("Velocity dispersion: {0:.2f}".format(sigma))
M=4*sigma**2*Reff/G #spheroidal galaxy mass
print("Mass",M)
print(M.decompose())
print("""Galaxy mass in solar units: {0:.3g} \nSI units: {1:.3g} \nCGS units: {2:.3g}""".format(M.to(u.Msun),M.si,M.cgs))
print("Log10 of M",np.log10(M/u.Msun))
