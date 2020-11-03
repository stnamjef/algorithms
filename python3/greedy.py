def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]


def union(parent, rank, r1, r2):
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]:
                rank[r2] += rank[r1]


def kruskal(graph):

    parent = dict()
    rank = dict()

    for v in graph['vertices']:
        parent[v] = v
        rank[v] = 0
    
    result = set()
    edges = sorted(graph['edges'], key=lambda item: item[0])
    for i in range(len(edges) - 1):
        w, u, v = edges[i]
        r1 = find(parent, u)
        r2 = find(parent, v)
        if r1 != r2:
            result.add((w, u, v))
            union(parent, rank, r1, r2)
    
    return result


INF = 1000000000

def dijkstra(W, start):
    n = len(W)
    T = [0] * n
    D = W[start][:]
    V = [False] * n

    F = set()
    V[start] = True
    for _ in range(n - 1):
        minimum = INF
        vnear = 0
        for i in range(1, n):
            if D[i] < minimum and not V[i]:
                minimum = D[i]
                vnear = i
        F.add((T[vnear], vnear))
        V[vnear] = True
        for i in range(1, n):
            if not V[i] and D[vnear] + W[vnear][i] < D[i]:
                D[i] = D[vnear] + W[vnear][i]
                T[i] = vnear
    return F, D


def dijkstra2(W, start):
    n = len(W)
    touch = [0 for _ in range(n)]
    length = [w for w in W[start]]
    save_length = [w for w in W[start]]

    F = set()
    for _ in range(n - 1):
        minimum = INF
        for j in range(1, n):
            if length[j] >= 0 and length[j] < minimum:
                minimum = length[j]
                vnear = j
        edge = (touch[vnear], vnear)
        F.add(edge)
        for j in range(1, n):
            if length[vnear] + W[vnear][j] < length[j]:
                length[j] = length[vnear] + W[vnear][j]
                save_length[j] = length[j]
                touch[j] = vnear
        length[vnear] = -1
    return F, save_length


if __name__ == '__main__':

    graph = {
        'vertices': ['A', 'B', 'C', 'D', 'E'],
        'edges': set([
            (1, 'A', 'B'),
            (3, 'A', 'C'),
            (3, 'B', 'C'),
            (6, 'B', 'D'),
            (4, 'C', 'D'),
            (2, 'C', 'E'),
            (5, 'D', 'E'),
        ])
    }

    mst = kruskal(graph)
    print(mst)

    W = [[0, 7, 4, 6, 1],
        [INF, 0, INF, INF, INF],
        [INF, 2, 0, 5, INF],
        [INF, 3, INF, 0, INF],
        [INF, INF, INF, 1, 0]]
    
    F, save_length = dijkstra(W, 0)

    print(F)
    print(save_length)


# def printMatrix(d):
#     m = len(d)
#     n=len(d[0])
    
#     for i in range(0,m):
#         for j in range(0,n):
#             print("%4d" % d[i][j],end=" ")
#         print()

# if __name__ == '__main__':
#     inf = 1000
#     W = [[0, 1, 3, inf, inf],
#         [1, 0, 3, 6, inf],
#         [3, 3, 0, 4, 2],
#         [inf, 6, 4, 0, 5],
#         [inf, inf, 2, 5, 0]]

#     printMatrix(W)

#     F = set()
#     n = len(W)
#     nearest = n * [0]
#     distance = n * [0]

#     for i in range(1, n):
#         nearest[i] = 0
#         distance[i] = W[0][i]

#     for _ in range(n - 1):
#         min_dist = inf
#         for i in range(1, n):
#             # distnace[i] < 0: the vertice has already been visited
#             if distance[i] >= 0 and distance[i] < min_dist:
#                 min_dist = distance[i]
#                 vnear = i
#         edge = (vnear, nearest[vnear])
#         F.add(edge)
#         distance[vnear] = -1
#         for i in range(1, n):
#             if W[i][vnear] < distance[i]:
#                 distance[i] = W[i][vnear]
#                 nearest[i] = vnear
    
#     print(F)