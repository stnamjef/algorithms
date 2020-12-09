def promising(i, color):
    switch = True
    j = 0
    while j < i and switch:
        if adj[i][j] == 1 and color[i] == color[j]:
            switch = False
        j += 1
    return switch


def graph_color(i, color):
    if promising(i, color):
        if i == n - 1:
            print('sol [ ', end='')
            for c in color:
                print(c, end=' ')
            print(']')
        else:
            # color type: [1, m]
            for j in range(1, m + 1):
                color[i + 1] = j
                graph_color(i + 1, color)


if __name__ == '__main__':
    n = 4
    adj = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]
    color = [0] * n
    m = 3
    graph_color(-1, color)