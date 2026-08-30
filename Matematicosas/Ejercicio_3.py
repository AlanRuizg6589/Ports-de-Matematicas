from scipy.optimize import fsolve

y = 3

def Intersección(x):
    
    return (0.8 * (x ** 3)) + (-10 * x) + 4


# w(x) = (0.6 * (x ** 3)) + 1.5

# t(x) = (0.8 * (x ** 3)) + (-10 * x) + 10

# Considera: -3 <= x <= 4, -4 <= y <= 24

for i in range(100):
    
    print(fsolve(Intersección, y))    
    
    y += 0.01
    
# 1) Screenshoot tomada!!!

# 2) El intervalo en el que w(x) >= t(x) es con el siguiente intervalo: 3.34716475 >= x >= 0.86284792

# 3) Los puntos en los cuales t(x) = 6 son los siguientes; x = 0.40532731; x = 3.31540149;