def findUpper(s, i=0):
    if i == len(s):
        print("No upper found")
        return
    if s[i].isupper():
        print(s[i])
        return
    return findUpper(s, i+1)


s = input("Enter Input : ")

findUpper(s)
