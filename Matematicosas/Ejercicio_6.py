import numpy
from scipy.optimize import fsolve

import math

u = 0
# E(x) = 200 * math.sqrt(x) + 500

# 1)La variable independiente es la cantidad de servidores activos (x) | la variable dependiente es la energía consumida (kWh).

# 2) Screenshot tomada!!!

# 3) Si en un momento hay 25 servidores activos, la energia utilizada en ese momento es 1500 kWh.

# 4) El numero máximo de servidores que se pueden mantener activo para que no superen los 1900 kWh es de 49 servidores.


def Energía(servidores : int):
    
    return 200 * numpy.sqrt(servidores) + 500 - 1900


print(fsolve(Energía, 0))
