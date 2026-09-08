def númeroPar(n : int):
    
    if n >= 1:
        
        return (n * 2)
    
    else:
        
        return False

# 1.- El valor del decimo número es 20.

# Procedimiento de la pregunta 2:

sumaTotal = 0

for número in range(1, 101):
    
    sumaTotal += númeroPar(número)

print(sumaTotal)

# 2.- La suma de los primeros 100 números pares es 10.100

# 3.- Se encuentra en el la posición 29.