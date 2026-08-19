import math

def calculador_consumo_energia(horas : float):

    return 50 * math.log(horas + 1) + 200

def calculador_horas(kWh : float):

    return (math.e ** (((kWh - 200)) / 50)) - 1

# 1) La variable independiente de esta funcion es la cantidad de horas transcurridas. | La variable dependiente de esta funcion es el consumo de energia (kWh).

# 2) El consumo de energia transucurrido 5 horas es de 289.6 kWh.

# 3) La cantidad de horas transcurridas necesarias para que el consumo de energia sea de 350 kWh es de 19.08 horas.

# 4) ! ! ! (Screenshot guardada)

print(calculador_consumo_energia(5))

print(calculador_horas(350))