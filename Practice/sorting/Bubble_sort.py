def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

a = [5, 9, 6, 16, 8, 17, 18, 19, 14, 14, 12, 5, 15, 3, 0,
     15, 16, 2, 18, 20, 19, 7, 1, 16, 5, 9, 4, 11, 13, 5]
print("Unsorted array : ", a)
bubble_sort(a)
print("Sorted array : ", a)