def campañasPublicitariasTotal(vistas : int):

    return (vistas - 500) / 300

def visitasTotales(campañas : int):

    return campañas * 300 + 500

# V(x) = 300 * x + 500

# 1) La variable dependiente de este problema es la cantidad de visitas totales | La variable independiente son la cantidad de campañas hechas.

# 2) El dominio de esta funcion con el caso hipotetico es el siguiente : x = [0, 20]; con x siendo un numero entero.

# 3) La pendiente de la funcion es 300, esto significa que por cada campaña publicitaria hecha, el total de visitas aumenta 300.

# 4) Si se hacen 5 campañas publicitarias, el total de visitas sera de 2000.

# 5) Se necesitan 14 campañas publicitarias para alcanzar 4700 visitas.

print(visitasTotales(5))

print(campañasPublicitariasTotal(4700))