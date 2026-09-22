"""
3. Impacto de una campaña publicitaria en redes sociales
Una agencia de marketing digital ha analizado la efectividad de una campaña publicitaria en
video. Estudió la relación entre la cantidad de visualizaciones (clics) que recibe un anuncio y los
ingresos netos generados por las ventas asociadas.
Los ingresos pueden modelarse mediante la función:

R(x) = -0,002x^2 + 1,2x

donde x representa la cantidad de usuarios que interactúan con el anuncio, medida en cientos de
personas (o miles de impresiones), y R(x) representa la rentabilidad o ganancia neta obtenida,
medida en millones de pesos.

• a) Identifique la variable independiente y la variable dependiente, indicando la unidad de
medida de cada una.

• b) Determine el dominio de la función considerando el contexto de la situación. Explique
por qué no todos los números reales representan cantidades posibles de usuarios.

• c) Determine la cantidad de usuarios/interacciones que se deben alcanzar para obtener la
rentabilidad máxima.

• d) Determine el valor de la rentabilidad máxima.

• e) Determine para qué cantidad de interacciones la rentabilidad es nula.

• f) Interprete el significado de los resultados obtenidos en el contexto de la situación.

"""

def ganancias(vistas : int):

    return ((-0.002 * (vistas ** 2)) + (1.2 * vistas))

print(ganancias(600))
# R(x) = ((-0.002 * (x ** 2)) + (1.2 * x))

# 1) La variable independiente es la cantidad de usuarios que dan click a la pagina. | La variable dependiente es la ganancia neta obtenida.

# 2) El dominio sería el siguiente: x = [0, x-máx] con x siendo un número entero. La razón del x-máx es, depende de la cantidad de personas con la que se va a probar el proyecto. No porque la ganancia sea negativa, significa que se va a parar la campaña publicitaria (recuerda que existen campañas en el mundo real que pierden dinero a proposito).

# 3) Se requieren 300.000 vistas de personas para alcanzar el profit más alto de todos.

# 4) El maximo de ganancias es de 180 millones de pesos.

# 5) Cuando hay 0 vistade usuarios la rentabilidad es nula. Y a su vez cuando la vista de los usuarios es de 600.000, la rentabilidad también es 0.

# 6) Entre ese dominio x = ]0, 300] las ganancias son positivas para la empresa, y en el dominio ]300, 600] las ganancias van en caida.
