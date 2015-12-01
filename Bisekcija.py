import numpy as np
import pylab as pl

# Granice su proizvoljne - trebamo vidjeti sjeciste
x = np.linspace(-2, 2, 100)

# Prva fja: y = x
# Druga fja y = e^-x
pl.plot(x, x, 'r-', x, e**(-x), 'b-')
pl.grid()
pl.show()

# Odrediti sto manji interval u kojem je ksi na temelju sjecista fja na grafu
# Iz grafa vidimo da je nultocka unutar [0.5,1]
a = 0.5
b = 1

# Metodu bisekcije primjenjujemo na f(x) = x-e^-x (ako nam nije definirana posebna funkcija)
def f(x):
    return x - (e**(-x))

print 'Metoda bisekcije:'

# Eps - tocnost; maxiter - maksimalni broj iteracija
def bisekcija(a, b, eps, maxiter = 30):
    poloviste = (a + b)/2.0
    i = 0  # Ispisujemo nultu iteraciju - x0
    print "%s. iteracija: %s" % (i, poloviste)
    while (((b-a)/2) > eps): # Dok je duljina segmenta veca od eps
        if f(a)*f(poloviste) < 0: 
            b = poloviste
        else:
            a = poloviste
        poloviste = (a + b)/2.0
        i = i + 1
        print "%s. iteracija: %s" % (i, poloviste)
    return poloviste, i
        
xn, i = bisekcija(a, b, 10**-8)

print 'Rjesenje: '
print "x%s = %s" % (i, xn)
