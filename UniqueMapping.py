n = input("Enter String : ")
s_list = []
r_list = []
answer = []


def mapping(alphabet):
    for char in alphabet:
        if not char in s_list:
            s_list.append(char)
        r_list.append(char)
    for i in r_list:
        for j in s_list:
            if i == j:
                answer.append(s_list.index(i))
    return answer


print(mapping(n))
