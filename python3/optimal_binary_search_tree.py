class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data
    

def tree(key, R, i, j):
    k = R[i][j]
    if k == 0:
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, R, i, k-1)
        p.r_child = tree(key, R, k + 1, j)
        return p


def optimal_binary_search_tree(n, p, A, R):
    for i in range(1, n + 1):
        A[i][i - 1] = 0
        A[i][i] = p[i]
        R[i][i - 1] = 0
        R[i][i] = i
    
    A[n + 1][n] = 0
    R[n + 1][n] = 0

    for diagnol in range(1, n):
        for i in range(1, n - diagnol + 1):
            j = i + diagnol

            temp = [(A[i][k - 1] + A[k + 1][j], k) for k in range(i, j + 1)]
            avg_op, k = min(temp)

            A[i][j] = avg_op + sum(p[i:j+1])
            R[i][j] = k


def print_matrix(M):
    for row in M:
        for elem in row:
            print(f'{elem:5}', end='')
        print()
    print()


def print_matrixF(M):
    for row in M:
        for elem in row:
            print(f'{elem:6.2F}', end='')
        print()
    print()


def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)


def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)


if __name__ == '__main__':
    key = [' ', 'A', 'B', 'C', 'D', 'E']
    p = [0, 5/15., 4/15., 3/15., 2/15., 1/15.]
    n = len(p) - 1

    A = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]
    R = [[0 for j in range(0, n + 2)] for i in range(0, n + 2)]

    optimal_binary_search_tree(n, p, A, R)
    
    print_matrixF(A)
    print()
    print_matrix(R)

    root = tree(key, R, 1, n)
    print_inOrder(root)
    print()
    print_preOrder(root)