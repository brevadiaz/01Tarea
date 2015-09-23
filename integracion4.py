import numpy as np
from astropy import units as u
from astropy import constants as ct
from scipy import integrate as itg

#PARTE 4: INTEGRACIÓN CON SCIPY QUAD

def funcion(x):
    f=(((np.tan(x))**3)+((np.tan(x))**5))/(np.exp(np.tan(x))-1);
    return f
I1=itg.quad(funcion,0.00001,np.pi/2)
T=5778*u.K
I2=((2*np.pi*ct.h)/(ct.c)**2)*((ct.k_B*T/ct.h)**4)*I1
print(I2)
