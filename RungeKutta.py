import numpy as np
import pylab as pl
from scipy import integrate

def f(x, y):
    return x + y

def fun(x):
    return 2*np.e**x-x-1
    
x0 = 0.
y0 = fun(x0)
b = 1.
n = 99 
h = (b - x0)/n 

def RungeKutta4(f, x, y, h):
    for i in range(0, n):
        k1 = f(x0, y0)
        k2 = f(x + h/2.0, y + k1*(h/2.0))
        k3 = f(x + h/2.0, y + k2*(h/2.0))
        k4 = f(x + h, y + k3 * h)
        y = (y + h*(k1 + 2.0 * k2 + 2.0 * k3 + k4))/6.0
        x = x + h
        i += 1
    return y
    
y99 = RungeKutta4(f, x0, y0, h)
    
print "Aproksimativna vrijednost pomocu RK metode: ", y99

print "Vrijednost funkcije u tocki x = 1: ", fun(1)

print "Greska za tocku x = 1: ", abs(y99 - fun(1))v
