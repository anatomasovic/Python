import numpy as np
from scipy import integrate
from scipy import interpolate
import pylab as pl

def f(x):
    return np.e**x
    
a = 0.
b = 3.
c = (a + b)/2.

x1 = np.array([a, b])
y1 = f(x1)

x2 = np.array([a, c, b])
y2 = f(x2)

# Primjena trapezne formule
iTrap = np.trapz(y1, x1)
print ("Rjesenje integrala trapeznom: ", iTrap)

iSimps = integrate.simps(y2, x2)
print ("Rjesenje integrala Simpsonom: ", iSimps)

integral = np.e**3 - np.e**0
print ("Pravo rjesenje integrala: ", integral)

prava_greska_t = abs(integral - iTrap)
prava_greska_s = abs(integral - iSimps)


xtocke = np.linspace(a, b, 50)
pl.plot(xtocke, f(xtocke))
pl.grid()
pl.show()

# Maksimum funkcije na intervalu [0, 3] je e^3
# To vidimo s grafa: M2 = M4 = e^3
aps_greska_t = ((b - a)**3.)/12 * np.e**3
aps_greska_s = (((b - a)/2.)**5) * ((np.e**3)/90)

# Funkciju dobivenu Simpsonom aproksimiramo Lagrangeom 
# da ju mozemo nacrtati
pLagrange = interpolate.lagrange(x2, y2)

# Grafovi funkcija koje smo dobili trapeznom i SIimpsonove
pl.plot(xtocke, f(xtocke), x1, y1, x2, y2, 'yo', xtocke, pLagrange(xtocke), 'r')
pl.fill_between(xtocke, f(xtocke), color='LightBlue')
pl.grid()
pl.show()
