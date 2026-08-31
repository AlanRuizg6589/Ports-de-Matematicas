from scipy.optimize import fsolve

import math

import numpy

Z = 2.5

# A(t) = ((1.4 * (t ** 4)) + (-2.55 * (t ** 3)) + (-3.37 * (t ** 2)) + (2.75 * t) + 10)

# B(t) = ((t ** 4) + (-2.67 * (t ** 3)) - (t ** 2) + (2 * t) + 20)

# 1) Screenshot tomada!!!

# 2) Transcurridas 3,5 horas, el proceso A filtra con un 79,098 % de eficiencia. El proceso B filtra con un 50,33 % de eficiencia.

# 3) En el punto x = 2,77030513 (Hora) ambas funciones son iguales. La eficiencia en ese punto es del 19.99860 % de eficiencia.

# 4) El proceso A es recomendable aplicarlo cuando x  > 2,77030513 (horas). La razón es porque despues de este punto, la eficiencia es menos tardía que el proceso B.

def solve(t : float): 

    return ((1.4 * (t ** 4)) + (-2.55 * (t ** 3)) + (-3.37 * (t ** 2)) + (2.75 * t) + 10)


print(solve(2.77030513))

