vnum, q = input("Enter Input : ").split("/")
vnum_l, q = [i for i in range(1, vnum+1)], list(map(int, q.split()))
queue = vnum_l.copy()
lefted = []
for i in range(len(q)):
    print(f"Customer {i+1} Booking Van {queue[i]} | {q[i]} day(s)")

