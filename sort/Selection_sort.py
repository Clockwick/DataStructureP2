def selection_sort(a):
    n = len(a)
    for i in range(n):
        MIN, MIN_INDEX = a[i], i
        for j in range(i+1, n):
            if MIN > a[j]:
                MIN = a[j]
                MIN_INDEX = j
        a[MIN_INDEX], a[i] = a[i], a[MIN_INDEX]


a = [5, 9, 6, 16, 8, 17, 18, 19, 14, 14, 12, 5, 15, 3, 0,
     15, 16, 2, 18, 20, 19, 7, 1, 16, 5, 9, 4, 11, 13, 5]
selection_sort(a)
print(a)
