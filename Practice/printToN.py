def printToN(n):
    if m == n:
        print(n, end=" ")
        return
    if m >= 1:
        print(n, end=" ")
        return printToN(n+1)
    else:
        print("1", end=" ")
        return


def nToPrint(n):
    if n == 0:
        return
    if m >= 1:
        print(n, end=" ")
        return nToPrint(n-1)
    else:
        print("1", end=" ")
        return


m = int(input())
printToN(1)
nToPrint(m)
