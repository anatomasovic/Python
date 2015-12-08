import numpy as np
import pylab as pl

def f(x):
    return x**5 - x**3 - 2

# Granice su proizvoljne - trebamo vidjeti sjeciste
x = np.linspace(-2, 2, 100)

pl.plot(x, f(x), 'r-')
pl.grid()
pl.show()

# Polinom ima jednu nultocku

print "Newtonova metoda: "

def df(x):
    return 5*x**4-3*x**2
    
def d2f(x):
    return 20*x**3-6*x

def newton(x, eps, max_iter = 20):
    if f(x)*d2f(x) < 0:
        print "Newtonova metoda ne konvergira"
        # Treba izabrati drugu pocetnu aproksimaciju
    else:
        print "0. iteracija: %s" % x
        i = 1
        while (i <= max_iter):
            if abs(df(x)) < eps:
                print "U tocki x je horizontalna tangenta.\n";
                # U sljedecem koraku bi se dijelilo s nulom, pa izlazimo
                break
            dx = f(x)/df(x)
            x = x - dx # Izracun svake sljedece aproksimacije
            print "%s. iteracija: %s" % (i, x)
            # Dok ne dobijemo da su zadnje dvije iteracije od x udaljene za epsilon
            if abs(dx) < eps:
                return x, i
            else:
                i += 1
        print "Rjesenje na zadanu tocnost nije nadeno u zadanom broju iteracija.\n"
        
# xn = x, i = i (fja vraca dvije vrijednosti)
xn, i = newton(1.5, 10**-3)
print "Rjesenje: "
print "x%s = %s" % (i, xn)

# Crtamo ponovno funkciju s oznacenom aproksimacijom nultocke
x = np.linspace(-2, 2, 100)

pl.plot(x, f(x), 'r-', xn, f(xn), 'y^')
pl.grid()
pl.show()


# Uvjet da derivacija ne smije biti jednaka 0
# zbog zaokruzivanja ga definiramo ovako: f'(x) < eps
# sa newton(1, 10**-3) dobiti cemo takvu situaciju
# mozemo dodati uvjet ako odmah pogodimo nultocku, break


