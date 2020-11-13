def merge(a,b):
    c = []
    a_index, b_index = 0, 0
    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            c.append(a[a_index])
            a_index +=1 
        else:
            c.append(b[b_index])
            b_index += 1
    if a_index == len(a):
        c.extend(b[b_index:])
    else:
        c.extend(a[a_index:])
    return c
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])

    return merge(left, right)
    
arr = [8, 12, 13, 16, 17, 19, 2, 12, 0, 11, 11, 9, 19, 19, 0, 14, 18, 20, 9, 3]
print("Unsorted array :", arr)
sort_arr = merge_sort(arr)
print("Sorted array :", sort_arr)