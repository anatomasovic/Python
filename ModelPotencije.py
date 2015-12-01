import numpy as np
import pylab as pl


x = [0.5, 1.0, 1.5, 2.0, 2.5] 
y = [0.49, 1.60, 3.36, 6.44, 10.16]

# Dvije liste na temelju kojih trazimo linearan model
lnx = np.log(x)
lny = np.log(y)

koef = np.polyfit(lnx, lny, 1)

regpravac = np.poly1d(koef)

# Isto kao kod eksponencijalnog modela
a = exp(regpravac[0])
b = regpravac[1]

print "Jednadzba krivulje regresije: y = %s * e^(%s*x)" % (a, b) 

def PotFja(x):
    return a*x**(b)

xtocke = np.linspace(min(x), max(x) + 2, 100)
yPot = PotFja(xtocke)

pl.plot(x, y, 'o', xtocke, yPot, '-')
pl.show()

