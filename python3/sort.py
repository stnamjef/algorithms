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

def quick_sort(data, start, end):
    if start >= end:
        return
    else:
        key = start
        i = start + 1
        j = end
        while i <= j:
            while data[i] <= data[key] and i <= end:
                i += 1
            while data[j] >= data[key] and j > start:
                j -= 1
            if i > j:
                tmp = data[j]
                data[j] = data[key]
                data[key] = tmp
            else:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
        quick_sort(data, start, j - 1)
        quick_sort(data, j + 1, end)

def quick_sort2(data, start, end):
    if start >= end:
        return
    else:
        key = start
        j = start
        for i in range(start + 1, end + 1):
            if data[i] < data[key]:
                j += 1
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
        tmp = data[j]
        data[j] = data[key]
        data[key] = tmp
        quick_sort2(data, start, j - 1)
        quick_sort2(data, j + 1, end)

if __name__ == '__main__':
    a = [3, 5, 2, 9, 10, 14, 4, 8]
    merge_sort(a, 0, len(a) - 1)
    print(a)