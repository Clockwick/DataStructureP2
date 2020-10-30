import random

length = int(input("Length of random list : "))
lst = []
for _ in range(length):
    lst.append(random.randint(0, 20))
print(lst)
