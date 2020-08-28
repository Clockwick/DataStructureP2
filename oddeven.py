print("*** Odd Even ***")
types, inp, sol = input("Enter Input : ").split(",")
new_inp = []
is_space = False

if types.lower() == "l":
    for i in inp:
        if i == " ":
            is_space = True
    if is_space:
        for i in inp:
            if i == " ":
                pass
            else:
                new_inp.append(i)
    else:
        new_inp.append(inp)
elif types.lower() == "s":
    new_inp = inp


def odd_even(arr, s):
    if type(arr).__name__ == "str":
        st = ""
        if s.lower() == "even":
            for i, char in enumerate(arr):
                if (i+1) % 2 == 0:
                    st += char
        elif s.lower() == "odd":
            for i, char in enumerate(arr):
                if (i+1) % 2 > 0:
                    st += char
        return st
    else:
        l = []
        if s.lower() == "even":
            for i, char in enumerate(arr):
                if (i+1) % 2 == 0:
                    l.append(char)
        elif s.lower() == "odd":
            for i, char in enumerate(arr):
                if (i+1) % 2 > 0:
                    l.append(char)
        return l


print(odd_even(new_inp, sol))
