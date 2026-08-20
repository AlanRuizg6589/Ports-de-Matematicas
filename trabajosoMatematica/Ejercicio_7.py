def tiempoTransucurrido(valorResidual : float):

    return (valorResidual - 10) / -1.2

def valorResidual(años : float):

    return años * -1.2 + 10

# y = -1.2 * x + 10

# 1) La variable dependiente de esta funcion es valor residual calculado en miles de dolares | La variable independiente es el tiempo calculado en años.

# 2) La pendiente es -1.2 y significa que cada año que transcurre desde la adquisicion de el equipo electronico (No se sabe cual es), su valor anual disminute 1.2 miles de dolares.

# 3) El valor residual inicial de el equipo (el momento que se adquirio) es de 10 miles de dolares.

# 4) Si su valor final del equipo es de 400 dolares entonces el dominio de x se escribe de la siguiente forma: x = [0, 8]; todo en años.

# 5) Si transcurren 3 años y seis meses, el valor residual del equipo electronico es de 3500 dolares.

# 6) Si el valor del equipo en un transcuso de tiempo es de 4000 dolares, entonces han transcurrido 5 años.

# 7) (Screenshot tomada! ! !)

print(valorResidual(3.5))

print(tiempoTransucurrido(4))