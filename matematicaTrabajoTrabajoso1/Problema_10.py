import math

def calculo_porcentaje(semanas : float):

    return 100 * (math.e ** (-0.1 * semanas))

def calculo_semanas(porcentaje : float):

    return -10 * math.log(porcentaje/100)

# 1) La variable independiente de la funcion es el tiempo (calculado en semanas) | La variable dependiente es la carga de trabajo (medida en porcentaje):

# 2) La carga de trabajo al inicio del proyecto (semana 0) fue del 100%.

# 3) La carga de trabajo transcurrido 4 semanas es del 67%.

# 4) Es incorrecto. La carga de trabajo en la semana 12 fue del 30%, no del 20%.

# 5) Si la carga de trabajo es del 55%, entonces han transcurrido en total 6 semanas.

# 6) ! ! ! (Screenshot guardada)

print(calculo_porcentaje(12))

print(calculo_semanas(55))