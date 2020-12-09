def queens(n, i, col):
    if promising(i, col):
        if i == n - 1:
            for c in col:
                print(c, end=' ')
            print()
        else:
            for j in range(n):
                col[i + 1] = j
                queens(n, i + 1, col)


def promising(i, col):
    k = 0
    switch = True
    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False
        k += 1
    return switch


if __name__ == "__main__":
    n = 5
    col = [0] * n
    queens(n, -1, col)