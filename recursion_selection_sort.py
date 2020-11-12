def is_sort(lst):
    b = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            b = False
            break
    return b

def maxIndex(lst, start, end):
    if start == end:
        return start
    k = maxIndex(lst, start-1, end)
    return start if lst[start] > lst[k] else k
    

def selection_sort(lst, i):
    if i == 0:
        return
    k = maxIndex(lst, i, 0)
    if k != i:
        lst[k], lst[i] = lst[i], lst[k]
        print(f"swap {lst[k]} <-> {lst[i]} : {lst}")
        
    selection_sort(lst, i-1)


inp = list(map(int, input("Enter Input : ").split()))
selection_sort(inp,len(inp)-1)
print(inp)
