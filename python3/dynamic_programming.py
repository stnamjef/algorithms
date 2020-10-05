from queue import PriorityQueue
import numpy as np

INF = 1000000000


# Greedy dijkstra
def naive_dijkstra(W, start):
    N = len(W)
    D = [w for w in W[start]]
    V = [False for _ in range(N)]
    V[start] = True
    for _ in range(N - 2):
        curr = get_small_index(D, V)
        V[curr] = True
        for j in range(N):
            if not V[j]:
                if D[curr] + W[curr][j] < D[j]:
                    D[j] = D[curr] + W[curr][j]
    return D


def get_small_index(D, V):
    min = INF
    idx = 0
    for i in range(len(D)):
        if D[i] < min and not V[i]:
            min = D[i]
            idx = i
    return idx


# NlogN dijkstra
def dijkstra(W, v1):
    D = [INF for _ in range(len(W))]
    D[v1] = 0
    Q = PriorityQueue()
    Q.put((0, v1))
    while not Q.empty():
        v1_to_v2, v2 = Q.get()
        if D[v2] < v1_to_v2:
            continue
        for v3, v2_to_v3 in W[v2]:
            v1_to_v3 = v1_to_v2 + v2_to_v3
            if D[v3] > v1_to_v3:
                D[v3] = v1_to_v3
                Q.put((v1_to_v3, v3))
    return D



# Floyd algorithm
def floyd(W):
    N = len(W)
    D = W
    P = [[0] * len(W) for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k + 1
    return (D, P)


def path(P, i, j):
    if P[i - 1][j - 1] != 0:
        path(P, i, P[i - 1][j - 1])
        print(f' v{P[i - 1][j - 1]}', end='')
        path(P, P[i - 1][j - 1], j)


if __name__ == '__main__':
    W1 = list()
    W1.append([0, 2, 5, 1, INF, INF])
    W1.append([2, 0, 3, 2, INF, INF])
    W1.append([5, 3, 0, 3, 1, 5])
    W1.append([1, 2, 3, 0, 1, INF])
    W1.append([INF, INF, 1, 1, 0, 2])
    W1.append([INF, INF, 5, INF, 2, 0])

    D1 = naive_dijkstra(W1, 0)
    print(f'Naive dijkstra: {D1}')

    W2 = list()
    W2.append([(1, 2), (2, 5), (3, 1)])
    W2.append([(0, 2), (2, 3), (3, 2)])
    W2.append([(0, 5), (1, 3), (3, 3), (4, 1), (5, 5)])
    W2.append([(0, 1), (1, 2), (2, 3), (4, 1)])
    W2.append([(2, 1), (3, 1), (5, 2)])
    W2.append([(2, 5), (4, 2)])

    D2 = dijkstra(W2, 0)
    print(f'NlogN dijkstra: {D2}')

    D3, P = floyd(W1)
    print(f'floyd: {D3[0]}')
    print(f'Path from 1 to 3: v1', end='')
    path(P, 1, 3)
    print(' v3')