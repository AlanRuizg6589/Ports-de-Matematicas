# 0, 1, 1, 2, 3, 5, 8, 13, ...

Patrones = {

    "F_0" : 0,

    "F_1" : 1

            }


def nueva_sucesión(número : int):

    Patrones["F_" + str(número)] = Patrones["F_" + str(número - 1)] + Patrones["F_" + str(número - 2)]

for i in range (0, 21):

    if i in [0, 1]:

        continue

    nueva_sucesión(i)

    print(f"F_{i} : {Patrones["F_" + str(i)]}")

print(Patrones)