def selection_sort(arr):
     n = len(arr)
     for i in range(n):
          minimum, minimum_index = arr[i], i
          for j in range(i+1, n):
               if arr[j] < minimum:
                    minimum, minimum_index = arr[j], j
          arr[i], arr[minimum_index] = arr[minimum_index], arr[i] 
     
a = [5, 9, 6, 16, 8, 17, 18, 19, 14, 14, 12, 5, 15, 3, 0,
     15, 16, 2, 18, 20, 19, 7, 1, 16, 5, 9, 4, 11, 13, 5]
print("Unsorted array : ", a)
selection_sort(a)
print("Sorted array : ", a)

