def mi_5(number):
    if number <= 0:
        plus_5(number)
        return
    print(number, end=", ")
    return mi_5(number-5)


def plus_5(number):
    if number == n:
        print(number)
        return
    print(number, end=", ")
    return plus_5(number+5)


n = int(input("Input : "))
print("Output : ", end="")
mi_5(n)
