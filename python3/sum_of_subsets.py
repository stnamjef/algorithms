def sum_of_subsets(i, cumulative_weight, remain, include):
        if cumulative_weight == W:
            print('sol [', end=' ')
            for elem in include:
                print(elem, end=' ')
            print(']')
        elif cumulative_weight + remain >= W and cumulative_weight + w[i + 1] <= W:
            include[i + 1] = 1
            sum_of_subsets(i + 1, cumulative_weight + w[i + 1], remain - w[i + 1], include)
            include[i + 1] = 0
            sum_of_subsets(i + 1, cumulative_weight, remain - w[i + 1], include)


if __name__ == '__main__':
    n = 4
    w = [1, 4, 2, 6]
    W = 6
    print('items=', w, 'W=', W)

    include = n * [0]
    remain = 0
    for k in w:
        remain += k

    sum_of_subsets(-1, 0, remain, include)