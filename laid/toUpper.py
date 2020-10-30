def toUpper(n, i, s):
    if i == len(n) - 1:
        return s
    if n[i].islower():
        s += chr(ord(n[i]) - 32)
    else:
        s += n[i]
    return toUpper(n, i + 1, s)


s = "asdAsdasd"
print(toUpper(s, 0, ""))
