# ZAD 7

import numpy as np
import pylab as pl
from scipy import integrate

def f(x):
  return x**3 - (2*(x**2)) - 1

def apsD2f(x):
    return 6*x - 4

a = 2.5
b = 3.
eps = 10**-3

# Iz grafa trazimo M2
xtocke = np.linspace(a, b, 100)
pl.plot(xtocke, apsD2f(xtocke), 3, apsD2f(3), 'o')

# Raste na cijelom segmentu pa je maksimum na kraju, za x = 3
m2 = apsD2f(3)

n = np.ceil((b-a) * np.sqrt((m2 * (b-a)) / (eps * 12)))


xtrap = np.linspace(a, b, n+1)
y = f(xtrap)
iPTrap = np.trapz(y, xtrap)
print "Rjesenje integrala koristeci produljenu trapeznu formulu: ", iPTrap
