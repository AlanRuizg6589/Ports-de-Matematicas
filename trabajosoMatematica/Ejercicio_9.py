# La funcion es de la siguiente forma: y = -10 * x + 500

# 1) La forma algebraica es de la siguiente forma: y = -10 * x + 500

# 2) La pendiente es -10; Esto se puede interpretar que por cada mes que transcurre, el gasto electrico disminuye 10.

# 3) El consumo de energia transcurrido un año es de 380 kWh.

# 4) Para que el consumo de energia sea 200 kWh, tienen que pasar en total 30 meses.

def tiempoTranscurrido(consumoEnergia : float) :
    
    return (consumoEnergia - 500) / -10

def consumoEnergia(tiempoTranscurrido : float) :
    
    return (- 10 * tiempoTranscurrido) + 500

print(consumoEnergia(12))

print(tiempoTranscurrido(200))