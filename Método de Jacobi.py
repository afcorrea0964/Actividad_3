import numpy as np
from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A,b,N=100,x=None):
    """Resolvemos la ecuación Ax = b mediante el método iterativo de Jacobi ."""
    # Creamos una suposición inicial si es necesario
    if x is None:
        x = zeros(len(A[0]))

    # Creamos un vector de los elementos diagonales de A  y restamos  de A
    D = diag(A)
    R = A - diagflat(D)

    # Iteramos para N veces
    for i in range(N):
         x = (b - dot(R,x)) / D
    return x

A = np.array([[7.0,1.0,-1.0,2.0],[1.0,8.0,0.0,-2.0],[-1,0,4,-1],[2,-2,-1,6]])
b = np.array([3,-5,4,-3])
guess = np.array([0,0,0,0])

sol = jacobi(A,b,N=10,x=guess)

print ("A:")
pprint(A)

print ("b:")
pprint(b)

print ("x:")
pprint(sol)