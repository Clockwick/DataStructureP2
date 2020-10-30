def bsum(lst):
    length = len(lst)
    half = length // 2
    if length == 1:
        return lst[0]
    a = lst[:half]
    b = lst[half:]
    return bsum(a) + bsum(b)


k = [1, 2, 3, 4, 5]
print(bsum(k))
