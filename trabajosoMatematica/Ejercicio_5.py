def servidoresTotales(milesDeDolares : float):

    return (milesDeDolares - 10) / 1.5

def milesDeDolares(servidoresActivos : int):

    return servidoresActivos * 1.5 + 10

# y = 1.5 * x + 10

# 1) La variable independiente de la funcion es la cantidad de servidores (x) | La variable dependiente de la funcion es el cosot de la operacion mensual (miles de dolares).

# 2) La pendiente del problema representa el costo (en miles de dolares) de cada servidor independiente.

# 3) El intercepto representa el costo base de la operacion, sin ningun servidor activo. Se mantiene constante por cada servidor activo nuevo.

# 4) Si hay 47 servidores activos, el costo de la operacion es de 80.5 miles de dolares.

# 5) Si el costo actual es de 92,500 miles de dolares, entonces hay 55 servidores activos.

print(milesDeDolares(47))

print(servidoresTotales(92.500))