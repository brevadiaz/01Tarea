import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

datos=np.loadtxt('sun_AM0.dat')
x_values=datos[:,0]*u.nm;
y_values=datos[:,1]*u.W/(u.m**2*u.nm);
x_new=x_values.to('um');
y_new=y_values.to('erg/(s cm2 um)');

plt.plot(x_new,y_new)
plt.xlim(0,6)
plt.xlabel('Longitud de onda $[\mu m]$')
plt.ylabel('Flujo $[erg$ $s^{-1} cm^{-2} \mu m]$')
plt.title('Espectro del Sol')
plt.savefig('grafico1.png')
plt.show()
