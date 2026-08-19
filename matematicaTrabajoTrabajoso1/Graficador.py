import matplotlib.pyplot as plt
import numpy as np

# Generamos los valores de x entre 0 y 6, con intervalos de 0.01
x = np.arange(0, 6, 0.01)

# Aplicamos la función y = 1850x + 2100
y = 1850 * x + 2100

# Creamos el gráfico
plt.plot(x, y, color="blue", label="y = 1850x + 2100")

# Configuramos los límites de los ejes
plt.xlim(0, 6)
plt.ylim(0, 13000)

# Añadimos etiquetas y título
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico de la función y = 1850x + 2100")

# Mostramos la cuadrícula y la leyenda
plt.grid(True)
plt.legend()

# Mostramos el gráfico
plt.show()