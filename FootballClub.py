

def calcPoint(win, loss, draw):
    return 3*win + (0*loss) + 1 * draw

def sortByPoint(a):
    n = len(a)
    for i in range(n):
        j = i
        while j > 0 and a[j-1][1]["points"] < a[j][1]["points"]:
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1
def sortByGD(a):
    n = len(a)
    for i in range(n):
        j = i
        while j > 0 and int(a[j-1][2]["gd"]) < int(a[j][2]["gd"]):
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

               
def football(name, wins, loss, draws, scored, conceded):
    points = calcPoint(wins, loss, draws)
    gd = scored - conceded
    return [name, {'points' : points}, {'gd' : gd}]
    

inp = input("Enter Input : ").split("/")
teams = []
for i in range(len(inp)):
    inp[i] = inp[i].split(",")
print("== results ==")
for obj in inp:
    teams.append(football(obj[0], int(obj[1]), int(obj[2]), int(obj[3]), int(obj[4]), int(obj[5])))


sortByPoint(teams)
for i in range(len(teams)):
    for j in range(len(teams)):
        if i != j:
            if teams[i][1]["points"] == teams[j][1]["points"]:
                if teams[i][2]["gd"] > teams[j][2]["gd"]:
                    teams[i],teams[j] = teams[j],teams[i]
                

for ans in teams:
    print(ans)