import numpy as np

def matrix_multiply_optimized(A, B):
    n = A.shape[0]
    C = np.zeros((n, n))

    # Transponer la matriz B
    B_T = B.T

    # Multiplicación de matrices optimizada
    for i in range(n):
        for j in range(n):
            C[i, j] = np.dot(A[i, :], B_T[j, :])

    return C
