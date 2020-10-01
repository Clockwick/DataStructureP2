def check(n):
    if n > 0:
        print(stair_plus(n, n))
    elif n < 0:
        n = abs(n)
        print(stair_neg(n, n))
    elif n == 0:
        print("Not Draw!")


def stair_plus(n, m):
    if n == 0:
        return ''
    else:
        return '_'*(n-1) + '#'*(m-n+1) + '\n' + stair_plus(n-1, m)


def stair_neg(n, m):
    if n == 0:
        return ''
    else:
        return stair_neg(n-1, m) + '_'*(n-1) + '#'*(m-n+1) + '\n'


n = int(input("Enter Input : "))
check(n)
