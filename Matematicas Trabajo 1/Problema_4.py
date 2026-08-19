def kilometros_de_cable_completados(horas : float):

    if horas < 0 or horas > (6600/1.85):
        
        return False
    
    return horas * 1.85

def horas_transcurridas(kilometros_de_cable : float):

    if kilometros_de_cable < 0 or kilometros_de_cable  > (6600):
        
        return False
    
    return kilometros_de_cable  / 1.85

# 1) La funcion es de la forma y = 1,85x, con "y" siendo los kilometros del cable | "x" siendo el tiempo medido en horas.

# 2) La variable dependiente es el tamaño del cable en kilometros (y) | La variable independiente es el tiempo medido en horas (x).

# 3) El domnio de la funcion es de la siguiente forma = [0, 3567,567 (Todos los digitos despues del punto son periodicos)]

# 4) ! ! ! (Screenshot guardada)

# 5) Al pasar 148 horas se instalaron en total 273,8 kilometros. Al transcurrir 2300 horas se instalan 4355 kilometros en total.

# 6) Si se instalan 3.480 kilometros de cable, entonces pasan 1881,081 horas en total.

# 7) Para que se complete la obra tienen que pasar 3567,567 horas en total.