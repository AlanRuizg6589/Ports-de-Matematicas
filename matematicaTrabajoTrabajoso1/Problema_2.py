def Segundos(Segundos : int):

    return Segundos * 100

Tiempo_en_segundos_actual = 0

while Tiempo_en_segundos_actual <= 1000:
    
    print(f'En {Tiempo_en_segundos_actual} segundos se transmiten {Segundos(Tiempo_en_segundos_actual)} Megabites.')
    
    Tiempo_en_segundos_actual += 100