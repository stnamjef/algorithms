def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        tmp = a[i]
        a[i] = a[min]
        a[min] = tmp


def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp


def insertion_sort(a):
    for i in range(len(a) - 1):
        j = i
        while a[j] > a[j + 1] and j >= 0:
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp
            j -= 1


def merge_sort(a, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        merge(a, low, mid, high)


def merge(a, low, mid, high):
    i, j, k = low, mid + 1, 0
    tmp = [0 for _ in range(low, high + 1)]
    while i <= mid and j <= high:
        if a[i] < a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    if i > mid:
        tmp[k:] = a[j:high + 1]
    else:
        tmp[k:] = a[i:mid + 1]
    a[low:high + 1] = tmp[:]


if __name__ == '__main__':
    a = [3, 5, 2, 9, 10, 14, 4, 8]
    merge_sort(a, 0, len(a) - 1)
    print(a)