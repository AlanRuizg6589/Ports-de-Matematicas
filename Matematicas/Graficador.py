
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 50, 0.01)

Carga = x / 5  

Descarga = (16 * x) / 100  

# Creamos el gráfico
plt.plot(x, Carga, color="blue", label="Carga = x / 5")

plt.plot(x, Descarga, color="red", label="Descarga = (16 * x) / 100 ")
plt.xlim(0, 50)
plt.ylim(0, 50)

# Añadimos etiquetas y título
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico de la funcion Carga = x / 5 y Descarga = (16 * x) / 100")
# Mostramos la cuadrícula y la leyenda
plt.grid(True)
plt.legend()

# Mostramos el gráfico
plt.show()
