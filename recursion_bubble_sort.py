c = 1


def bubble_sort(lst, k, s="", i=0, haha=False):
    sk = False
    global c
    global inp
    msg = None

    if i == 0 and is_sort(lst):
        print(f"last step : {lst} move[{msg}]")
    elif i == 0:
        for n in range(k-1):
            if lst[n] > lst[n+1]:
                msg = lst[n]
                lst[n], lst[n+1] = lst[n+1], lst[n]
        bubble_sort(lst, k-1, msg, i+1)
    else:
        if haha or i == len(lst) - 1:
            print(f"last step : {lst} move[{s}]")
            return
        else:
            print(f"{c} step : {lst} move[{s}]")
        for n in range(k-1):
            if lst[n] > lst[n+1]:
                sk = True
                msg = lst[n]
                lst[n], lst[n+1] = lst[n+1], lst[n]
        c += 1
        if not sk:
            bubble_sort(lst, k-1, msg, i+1, True)
        else:
            bubble_sort(lst, k-1, msg, i+1)


def is_sort(lst):
    b = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            b = False
    return b


inp = list(map(int, input("Enter Input : ").split()))
bubble_sort(inp, len(inp))
