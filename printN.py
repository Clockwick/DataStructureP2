
def print1ToN(n):
    # code here
    if n > 1:
        print1ToN(n-1)
        print(str(n) + ' ', end='')
    elif n <= 1:
        print("1 ", end='')


def printNto1(n):
    # code here
    if n > 1:
        print(str(n) + ' ', end='')
        printNto1(n-1)
    elif n <= 1:
        print("1 ", end='')


n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)
