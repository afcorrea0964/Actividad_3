#mMetodo de Gauss-Seidel
import numpy as np
def G_S(a, b, x, g):   # a es una columna de la matriz de coeficientes b es la aumentada,  x es el valor inicial de la iteración y g es la precisión del cálculo
    x = x.astype(float)   #Establecemos la precisión de x, de modo que se muestren varios decimales en el cálculo de x
    m, n = a.shape
    N = 6                    #Número de Iteraciones
    if (m < n):
        print("Hay un espacio de solución")    # Nos aseguramos  de que el número de ecuaciones sea mayor que el número de incógnitas
    else:
        while True:
            for i in range(n):
                s1 = 0
                tempx = x.copy()        #Registra la respuesta de la última iteración
                for j in range(n):
                    if i != j:
                        s1 += x[j] * a[i][j]
                x[i] = (b[i] - s1) / a[i][i]
                N = 6                                    #Numero de iteraciones
            gap = max(abs(x - tempx))              #Diferencia del último módulo de respuesta
            if gap < g:                          #La precisión cumple con los requisitos, fin
                break
    print(a)
    print(b)
    print("Iteraciones = ", N)
    print(x)
if __name__ == '__main__':            #Cuando el módulo se ejecuta directamente, se ejecutarán los siguientes bloques de código. Cuando se importa el módulo, los bloques de código no se ejecutarán.
    a = np.array([[7,1,-1,2],[1,8,0,-2],[-1,0,4,-1],[2,-2,-1,6]])
    b = np.array([3,-5,4,-3])
    x = np.array([0, 0, 0, 0])          #Iteración valor inicial
    g = 1e-4                                            #La precisión es 0,0001
    G_S(a, b, x, g)
