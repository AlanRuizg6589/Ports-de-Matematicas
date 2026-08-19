import math


# y = 1000/(1 + 9 * (e**(-0.5 * x)))

def calculador_de_usuarios_total(meses : float):

    return 1000/(1 + 9 * ((math.e)**(-0.5 * meses)))

def calculador_de_tiempo(usuarios : float):

    if usuarios >= 1000:

        return False
    
    return round(-2 * (math.log(((1000-usuarios)/(usuarios))/(9))), 4)

# 1) La variable dependiente de este ejercicio es la temperatura calculada en °C (y) | La variable independiente de este ejercicio es el tiempo medido en horas (x).

# 2) Transcurrido 12 meses, hay 978 usuarios en la aplicacion hasta ese momento.

# 3) ! ! ! (Screenshot guardada)

# 4) Para llegar a 800 usuarios, tienen que transcurrirr 7.1 meses.
print(calculador_de_tiempo(800))