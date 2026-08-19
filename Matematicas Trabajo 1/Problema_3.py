def calculador_latencia_real(latencia_estimada : int):
    
    return latencia_estimada * (6/5)

latencias_estimadas = [200, 149, 74]


for latencias in latencias_estimadas:
    
    print(f'La latencia estimada de {latencias} milisegundos tiene una latencia real de {round(calculador_latencia_real(latencias), 4)} milisegundos.')