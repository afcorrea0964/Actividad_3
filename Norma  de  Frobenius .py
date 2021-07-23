import numpy as np
import math
def main():
    # 1-D Array
    array_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    # 2-D Array
    array_2d = np.array([[1, 1, 0], [0, 1, -1], [2, 1, 0]])
    print(array_2d)
    # Norma de Frobenius
    fro_norms = np.linalg.norm(array_2d, "fro")
    print("Norma de Frobenius: ", fro_norms)
if __name__ == '__main__':
     main()