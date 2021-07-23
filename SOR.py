# Método de iteración de sobre-relajación sucesiva (SOR)
import math
#Definimos la matriz para que se pueda ingresar de cualquier tamaño, ademas de esta manera
#ingresamos la matriz aumentada en la misma matriz, no hay necidad de ingresarla aparte.
def column(m, c):
    return [m[i][c] for i in range(len(m))]
def row(m, r):
    return m[r][:]
def height(m):
    return len(m)
def width(m):
    return len(m[0])
def sor(m, w=1.1, x0=None, error=1e-4, iteracion=10):
#Imprimimos el factor de relajación (w), el error y el número de iteraciones, ademas de la matriz m
    print("w =",w)
    print("error =",error)
    print("iteracion= ",iteracion)
    print(m)
#Construcción de la formula para obtener la formula iterativa
    n = height(m)
    x0 = [0] * n if x0 == None else x0
    x1 = x0[:]
    for __ in range(iteracion):
        for i in range(n):
            s = sum(-m[i][j] * x1[j] for j in range(n) if i != j) #Determinamos si se cumplen los requisitos de precisión
            x1[i] = w * (m[i][n] + s) / m[i][i] + (1 - w) * x0[i] #Calculo iterativo
        if all(abs(x1[i] - x0[i]) < error for i in range(n)):
            return x1
        x0 = x1[:]
    raise ValueError('La solución no converge')
if __name__ == '__main__':
    m = [[7, 1, -1, 2,3], [1, 8, 0, -2,-5 ], [-1, 0, 4, -1,4 ], [2, -2, -1, 6,-3]] #Ingresamos la matriz que queramos
    print(sor(m)) # Por último imprimimos los resultados



