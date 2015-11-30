import numpy as np

import pylab as pl


x = [15, 22, 25, 30, 40, 45, 50, 60, 70, 80, 95, 100, 120, 130, 150]

y = [80, 95, 100, 120, 110, 145, 130, 180, 210, 200, 280, 320, 350, 375, 480]


# Trazimo koeficijente regresijskog pravca

koef = np.polyfit(x, y, 1)


# Proslijedino koeficijente poly1d funkciji

pravac = np.poly1d(koef)


print "Koeficijenti regresijskog pravca: ", koef

print "Regresijski pravac: ", pravac


yPravac = pravac(x)


pl.plot(x, y, 'o', x, yPravac, '-')

pl.show()


print "Kada bi u marketing bilo ulozeno 220 tisuca, profit bi iznosio:", pravac(220)
