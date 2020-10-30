n, arr = input("Enter Input : ").split("/")
n = int(n)
arr = list(map(int, arr.split()))


def abc(s: int, l: list, e: list):
    if len(l) == 1:
        s += l[0]
        return s
    if len(l) == 0:
        return abc(s, e, [])
    else:
        m = min(l[0], l[1])
        e.append(m)
        l[0] -= m
        l[1] -= m
        s += l[0] + l[1]
        l.pop(0)
        l.pop(0)
        return abc(s, l, e)


if (len(arr) * 2) - 1 != n:
    print("Incorrect Input")
else:
    print(abc(0, arr, []))
