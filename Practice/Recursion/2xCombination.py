def r(x):
    if x >= n and not 0 in a:
        print(a)
        return
    if a[x] != 0:
        r(x+1)
        return
    for i in range(1, n+1):
        if c[i-1] and x+i+1 < n*2 and a[x] == 0 and a[x+i+1] == 0:
            a[x], a[x+i+1] = i, i
            c[i-1] = False
            r(x+1)
            a[x], a[x+i+1] = 0, 0
            c[i-1] = True


n = int(input())
a = [0]*n*2
c = [True] * n
r(0)
