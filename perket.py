def powerSet(str1, index, lst, dif):
    n = len(str1)

    # base case
    if (index == n):
        return

    for i in range(index + 1, n):
        lst.append(tuple(map(int, str1[i].split())))
        sour = 1
        bitter = 0
        for j in lst:
            sour *= j[0]
            bitter += j[1]
        re = abs(sour - bitter)

        if re > dif:
            ans.append(dif)
            powerSet(str1, i, lst, dif)
        else:
            ans.append(re)
            powerSet(str1, i, lst, re)
        lst.remove(lst[len(lst) - 1])


if __name__ == '__main__':
    ans = []
    inp = input("Enter Input : ").split(",")
    powerSet(inp, -1, [], 1000000)
    print(min(ans))
