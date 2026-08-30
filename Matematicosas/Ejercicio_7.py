import math

from scipy.optimize import fsolve

# I(x) = ((10 * (x ** 2)) + (50 * x))

# C(x) = ((5 * (x ** 2)) + (80 * x) + 100)

# 1) Se equilibran ambas funciones cuando x = 8.38516481; Es el punto de equilibrio matemático pero no necesariamente pueda ser una cantidad real de subscriptores.

# 2) Cuando 0 <= x < 8.38516481, los costos de operación son mayores a los de ingreso por subscriptores.

def Balanza(x):
    
    return ((5 * (x ** 2)) + (80 * x) + 100) - ((10 * (x ** 2)) + (50 * x))

print(fsolve(Balanza, 7.5))