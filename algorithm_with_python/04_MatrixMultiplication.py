def matrixmult (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    # python에서는 array가 없으므로 list를 만들어줌
    # # 0으로 초기화
    # [0] * n = [0, 0] ex) n = 2
    # for _ in range(n) ex) n = 2 (0 ~ n-1)
    # [ 0, 0 ]
    # [ 0, 0 ]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


A = [[2,3], [4,1]]
B = [[5,7], [6,8]]
print('A =', A)
print('B =', B)
C = matrixmult(A, B)
print('C =', C)
