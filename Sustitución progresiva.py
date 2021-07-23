# Importamos la biblioteca NumPy
import numpy as np
import sys

# Pedimos al usuario que ingrese el número de incógnitas
n = int(input('Por favor ingrese el número de incógnitas: '))

#Hacemos una matriz de nxn+1 comenzando desde cero para almacenar una nueva matriz
a = np.zeros((n, n + 1))

#Hacemos una matriz de tamaño n iniciando desde cero para almacenar el vector solución
x = np.zeros(n)

# Leemos los coeficientes de la matriz
print('Ingrese los coeficientes de la matriz:')
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

# Aplicamos Susticución progresiva
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('División para cero detectada!')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]


x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

# Mostramos la solución en pantalla
print('\nLa solución es : ')
for i in range(n):
    print('X%d = %0.2f' % (i+1, x[i]), end='\t')