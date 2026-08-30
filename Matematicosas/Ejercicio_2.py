from scipy.optimize import fsolve

y = 0

# función h(x) = 2 * ((x - 2) ** 2)

# función i(x) = x + 1

# h(x) <= i(x) | 2 * ((x - 2) ** 2) <= x + 1 
def función_h(x):
    
    return 2 * ((x - 2) ** 2) - 50

def función_i(x):
    
    return x + 1

for i in range(100):
    
    print(fsolve(función_h, 0))
    
    y += 1
    
# 1) Screenshot tomada ! ! !

# 2) La función h(x) intersecta el eje x en el punto (2, 0); la función i(x) intersecta al eje y en el punto (-1, 0).

# 3) Las dos funciones representadas en el ejercicio se intersectan en dos puntos especificos: x = 1; x = 3,5.

# 4) Para los valores de x en los que ocurre que h(x) <= i(x) se demuestra con el siguiente intervalo: 3,5 >= x >= 1

# 5) La función h(x) es igual a 50 con x = -3.
