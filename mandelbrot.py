import numpy as np
import matplotlib.pyplot

def mandel(c, maxiter):
    # Test point c, max number of iterations
    z = complex(0, 0)
    for i in xrange(maxiter):
        z = z**2 + c
        if (abs(z) > 4):
            break
            pass
        pass
    return i
    
x = np.linspace(-2, 4, 13)
y = np.linspace (-2, 2, 9)

for i in x:
    for j in y:
        #print x, y
        pass
    pass

xvalues = np.linspace(-0.22, -0.21, 1000)
yvalues = np.linspace(-0.70, -0.69, 1000)

xlen = len(xvalues)
ylen = len(yvalues)

atlas = np.empty((xlen, ylen))

for ix in xrange(xlen):
    for iy in range(ylen):
        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx, cy)
        atlas[ix, iy] = mandel(c, 120)
        pass
    pass

figsize(10, 10)
matplotlib.pyplot.imshow(atlas.T, interpolation="nearest")