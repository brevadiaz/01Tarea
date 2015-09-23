import numpy as np
from astropy import constants as ct
from astropy import units as u

#PARTE 3: RADIO SOLAR
#se calcula usando la primera y segunda intetral
datos=np.loadtxt('sun_AM0.dat')
x_values=datos[:,0]*u.nm;
y_values=datos[:,1]*u.W/(u.m**2*u.nm);
n=len(x_values)
suma=0
for i in range(0,n-1): #método del trapecio
    base=x_values[i+1]-x_values[i]
    area=((y_values[i]+y_values[i+1])/2)*base
    suma=suma+area #luminosidad total del sol
T=5778*u.K
x_values2=np.linspace(0.00001,np.pi/2,10000);
y_values2=(((np.tan(x_values2))**3)+((np.tan(x_values2))**5))/(np.exp(np.tan(x_values2))-1);
m=len(x_values2)
base2=x_values2[1]-x_values2[0] #el mismo paso siempre
suma2=0
for i in range (0,m-1): #metodo del trapecio
    area2=((y_values2[i+1]+y_values2[i])*base2)/2
    suma2=suma2+area2
integral=((2*np.pi*ct.h)/(ct.c)**2)*((ct.k_B*T/ct.h)**4)*suma2 #energía total
r_s=(suma/integral)**(0.5)*ct.au
print(r_s)
