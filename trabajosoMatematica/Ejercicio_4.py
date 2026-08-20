def usuariosActivos(GB : float):

    return (GB - 2) / 0.5

def memoria(usuariosActivos : int):

    return (usuariosActivos * 0.5) + 2

# Funcion de la forma y = 0.5 * x + 2

# 1) La variable dependiente de la funcion es la memoria (GB) | La variable independiente de la funcion es la cantidad de usuarios activos.

# 2) La pendiente de la funcion es 0.5. Esta funcion se puede interpretar en que cuando no hay usuarios activos, el espacio de la memoria default es 2 GB. Y que cada usuario activo agrega 0.5 GB.

# 3) Cuando no hay usuarios activos, la memoria del servido activa es de 2 GB.

# 4) Cuando hay 637 usuarios activos, la memoria del servidor usada es de 320.5 GB.

# 5) Para el consumo de 32 MB se necesitan 60 usuarios activos.

# 6) NO, la razon es porque la cantidad de usuarios activos no puede ser decimal, son solo numeros enteros.

print(memoria(59.8))

print(usuariosActivos(32))