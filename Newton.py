import numpy as np
import pylab as pl

def f(x):
    return x**5 - x**3 - 2

# Granice su proizvoljne - trebamo vidjeti sjeciste
x = np.linspace(-2, 2, 100)

pl.plot(x, f(x), 'r-')
pl.grid()
pl.show()

