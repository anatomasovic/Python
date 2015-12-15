import numpy as np
from scipy import integrate
from scipy import interpolate
import pylab as pl

def f(x):
    return np.log(x)
    
def Absd2f(x): # f''
    return abs(-1/x**2) # abs zato jer za M2 i M4 gledamo apsolutnu
    
def Absd4f(x): # f(IV)
    return abs(-6/x**4)
    
a = 1.
b = 3.
n = 4

h = (b - a)/n # Duljina jednog podsegmenta

x = np.linspace(a, b, n+1)
y = f(x)

# PRVI NACIN - Produljena trapezna
iPTrap = h/2. * (y[0] + y[n] + 2*sum(y[1:4])) # Ne ukljucuje posljednji
print ("Rjesenje integrala koristeci produljenu trapeznu formulu: ", iPTrap)

# Produljena Simpsonova
iPSimps = 0
for i in range(0, n-1, 2):
    iPSimps = iPSimps + h/3. * (y[i] + 4*y[i+1] + y[i+2])

print ("Rjesenje integrala koristeci produljenu Simpsonovu: ", iPSimps)

"""-----------------------------------------------------------------------"""

# DRUGI NACIN - Preko ugradenih funkcija

iTrap = np.trapz(y, x)
print ("Rjesenje integrala koristeci produljenu trapeznu formulu: ", iPTrap)

iSimps = integrate.simps(y, x)
print ("Rjesenje integrala koristeci produljenu Simpsonovu: ", iPSimps)

"""--------------------------------------------------------------------------"""

integral = 3*np.log(3) - np.log(1) - 2
print ("Pravo rjesenje integrala: ", integral)

# Crtamo fje da vidimo gdje je maksimum za M2
xtocke = np.linspace(a-0.5, b, 100)
pl.plot(xtocke, Absd2f(xtocke), 1, Absd2f(1), 'ro')
pl.grid()
pl.show()

M2 = Absd2f(1)
print ("Apsolutna greska produljenje Trapezne: ", (b-a)/12 * h**2 * M2)

# Crtamo za M4
xtocke = np.linspace(a, b, 100)
pl.plot(xtocke, Absd4f(xtocke))
pl.grid()
pl.show()

M4 = Absd4f(1)
print ("Apsolutna greska produljene Simpsonove: ", (b-a)/180 * h**4 * M4)

pl.plot(xtocke, f(xtocke), x, y, 'r-', x, y, 'yo')
pl.fill_between(xtocke, f(xtocke), color='LightGreen')
