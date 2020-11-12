
def insertion_sort(a):
    n = len(a)
    for i in range(n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1


arr = [8, 12, 13, 16, 17, 19, 2, 12, 0, 11, 11, 9, 19, 19, 0, 14, 18, 20, 9, 3]
print("Unsorted array :", arr)
insertion_sort(arr)
print("Sorted array :", arr)

