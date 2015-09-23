import numpy as np
from astropy import units as u
from scipy import integrate as itg

#PARTE 4: INTEGRACIÓN CON SCIPY TRAPZ

datos=np.loadtxt('sun_AM0.dat')
x_values=datos[:,0]*u.nm;
y_values=datos[:,1]*u.W/(u.m**2*u.nm);
I1=itg.trapz(y_values,x_values)
print(I1)
