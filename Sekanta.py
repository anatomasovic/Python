import numpy as np
import pylab as pl

def f(x):
    return x**2 + 4*np.sin(x) - 1

# Ima dvije nultocke [-2.5, -2], [0, 0.5]
x = np.linspace(-3, 1, 100)

pl.plot(x, f(x), 'r-')
pl.grid()
pl.show()

print "Metoda sekante: \n"

def sekanta(a, b, eps, max_iter = 20):
    print "0. iteracija: ", a
    print "1. iteracija: ", b
    i = 1
    while (abs(a - b) > eps):
        i += 1
        xi = b - f(b)*((b-a)/f(b) - f(a))
        print "%s. iteracija: %s" % (i, xi)
        if f(xi) == 0:
            return xi, i
        else:
            a = b
            b = xi
        if i == max_iter:
             print "Rjesenje na zadanu tocnost nije nadeno.\n"
             break
        return xi, i
    
xn, i = sekanta(-2.5, -2, 10**-8)
print "Rjesenje: 1"
print "x%s = %s" % (i, xn)    

xm, j = sekanta(0, 0.5, 10**-8)
print "Rjesenje: 2"
print "x%s = %s" % (j, xm) 

x = np.linspace(-3, 1, 100)

pl.plot(x, f(x), 'r-', xn, f(xn), 'm^', xm, f(xm), 'm^')
pl.grid()
pl.show()
