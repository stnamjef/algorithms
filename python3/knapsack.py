import queue
import heapq


n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
max_profit = 0
include = [0, 0, 0, 0]
bestset = [0, 0, 0, 0]


# depth-first search
def knapsack(i, profit, weight):
    global max_profit
    global bestset
    if weight <= W and profit > max_profit:
        max_profit = profit
        bestset = include[:]
    if promising(i, profit, weight):
        include[i + 1] = 1
        knapsack(i + 1, profit + p[i + 1], weight + w[i + 1])
        include[i + 1] = 0
        knapsack(i + 1, profit, weight)


def promising(i, profit, weight):
    if weight >= W:
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while j < n and totweight + w[j] <= W:
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        # if item left
        if k < n:
            bound = bound + (W - totweight) * p[k] / w[k]
        return bound > max_profit


class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include


def knapsack_bfs():
    global max_profit
    global bestset

    q = queue.Queue()
    v = Node(-1, 0, 0, include[:])

    q.put(v)

    n_node = 1
    while not q.empty():
        n_node += 2
        v = q.get()
        left = Node(
            level=v.level + 1,
            weight=v.weight + w[v.level + 1],
            profit=v.profit + p[v.level + 1],
            include=v.include[:]
        )
        left.include[left.level] = 1

        if left.weight <= W and left.profit > max_profit:
            max_profit = left.profit
            bestset = left.include[:]

        if bound(left) > max_profit:
            q.put(left)
        
        right = Node(
            level=v.level + 1,
            weight=v.weight,
            profit=v.profit,
            include=v.include[:]
        )
        right.include[right.level] = 0

        if bound(right) > max_profit:
            q.put(right)
    print(f'# of node travered: {n_node}')


class Node2:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include


def knapsack_best_fs():
    global max_profit
    global bestset

    max_profit = 0

    v = Node2(-1, 0, 0, 0, include[:])
    v.bound = bound(v)

    q = queue.PriorityQueue()
    q.put((-v.bound, v))

    n_node = 1
    while not q.empty():
        _, v = q.get()
        if v.bound > max_profit:
            n_node += 2
            left = Node2(
                level=v.level + 1,
                weight=v.weight + w[v.level + 1],
                profit=v.profit + p[v.level + 1],
                bound=0,
                include=v.include[:]
            )
            left.bound = bound(left)
            left.include[left.level] = 1

            if left.weight <= W and left.profit > max_profit:
                max_profit = left.profit
                bestset = left.include[:]
            
            if left.bound > max_profit:
                q.put((-left.bound, left))
            
            right = Node2(
                level=v.level + 1,
                weight=v.weight,
                profit=v.profit,
                bound=0,
                include=v.include[:]
            )
            right.bound = bound(right)
            right.include[right.level] = 0

            if right.bound > max_profit:
                q.put((-right.bound, right))
    print(f'# of node traversed: {n_node}')


def bound(u):
    if u.weight >= W:
        return 0
    else:
        j = u.level + 1
        bound = u.profit
        totweight = u.weight
        while j < n and totweight + w[j] <= W:
            bound += p[j]
            totweight += w[j]
            j += 1
        k = j
        if k < n:
            bound = bound + (W - totweight) * p[k] / w[k]
        return bound


if __name__ == '__main__':
    print('Knapsack(Breadth first search):')
    knapsack_bfs()
    print(f'max profit: {max_profit}')
    print(f'best set: {bestset}')
    print('Knapsack(Best first search):')
    knapsack_best_fs()
    print(f'max profit: {max_profit}')
    print(f'best set: {bestset}')