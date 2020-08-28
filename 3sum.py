import itertools

n = input("Enter Your List : ").split()
answer = []
real_answer = []


def _3Sum(inp):
    for i in inp:
        for j in inp:
            for k in inp:
                if i == j or i == k or j == k:
                    if int(i) == 0 and int(j) == 0 and int(k) == 0:
                        answer.append([int(i), int(j), int(k)])
                    else:
                        pass
                else:
                    if int(i)+int(j)+int(k) == 0:
                        answer.append([int(i), int(j), int(k)])
    for i in answer:
        i.sort()
    for i in answer:
        if i not in real_answer:
            real_answer.append(i)
    return real_answer


if len(n) < 3:
    print("Array Input Length Must More Than 2")
else:
    print(_3Sum(n))
