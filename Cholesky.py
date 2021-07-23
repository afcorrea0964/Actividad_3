# Programa Python para descomponer una matriz usando Cholesky
import math
MAX = 100;
def Cholesky(matriz, n):
    lower = [[0 for x in range(n + 1)]
             for y in range(n + 1)];
    # Descomponemos una matriz en triangular inferior
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0;

            # sumatoria para diagonales
            if (j == i):
                for k in range(j):
                    sum1 += pow(lower[j][k], 2);
                lower[j][j] = int(math.sqrt(matriz[j][j] - sum1));
            else:
                # Evaluamos L(i, j)
                # Usando L(j, j)
                for k in range(j):
                    sum1 += (lower[i][k] * lower[j][k]);
                if (lower[j][j] > 0):
                    lower[i][j] = int((matriz[i][j] - sum1) /
                                      lower[j][j]);
    # Visualización de la matriz triangular inferior y su transposición
    print("T. inferior \tTranspuesta");
    for i in range(n):
        # Matriz Triangular inferior
        for j in range(n):
            print(lower[i][j], end="\t");
        print("", end="\t");
    # Transposición de la matriz Triangular inferior
        for j in range(n):
            print(lower[j][i], end="\t");
        print("");
n = 3;
matriz = [[4, 6, 10],
          [6, 25, 19],
          [10, 19, 62]];
print(matriz)
Cholesky(matriz, n);

