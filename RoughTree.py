
def rough(n):
    if po[n] != -1:
        return po[n]
    po[n] = min(rough(2*n+1), rough(2*n+2))
    po[2*n+1] -= po[n]
    po[2*n+2] -= po[n]
    return po[n]


N, vall = input("Enter Input : ").split("/")
cal = (int(N)//2)+1
val = vall.split()
po = []
m = 0
for i in range(int(N)):
    if i >= int(cal)-1:
        po.append(int(val[m]))
        m += 1
    else:
        po.append(-1)
if len(val) != cal:
    print("Incorrect Input")
else:
    rough(0)
    print(sum(po))
