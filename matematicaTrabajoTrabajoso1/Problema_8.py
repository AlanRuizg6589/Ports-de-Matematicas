import math

def tiempo_de_ejecucion(elementos_ordenados : float):

    return 0.01 * (elementos_ordenados **2) + 0.5 * elementos_ordenados  + 2 

def elementos_ordenados_totales(tiempo_transcurrido : float):

    return (math.sqrt(100 * tiempo_transcurrido + 425)) - 25

# y = 0.01 * (x**2) + 0.5 * x + 2 

# 1) La varible independiente de esta funcion es la cantidad de elementos a ordenar. | La variable dependiente de esta funcion es el tiempo de ejecucion (en segundos).

# 2) El dominio de este ejercicio (Los rangos posibles de x) se escribe de la siguiente forma: [0, 1.562]

# 3) Para ejecutar 1200 elementos, tiene que pasar 15002 segundos (4 horas | 10 minutos | 2 segundos)

# 4) ! ! ! (Screenshot guardada)

# 5) Transcurrido 6 horas, se habran ordenado en total 1445 elementos.

print(elementos_ordenados_totales(25200))