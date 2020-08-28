def fun_string(text, choice):
    if choice == 1:
        return len(text)
    elif choice == 2:
        buffer = ""
        for i in range(len(text)):
            if text[i].isupper():
                buffer += chr(ord(text[i]) + 32)
            else:
                buffer += chr(ord(text[i]) - 32)
        return buffer
    elif choice == 3:
        buffer = ""
        for i in range(len(text)-1, -1, -1):
            buffer += text[i]
        return buffer
    elif choice == 4:
        buffer = ""
        for i in range(len(text)):
            if text[i] not in buffer:
                buffer += text[i]
        return buffer


if __name__ == "__main__":
    word, number = input().split()
    number = int(number)
    print(fun_string(word, number))
