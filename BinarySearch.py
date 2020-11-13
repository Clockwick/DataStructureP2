def quick_sort(arr):
    length = len(arr)
    if length <= 1:
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
def bi_search(l, r, arr, x):
    if r >= l:
        m = (l + r) // 2
        if arr[m] == x:
            return True
        elif arr[m] > x:
            return bi_search(l,m-1,arr,x)
        else:
            return bi_search(m+1,r,arr,x)
    return False
inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
arr = quick_sort(arr)
arr.sort()
print(arr)

