import numpy as np
import pylab as pl

# Eksponencijalni model preko linearnog

x = [0, 2, 4, 6, 8, 10, 12, 16] 
y = [25, 36, 52, 68, 85, 104, 142, 260]


# Pretvorba u linearni model
lny = np.log(y)

# Koeficijeni linearne regresije
koef = np.polyfit(x, lny, 1)

regpravac = np.poly1d(koef)

# Eksponencijalni model
a = exp(regpravac[0])
b = regpravac[1]

print "Jednadzba krivulje regresije: y = %s * e^(%s*x)" % (a, b) 


# Definiramo funkciju za crtanje
def ExpFja(x):
    return a*e**(b*x) # prima vrijeme kao argument, a vrijednost je procijenjeni broj organizama
    
# Definiramo novu listu tocaka jer ne crtamo pravac
xtocke = np.linspace(min(x), max(x), 100)
yExp = ExpFja(xtocke)

pl.plot(x, y, 'o', xtocke, yExp, '-')
pl.show()

print 'Procijenjeni broj mikroorganizama nakon 18 sati: ', ExpFja(18)
