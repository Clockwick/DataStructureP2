def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    lower_arr = []
    higher_arr = []

    for item in arr:
        if item > pivot:
            higher_arr.append(item)
        else:
            lower_arr.append(item)

    return quick_sort(lower_arr) + [pivot] + quick_sort(higher_arr)

arr = [8, 12, 13, 16, 17, 19, 2, 12, 0, 11, 11, 9, 19, 19, 0, 14, 18, 20, 9, 3]
print("Unsorted array :", arr)
sort_arr = quick_sort(arr)
print("Sorted array :", sort_arr)