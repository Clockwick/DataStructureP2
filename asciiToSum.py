inp = input("Enter Input : ")
summ = 0
for item in inp:
    summ += ord(item)
print(summ % 5)