def tiempo_de_ejecucion(cantidad_de_elementos : float):

    return 0.02 * cantidad_de_elementos

def cantidad_de_elementos(tiempo_de_ejecucion : float):

    return (tiempo_de_ejecucion/0.02)

# Forma de la funcion; y = 0,02 * x

# RESPUESTAS DE CADA PREGUNTA:

# 1) La variable indpendiente de esta funcion es la cantidad de elementos de entrada (unidades) | La variable dependiente de esta funcion es el tiempo de ejecucion de los datos (ms).

# 2) La funcion es y = 0,02 * x

# 3) Para la entrada de 1500 elementos, el tiempo de ejecucion es de 30 ms.

# 4) El tamaño de entrada que haria que el tiempo de ejecucion sea de 50 ms es de 2500 elementos.

print(tiempo_de_ejecucion(1500))

print(cantidad_de_elementos(50))