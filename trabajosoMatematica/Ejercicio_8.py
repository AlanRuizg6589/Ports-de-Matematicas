# funcion de la siguiente forma: y = (x / 20) + 2

def tiempoDeEjecucion(elementos : float):
    
    return (elementos / 20) + 2

def elementoDeEntrada(tiempo : float):
    
    return 20 * (tiempo - 2)

# 1) La funcion del problema es representada de la siguiente forma: T(x) = (x / 20) + 2

# 2) El tiempo de ejecucion para 67 elementos es de 5,35 milisegundos.

# 3) Para que el tiempo sea de 6.4 milisegundos, la cantidad de elementos de entrada tiene que ser 88.

print(tiempoDeEjecucion(67))

print(elementoDeEntrada(6.4))