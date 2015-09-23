import numpy as np
from astropy import units as u

#PARTE 2: INTEGRACION DEL ESPECTRO

datos=np.loadtxt('sun_AM0.dat')
x_values=datos[:,0]*u.nm;
y_values=datos[:,1]*u.W/(u.m**2*u.nm);
x_new=x_values.to('um');
y_new=y_values.to('erg/(s cm2 um)');
n=len(x_new);
suma=0;
for i in range(0,n-1): #en unidades cgs
    base=x_new[i+1]-x_new[i]
    area=((y_new[i]+y_new[i+1])/2)*base
    suma=suma+area
print(suma)
suma2=0
for i in range(0,n-1): #en unidades SI
    base2=x_values[i+1]-x_values[i]
    area2=((y_values[i]+y_values[i+1])/2)*base2
    suma2=suma2+area2
print(suma2)
