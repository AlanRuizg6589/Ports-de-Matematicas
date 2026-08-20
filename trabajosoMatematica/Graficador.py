import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 8, 0.01)

valorResidual = -1.2 * t + 10

# Creamos el gráfico
plt.plot(t, valorResidual, color="blue", label="valorResidual ")

plt.xlim(0, 10)
plt.ylim(0, 10)

# Añadimos etiquetas y título
plt.xlabel("x")
plt.ylabel("y")
plt.title("Grafico de la funcion R(t) = -1.2 * t + 10")
# Mostramos la cuadrícula y la leyenda
plt.grid(True)
plt.legend()

# Mostramos el gráfico
plt.show()
