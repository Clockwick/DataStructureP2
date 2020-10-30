# start from index 0 compare the next number
# if less than current number, do the swap
# else move current to the next [3,9,4,7,1,10]
# do the same thing [3,4,9,7,1,10]
# [3,4,7,9,1,10]
# [3,4,9,7,1,10] Found 1 swap with the previous number if the current is less than the previous or the current position is not index 0
# [3,4,9,1,7,10]
# [3,4,1,9,7,10]
# [3,1,4,9,7,10]
# [1,3,4,9,7,10]
# [1,3,4,9,7,10]
# do the same thing
# [1,3,4,7,9,10]
# complete


"""
Break down to the pseudocode
index = 0
in_sort(arr, 1)
function in_sort(arr, index):
    current = a[index]
    prev = a[index-1] 
    while current < prev:
        current = a[index]
        prev = a[index-1] 
        swap(current, prev)
        index -= 1
    return in_sort(arr, index+1)
        
print(arr) -> [1,3,4,7,9,10]
"""

"""
current = arr[index]
# Base case is if index == len(arr)
if current > next swap else next
return bubble_sort(arr, index+1)
"""

"""
Selection sort
start at index = 0
select the element at index = 0, compare to the next element until it's out of range (len(arr))
get that smallest element, swap to the element at index
repeat the process until index == len(arr) - 1
"""


def bubble_sort(arr, index=0):
    if index == len(arr)-1:
        return
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubble_sort(arr, index+1)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [8, 12, 13, 16, 17, 19, 2, 12, 0, 11, 11, 9, 19, 19, 0, 14, 18, 20, 9, 3]
print("Unsorted array :", arr)
insertion_sort(arr)
print("Sorted array :", arr)
