import numpy as np

import pylab as pl


x = [1, 3, 4, 6, 7]

y = [1, 3, 2, 4, 3]


# Trazimo koeficijente regresijskog pravca

koef = np.polyfit(x, y, 1)


# Proslijedino koeficijente poly1d funkciji

pravac = np.poly1d(koef)


print "Koeficijenti regresijskog pravca: ", koef

print "Regresijski pravac: ", pravac


yPravac = pravac(x)


pl.plot(x, y, 'o', x, yPravac, '-')

pl.show()
