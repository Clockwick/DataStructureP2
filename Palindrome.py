def palindrome(s):
    if len(s) == 0:
        return True
    if s[0] == s[-1]:
        s = s[1:-1]
    else:
        return False
    return palindrome(s)


n = input("Enter Input : ")
if (palindrome(n)):
    print("'{}' is palindrome".format(n))
else:
    print("'{}' is not palindrome".format(n))
