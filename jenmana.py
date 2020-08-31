if __name__ == "__main__":
    inp, s = input("Enter Input : ").split(','), []
    for i in inp:
        if i[0] == 'A':
            while s and s[-1] <= int(i.partition(" ")[2]):
                s = s[:-1]
            s.append(int(i.partition(" ")[2]))
        elif i[0] == 'B':
            print(len(s))
