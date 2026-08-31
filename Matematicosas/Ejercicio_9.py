import numpy

from scipy.optimize import fsolve

import math


# f(x) = numpy.sqrt((500 * x) + 2000)

# g(x) = numpy.sqrt((800 * x) + 1000)

# 1) Cuando x = (10/3) o 3.33333 luz (en lux) ambas funciones tienen la misma tasa de crecimiento.

# 2) La alga de la función f(x) crece más rápidamente cuando x < (10/3), pero si x sigue aumentando, la alga de la función g(x) crece más a largo plazo.

def Balanza(x):
    
    return numpy.sqrt((500 * x) + 2000) - numpy.sqrt((800 * x) + 1000)

print(fsolve(Balanza, 0))


print(Balanza((10/3)))