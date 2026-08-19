def calculador_de_temperatura(Hora : float):

    if Hora < 0 or Hora > 9:

        return False
    
    return (-(Hora**2)/2) + 3 * Hora + 20


print(calculador_de_temperatura(3))

#  funcion[y = (-(x**2)/2) + 3 * x + 20]

# x = [0,9]

# 1) La variable dependiente de este ejercicio es la temperatura calculada en °C (y) | La variable independiente de este ejercicio es el tiempo medido en horas (x).

# 2) El dominio de x es de la siguiente forma: [0,9].

# 3) ! ! ! (Screenshot guardada)

# 4) El servido alcanza su temperatura maxima pasada 3 horas exactas desde su apertura. La temperatura es de 24.5 °C.

# 5) La temperatura a las 13:00 fue de 22.5 °C | La temperatura al finalizar la jornada fue de 6.5 °C.