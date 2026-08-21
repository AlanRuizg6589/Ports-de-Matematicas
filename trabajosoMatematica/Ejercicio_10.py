import math

# G(x) = 0.7 * x ** 2

# F(t) = t * 10

def atleta_1(tiempo : float ) :
    
    return 0.7 * tiempo ** 2

def atleta_2(tiempo : float) :
    
    return tiempo * 10

def tiempo_atleta1(metros : float) :
    
    return abs(math.sqrt((metros / 0.7)))

def tiempo_atleta2(metros : float) :
    
    return metros / 10

# 1) El atleta 2 siempre mantuvo una velocidad constante, la razon de esto es por que su funcion es la lineal. La funcion del atleta 1 es exponencial, creciendo rapidamente.

# 2) Para los primeros 100 metros, el atleta 1 (11.9 segundos) llega primero que el atleta 2 (10 segundos).

# 3) Cuando transcurren 8 segundos las distancia entre los dos es de 35,2 metros (El atleta 1 a corrido 44,8 metros, el atleta 2 a corrido 80 metros) | Cuando transcurren 10 segundos las distancia entre los dos es de 30 metros (El atleta 1 a corrido 70 metros, el atleta 2 a corrido 100 metros)

# 4) En el segundo 8 y segundo 10 el atleta 2 va mas rapido, la razon de esto es porque la velocidad del atleta 1 es exponencial pero con mucha tardesa inicial, la carrera dura 10 segundos y cuando el realmente empieza a tomar la ventaja se a acabdo esta misma.

# Meta para los primeros 100 metros.

print(tiempo_atleta1(100))

print(tiempo_atleta2(100))

print(atleta_1(10))

print(atleta_2(10))
