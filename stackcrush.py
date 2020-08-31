col = input("Enter Input : ").split(" ")
combo = 0
n = 0
boom = []
rev = ""
while n < len(col):
    boom.append(col[n])
    if boom[0] == col[n]:
        if len(boom) == 3 and boom[0] == boom[1] and boom[0] == boom[2]:
            for i in range(3):
                col.remove(col[n-2])
            combo += 1
            boom.clear()
            n = 0
        else:
            n += 1
    else:
        boom.pop(0)
        n += 1
print(len(col))
if len(col) != 0:
    for i in range(len(col)):
        rev += col[-i-1]
    print(rev)

else:
    print("Empty")

if combo > 1:
    print(f"Combo : {combo} ! ! !")
