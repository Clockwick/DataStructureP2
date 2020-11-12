# a = 97 z = 122

inp = input("Enter Input : ").split()
summy = []
def selection_sort(arr, asa):
    n = len(arr)
    for i in range(n-1):
        MIN, MIN_INDEX = arr[i], i
        for j in range(i+1,n):
            if arr[j] < arr[MIN_INDEX]:
                MIN = arr[j]
                MIN_INDEX = j
            arr[i], arr[MIN_INDEX]=arr[MIN_INDEX], arr[i]
            asa[i], asa[MIN_INDEX]=asa[MIN_INDEX], asa[i]
    
for stone in inp:
    sumi = 0
    for sand in stone:
        if (ord(sand) >= 97 and ord(sand) <= 122) or (ord(sand) >= 0 and ord(sand) <= 9):
            sumi += ord(sand)
    summy.append(sumi)
selection_sort(summy, inp)
print(" ".join(inp))

        
