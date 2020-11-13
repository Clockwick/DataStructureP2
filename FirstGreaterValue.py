def greatValue(arr, num):
    for i in range(1,10001):
        num += 1
        if num in arr:
            return num
            break
    return "No First Greater Value"
        

inp = input("Enter Input : ").split("/")
inp[0] = list(map(int,inp[0].split()))
inp[1] = list(map(int,inp[1].split()))
for item in inp[1]:
    print(greatValue(inp[0], item))
                
            