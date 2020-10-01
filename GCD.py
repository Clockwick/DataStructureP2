

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


x, y = input("Enter Input : ").split()
x = int(x)
y = int(y)

if x == 0 or y == 0:
    if x > y:
        gg = gcd(x, y)
        print(f"The gcd of {x} and {y} is : {abs(gg)}")
    elif x == 0 and y == 0:
        print("Error! must be not all zero.")
    else:
        gg = gcd(y, x)
        print(f"The gcd of {y} and {x} is : {abs(gg)}")
else:
    if abs(x) > abs(y):
        gg = gcd(x, y)
        print(f"The gcd of {x} and {y} is : {abs(gg)}")
    elif x == 0 and y == 0:
        print("Error! must be not all zero.")
    else:
        gg = gcd(y, x)
        print(f"The gcd of {y} and {x} is : {abs(gg)}")
