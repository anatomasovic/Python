# ZAD 6
import numpy as np
import pylab as pl
from scipy import integrate

def f(x):
  return np.sin(x)

def apsD4f(x):
    return abs(np.sin(x))

a = 0.
b = 3.
eps = 10**-4

xtocke = np.linspace(a, b, 100)
pl.plot(xtocke, apsD4f(xtocke), np.pi/2, apsD4f(np.pi/2), 'o')
pl.grid()
pl.show()

# Trazena tocka je za x = pi/2
m4 = apsD4f(np.pi/2)
n = np.ceil((b-a) * (((m4 * (b-a)) / (eps*180))**(1./4)))

if (n % 2 != 0):
    print "Dobili smo ", n, " podsegmenata - neparan broj, dodajemo jos 1:"
    m = n+1
    print "Broj podsegmenata na koji treba podijeliti pocetni interval: ", m

else:
    m = n
    print "Broj podsegmenata na koji treba podijeliti pocetni interval: ", m
    
# Simpsonova funkcija

x = np.linspace(a, b, m+1)
y = f(x)
isimps = integrate.simps(y, x)
print "Rjesenje integrala koristeci Simpsonovu: ", isimps

# Produljena Simpsonova

iPSimps = 0
h = (b -a)/m
for i in range(0, int(m-1), 2):
    iPSimps = iPSimps + h/3. * (y[i] + 4*y[i+1] + y[i+2])

print "Rjesenje integrala koristeci produljenu Simpsonovu: ", iPSimps

integral = -np.cos(3.) + np.cos(0.)
print "Rjesenje integrala: ", integral 

# Apsolutna greska 

print "Apsolutna greska produljene Simpsonove: ", (b-a)/180 * h**4 * m4
