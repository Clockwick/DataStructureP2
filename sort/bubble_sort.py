def bubble_sort(n):
    num = len(n)
    global k
    for i in range(num-1):
        for j in range(num-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
            k += 1
            print(k)


if __name__ == "__main__":
    a = [4, 10, 13, 12, 18, 1, 2, 18, 15, 17, 13, 4, 11, 17, 15]
    k = 0
    bubble_sort(a)
    print(a)
