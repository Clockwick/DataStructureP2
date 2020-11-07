def comp(a, b):
    val_1 = calc(a)
    val_2 = calc(b)
    if val_1 > val_2:
        print(f"{a}>{b}")
    elif val_1 < val_2:
        print(f"{a}<{b}")
    elif val_1 == val_2:
        print(f"{a}={b}")


def calc(s):
    pp = power[s]
    if (2*s) + 1 < len(power):
        pp += power[(2*s)+1]
    if (2*s) + 2 < len(power):
        pp += power[(2*s)+2]
    return pp


power, com = input("Enter Input : ").split("/")
power = list(map(int, power.split()))
com = com.split(",")
print(sum(power))
for i in com:
    a = int(i.split()[0])
    b = int(i.split()[1])
    comp(a, b)
