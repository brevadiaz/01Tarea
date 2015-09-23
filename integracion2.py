import numpy as np
from astropy import constants as ct
from astropy import units as u

#PARTE 3: INTEGRACIÓN DE LA FUNCIÓN DE PLANCK

x_values=np.linspace(0.00001,np.pi/2,10000);
y_values=(((np.tan(x_values))**3)+((np.tan(x_values))**5))/(np.exp(np.tan(x_values))-1);
n=len(x_values)
base=x_values[1]-x_values[0] #el mismo paso siempre
suma=0

#metodo del trapecio
for i in range (0,n-1):
    area=((y_values[i+1]+y_values[i])*base)/2
    suma=suma+area
print(suma) #valor de la integral = pi^4/15

#método de simpson
def func(x):
    f=(((np.tan(x))**3)+((np.tan(x))**5))/(np.exp(np.tan(x))-1)
    return f
suma2=0
for i in range(0,n-1):
    area2=(base/6)*(func(x_values[i])+func(x_values[i+1])+4*func((x_values[i]+x_values[i+1])/2))
    suma2=suma2+area2
print(suma2)

T=5778*u.K
integral=((2*np.pi*ct.h)/(ct.c)**2)*((ct.k_B*T/ct.h)**4)*suma
print(integral)
integral2=integral.to('erg/cm2 s') #en unidades cgs
print(integral2)
