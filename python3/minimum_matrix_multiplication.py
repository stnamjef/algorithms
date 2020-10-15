def order(P, i, j):
    if i == j:
        print('A', i, end='')
    else:
        k = P[i][j]
        print('(', end='')
        order(P, i, k)
        order(P, k + 1, j)
        print(')', end='')


def minimum_matrix_multiplication(n, d, M, P):
    for diagnol in range(1, n):
        for i in range(1, n - diagnol + 1):
            j = i + diagnol

            temp = [(M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j], k) for k in range(i, j)]
            min_mult, k = min(temp)
            M[i][j] = min_mult
            P[i][j] = k


def print_matrix(M):
    for row in M:
        for elem in row:
            print(f'{elem:5}', end='')
        print()
    print()


if __name__ == '__main__':
    d = [5, 2, 3, 4, 6, 7, 8]
    n = len(d) - 1

    M = [[0 for j in range(1, n + 2)] for i in range(1, n + 2)]
    P = [[0 for j in range(1, n + 2)] for i in range(1, n + 2)]

    minimum_matrix_multiplication(n, d, M, P)
    
    print_matrix(M)
    print_matrix(P)
    order(P, 1, 6)