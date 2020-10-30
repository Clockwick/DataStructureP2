
def toString(a):
    print("".join(a))


def permute(arr, n, l):
    if n == l:
        toString(arr)
        return
    else:
        for i in range(n, l+1):
            curr[n], curr[i] = curr[i], curr[n]
            permute(arr, n+1, l)
            curr[n], curr[i] = curr[i], curr[n]


inp = input("Enter the Input : ")
curr = list(inp)
l = len(inp)
permute(curr, 0, l-1)
