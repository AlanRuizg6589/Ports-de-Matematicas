from scipy.optimize import fsolve

import math

u = 50

# 1) El periodo de tiempo que se calcula las funciones es entre 1960 y 2023. Por lo que el dominio de x se escribe de la siguiente forma: 0 <= x <= 63

# 2) Screenshot tomada!!!

# 3) En los comienzos del 1960, el país con mayor poblacion es Chile, con 19493 miles de poblantes.

# 4) En el año 2000 se espera para Chile una población de 29080.1 miles de poblantes | en el Ecuador se espera 28402.5 miles de poblantes | en Honduras se espera 18434.3 miles de poblantes.

# 5) La población superara la población de Chile despues mientras x > 51.7889; O escrito de forma mas clara, x > 16 de octubre de 2011, 18:30:13

# 6) Entre los años 1960 y 2023, no se espera en ningun solo momento que la población de Honduras supere a la de Chile.

# (Chile) C(x) = (19.493 * ((math.e) ** (0.010 * x)))

# (Ecuador) E(x) = (17.575 * ((math.e) ** (0.012 * x)))

# (Honduras) H(x) = (10.117 * ((math.e) ** (0.015 * x)))

def Chile(años):
    
    return (19493 * ((math.e) ** (0.010 * años)))

def Ecuador(años):
    
    return (17575 * ((math.e) ** (0.012 * años)))

def Honduras(años):
    
    return (10117 * ((math.e) ** (0.015 * años)))

def Igual(x):
    
    return (19493 * ((math.e) ** (0.010 * x))) - (17575 * ((math.e) ** (0.012 * x)))

for i in range(1000):
    
    print(fsolve(Igual, u))
    
    u += 0.01