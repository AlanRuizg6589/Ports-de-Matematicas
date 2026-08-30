from scipy.optimize import fsolve

y = 0

# Funcion 1 : y = -1.5 * x ** 2 + 11.5 * x -15

# Funcion 2 : y = 1.58 * x ** 4 - 19.17 * x ** 3 + 80.92 * x ** 2 - 139.33 * x + 85


#Punto de intersección 1.58 * x ** 4 - 19.17 * x ** 3 + 80.92 * x ** 2 - 139.33 * x + 85 + -1 * (-1.5 * x ** 2 + 11.5 * x -15)

def solve(x): 

    return (1.58 * (x ** 4)) - (19.17 * (x ** 3)) + (80.92 * (x ** 2)) - (139.33 * x) + 85 + (1.5 * (x ** 2)) + (-11.5 * x) + 15

# 1)

# 2) El punto de intersección de ambos puntos son todos los siguientes: x = 1.93880053; x = 2.22824776; x = 2.88136406; x = 5.08449904

print(solve(1.93880053))

for i in range(1000):
    
    print(fsolve(solve, y))
    
    y += 0.01