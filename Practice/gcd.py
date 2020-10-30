def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


GCD = gcd(45, 10)
print(f"gcd = {GCD}")

# gcd(45, 10)
# Take the greater number
# 45 = 10 * q + r
# 45 = 10 * 4 + 5
# 10 = 5 * q + r
# 10 = 5 * 2 + 0
