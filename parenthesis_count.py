# Python3 code to Check for
# balanced parentheses in an expression
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

sk = input("Enter Input : ")
# Function to check parentheses


def check(myStr):
    stack = []
    match = 0
    lack = 0
    for i in myStr:
        if i in open_list:
            stack.append(i)
            match += 1
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
                match -= 1
            else:
                lack += 1
    if len(stack) == 0 and match == 0 and lack == 0:
        print(match + lack)
        return "Perfect ! ! !"
    else:
        return match + lack


print(check(sk))
