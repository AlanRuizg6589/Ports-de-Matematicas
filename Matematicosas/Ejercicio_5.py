import math

from scipy.optimize import fsolve

# I(x) = ((-20 * x) + 1000)

# C(x) = ((200 * x) + 500)

# 1) La pendiente en la función Ingresos es negativa, esto significa que entre mas tiempo pase, los ingresos seran menores. El tiempo limite lo pone el intercepto 1000.
# ---La pendiente y el intercepto de la función costos por ambas parte son positivos, esto significa que independiente del tiempo transcurrido, aumentara consistentemente el precio de los costos.     

# 2) Screenshot tomada!!!

# 3) El punto de intersección de ambas funciones es en x = 2,272727... (semanas). Esto significa que transcurrido este punto, los ingresos siempre seran menores a los costos de inversión.

# 4) El tiempo maxímo que se le deberia dar a la campaña es de 2,27 semanas, luego de esto la campaña cae en decadencia y los ingresos son mucho menores que los costos totales, podria llevar a la ruina.

def Balanza(x):
    
    return ((-20 * x) + 1000) - ((200 * x) + 500)

print(fsolve(Balanza, 2))