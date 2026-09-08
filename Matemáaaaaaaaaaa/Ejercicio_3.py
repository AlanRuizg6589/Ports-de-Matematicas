# 0, 1, 1, 2, 3, 5, 8, 13, ...

Patrones = {

    "F_0" : 0,

    "F_1" : 1

            }


def nueva_sucesión(número : int):

    Patrones["F_" + str(número)] = Patrones["F_" + str(número - 1)] + Patrones["F_" + str(número - 2)]

# Respuesta de la pregunta 1:

for i in range (0, 31):

    if i in [0, 1]:

        continue

    nueva_sucesión(i)

    if i >= 21:
        
        continue
    
    print(f"F_{i} : {Patrones["F_" + str(i)]}")

Suma_total = 0

# Respuesta de la pregunta 2:

for número in range (31):
    
    Suma_total += Patrones["F_" + str(número)]
    
    print(Suma_total)