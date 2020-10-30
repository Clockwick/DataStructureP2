
dub = []


def search_dup(inp, lst, siz):
    global dub
    if siz == len(inp):
        return
    if inp[siz] in lst and inp[siz] not in dub:
        dub.append(inp[siz])
    lst.append(inp[siz])
    return search_dup(inp, lst, siz+1)


inp = list(map(int, input("Input : ")[1:-1].split(",")))
search_dup(inp, [], 0)
if len(dub):
    print(", ".join(map(str, dub)))
else:
    print(-1)
