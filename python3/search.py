import queue

def print_matrix(mat):
    for row in mat:
        for elem in row:
            print(f'{elem:3}', end='')
        print()


def dfs(graph, start):
    visited = [0] * len(graph)
    dfs_inner(graph, start, visited)
    print()


def dfs_inner(graph, here, visited):
    print(here, end=' ')
    visited[here] = 1
    for there in range(len(graph[here])):
        if graph[here][there] != 0 and not visited[there]:
            dfs_inner(graph, there, visited)


def bfs(graph, start):
    q = queue.Queue()
    q.put(start)

    discovered = [0] * len(graph)
    discovered[start] = 1
    while not q.empty():
        here = q.get()
        print(here, end=' ')
        for there in range(len(graph[here])):
            if graph[here][there] != 0 and not discovered[there]:
                q.put(there)
                discovered[there] = 1
    print()


if __name__ == '__main__':
    e={0:[1,2,3], 1:[2,5], 2:[3,4,5,6], 3:[4,6],4:[6,7]}
    n=8
    a = [ [0 for j in range(0,n)] for i in range(0,n)]
    for i in range(0,n-1):
        for j in range(i+1,n):
            if i in e:
                if j in e[i]:
                    a[i][j]=1
                    a[j][i]=1

    print_matrix(a)
    bfs(a, 0)
    dfs(a, 0)