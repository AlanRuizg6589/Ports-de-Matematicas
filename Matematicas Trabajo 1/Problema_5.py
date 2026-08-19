import math

def kilometros_en_metro(minutos : float):

    return minutos * 0.4

def kilometros_en_bus(minutos : float):

    return minutos * 0.3

def tiempo_en_metro(kilometros : float):

    return kilometros / 0.4

def tiempo_en_bus(kilometros : float):

    return kilometros / 0.3

print(tiempo_en_bus(6))
print(tiempo_en_metro(6))
# 1) ! ! ! (Ambas screenshots guardadas)

# 2) El dominio de x en la funcion del metro es de la siguiente forma: [0, 648], La razon es que no se considera los lapsos de tiempo en los que el metro se queda esperando (30 segundoos). Si se consideraran, agregarias kilometros extra que nunca recorre. Recuerda, el tiempo en pare no hace que se avances kilometros.

# 3) El grafico del metro no considera los lapsos de 30 segundos, los segundos totales de cada uno considerando los lapsos del metro es de la siguiente forma: | Metro: 888 segundos | Bus: 864 segundos |. El bus es mas conveniente con una diferencia total de 24 segundos.

# 4) El bus se tarda 20 minutos para alcanzar 6 kilometros | El metro se tarda 15 minutos en alcanzar 6 kilometros.