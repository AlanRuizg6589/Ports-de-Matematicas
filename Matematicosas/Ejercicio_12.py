"""

1) si x = 0; T(x) = 0

   si x = 1; T(x) = 70.000

   si x = 2; T(x) = 140.000

   si x = 3; T(x) = 210.000

   si x = 4; T(x) = 264.000

   si x = 5; T(x) = 318.000

   si x = 6; T(x) = 372.000

   si x = 7; T(x) = 426.000

2) Si 0 <= x <= 3; (70.000 * x)

   Si x > 3; (210.000 + (54.000 * x))

3) En el tramo del día 1 hasta el día 3 avanza más rápido. Desde el día 4 en adelante avanza de 54.000 a 54.0000, la constante que tiene su función es solo el total de los 3 primeros días, pero es menos caro.
   
"""