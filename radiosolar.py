import numpy as np
from astropy import constants as ct
from astropy import units as u

#PARTE 3: RADIO SOLAR

datos=np.loadtxt('sun_AM0.dat')
x_values=datos[:,0]*u.nm;
y_values=datos[:,1]*u.W/(u.m**2*u.nm);
n=len(x_values)
suma=0
for i in range(0,n-1): #en unidades SI
    base=x_values[i+1]-x_values[i]
    area=((y_values[i]+y_values[i+1])/2)*base
    suma=suma+area
print(suma)
T=5778*u.K
r_s=((suma)**(0.5)*ct.au)/((ct.sigma_sb)**(0.5)*T**2)
print(r_s)
