def opt(X, Y, i, j):
    m = len(X)
    n = len(Y)
    if i == m:
        opt_val = 2 * (n - j)
    elif j == n:
        opt_val = 2 * (m - i)
    else:
        if X[i] == Y[j]:
            penalty = 0
        else:
            penalty = 1
        opt_val = min(opt(X, Y, i + 1, j + 1) + penalty, opt(X, Y, i + 1, j) + 2, opt(X, Y, i, j + 1) + 2)
    return opt_val


def opt2(X, Y, i, j):
    m = len(X) + 1
    n = len(Y) + 1
    M = [[0] * n for _ in range(m)]

    dim = m + n - 1

    last = 0
    for k in reversed(range(dim)):
        for j in reversed(range(k + 1)):
            i = k - j
            if i < m and j < n:
                if i == m - 1 or j == n - 1:
                    M[i][j] = last
                else:
                    if X[i] == Y[j]:
                        penalty = 0
                    else:
                        penalty = 1
                    M[i][j] = min(M[i + 1][j + 1] + penalty, M[i + 1][j] + 2, M[i][j + 1] + 2)
        last += 2
    
    return M


def print_matrix(M):
    for row in M:
        for elem in row:
            print(f'{elem:5}', end=' ')
        print()


if __name__ == '__main__':
    X = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
    Y = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']

    M = opt2(X, Y, 0, 0)

    m = len(X) + 1
    n = len(Y) + 1
    dim = m + n - 1

    X2 = list()
    Y2 = list()
    i = j = 0
    while i < m - 1 and j < n - 1:
        cost = M[i][j]
        if cost == M[i + 1][j] + 2:
            X2.append(X[i])
            Y2.append('-')
            i += 1
        elif cost == M[i][j + 1] + 2:
            X2.append('-')
            Y2.append(Y[i])
            j += 1
        else:
            X2.append(X[i])
            Y2.append(Y[j])
            i += 1
            j += 1
    
    print(X2)
    print(Y2)