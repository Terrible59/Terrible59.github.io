def bubble_sort(array):
    a = array
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j - 1] > a[j]:
                tmp = a[j - 1]
                a[j - 1] = a[j]
                a[j] = tmp
                print(a)
    return a