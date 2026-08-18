def tiempoDeCarga(MB : float):

    return (MB / 5)

def tiempoDeDescarga(MB : float):

    return ((16 * MB) / 100)

def MBtiempoCarga(segundos : float):

    return segundos * 5

def MBtiempoDescarga(segundos : float):
    
    return ((segundos * 100) / 16)

# RESPUESTA DE CADA PREGUNTA:

# 1) Tiempo de carga f(x) = (x / 5) | Tiempo de descarga g(x) = ((16 * x) / 100)

# 2) La variable independiente de ambas funcion son el tamaño de los archivos (MB) | La variable dependiente de la funcion f(x) es el tiempo de carga (s); La variable dependiente de la funcion g(x) es el tiempo de descarga (s).

# 3) Para un archivo de 750 MB el tiempo de carga es 150 segundos y para el tiempo de descarga es 120 segundos.

# 4) Si el tiempo de carga es de 163 segundos, el tamaño del archivo es de 815 MB.

# 5) La afirmacion es erronea, el tamaño real del archivo con 195 segundos de descarga es de 1218,75 MB.

# 6) (Screenshot tomada)!

print(tiempoDeCarga(750))

print(tiempoDeDescarga(750))

print(MBtiempoCarga(163))

print(MBtiempoDescarga(195))