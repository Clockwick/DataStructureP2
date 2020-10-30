def perket(str1, index, curr, value):
    n = len(str1)
    if index == n:
        return
#    print(curr)
    for i in range(index+1, n):
        curr.append(list(map(int, str1[i].split())))
        sour = 1
        bitter = 0
        for j in curr:
            sour *= j[0]
            bitter += j[1]
#        print("Sour :", sour)
#        print("Bitter :", bitter)
#        print("Different :", abs(sour - bitter))
        if abs(sour - bitter) > value:
            ans.append(value)
            perket(str1, i, curr, value)
        else:
            ans.append(abs(sour-bitter))
            perket(str1, i, curr, abs(sour-bitter))
        curr.pop()
    return


inp = input("Enter Input : ").split(",")  # ["1 2", "3 4", "5 6"]
ans = []
perket(inp, -1, [], 100000)
print(min(ans))
