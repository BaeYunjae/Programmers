def solution(balls, share):
    D = [[0 for j in range(balls + 1)] for i in range(balls + 1)]

    for i in range(balls + 1):
        D[i][1] = i 
        D[i][0] = 1
        D[i][i] = 1

    for i in range(2, balls + 1):
        for j in range(1, i):
            D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

    return D[balls][share]
