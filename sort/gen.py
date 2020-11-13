import random

length = int(input("Length of random list : "))
lst = []
anot = []
for _ in range(length):
    lst.append(random.randint(0, 20))
for item in lst:
    if item not in anot:
        anot.append(item)

print(anot)
