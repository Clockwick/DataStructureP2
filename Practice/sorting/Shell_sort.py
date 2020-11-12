def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for j in range(gap, n):
            temp = arr[j]
            i = j
            while i >= gap and arr[i-gap] > temp:
                arr[i], arr[i-gap] = arr[i-gap], arr[i]
                i -= gap
        gap //= 2
            
        
        


a = [5, 9, 6, 16, 8, 17, 18, 19, 14, 14, 12, 5, 15, 3, 0,
     15, 16, 2, 18, 20, 19, 7, 1, 16, 5, 9, 4, 11, 13, 5]
print("Unsorted array : ", a)
shell_sort(a)
print("Sorted array : ", a)
    