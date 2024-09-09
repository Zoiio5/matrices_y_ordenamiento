def multiplica_matrices(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])

    C = [[0 for _ in range(p)] for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C
