c = 1


def bubble_sort(lst, k):
    if k == 1:
        return
    global c
    b = True
    for n in range(k-1):
        if lst[n] > lst[n+1]:
            lst[n], lst[n+1] = lst[n+1], lst[n]
        if n == k-2:
            if not is_sort(lst):
                print(f"{c} step : {lst} move[{lst[k-1]}]")
            else:
                print(f"last step : {lst} move[{lst[k-1]}]")
        if is_sort(lst):
            print(f"last step : {lst} move[{lst[k-1]}]")
            return

    c += 1
    bubble_sort(lst, k-1)


def is_sort(lst):
    b = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            b = False
    return b


inp = list(map(int, input("Enter Input : ").split()))
bubble_sort(inp, len(inp))
