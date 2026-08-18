def tiempo_de_transferencia(GB : float):
    
    return 2 * GB

def GB(tiempo_de_transferencia : float):

    return (tiempo_de_transferencia / 2)

# Forma de la funcion; y = 2 * x

# RESPUESTAS DE CADA PREGUNTA:

# 1) La variable independiente es la cantidad de datos transferidos (GB) | La variable dependiente es el tiempo de transferencia (min).

# 2) La funcion es T(x) = 2 * x

# 3) La pendiente de la funcion es 2. Esto significa que por cualquier valor de GB transferidos, el tiempo de transferencia siempre sera el doble.

# 4) Una trasnferencia de 73,2 GB toma 146,4 min.

# 5) En 123,5 min se pueden transferir 61,75 GB.

# 6) (Screenshot tomada)! 

print(tiempo_de_transferencia(73.2))

print(GB(123.5))