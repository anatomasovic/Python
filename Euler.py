import numpy as np
import pylab as pl
from scipy import integrate

def f(x, y):
    return x + y

# Analiticko rjesenje
def fun(x):
    return 2*np.e**x-x-1
    
# Sto ekvidistantnih tocaka na [0, 1]
x0 = 0.
b = 1.
n = 99 # Jer imamo sto tocaka, pa je 99 intervala
h = (b - x0)/n # Duljina svakog podsegmenta; udaljenost
# svake dvije susjedne tocke

xi = np.linspace(0, 1, n+1) # lista x vrijednosti
yi = np.zeros(n+1)
yi[0] = 1 # Iz pocentog uvjeta

for i in range(1, n+1):
    yi[i] = yi[i-1] + h*f(xi[i-1], yi[i-1])
    
# Najveca greska je na posljednoj tocki u xi
# Gresku nalazimo kao apsolutnu vrijednost analiticki izracunate
# i zadnje iteracije petlje
    
print "Aproksimativna vrijednost pomocu Eulera: ", yi[99]

print "Vrijednost funkcije u tocki x = 1: ", fun(1)

print "Greska za tocku x = 1: ", abs(yi[99] - fun(1))

xtocke = np.linspace(0, 1, 10)
pl.plot(xtocke, fun(xtocke), 'o', xi, yi)
# tocke predstavljaju analiticka rjesenja
pl.grid()
pl.show()
