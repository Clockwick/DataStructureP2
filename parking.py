"""
1.look up to m
Arrive:
    if len(cis) < m:
        if a in cis
            print format already
        else
            append(a) to cis
            print format arrive
    else:
        print format full
Depart:
    if cis > 0:
        if a in cis
            print format remove
            remove(a) in cis
        else
            print format dont have

    else:
        print empty
2.print cis
"""
print("******** Parking Lot ********")
m, c, s, a = input("Enter max of car,car in soi,operation : ").split()
cis = list(map(int, c.split(",")))
if 0 in cis:
    cis.clear()
if s == "arrive":
    if len(cis) < int(m):
        if int(a) in cis:
            print(f"car {a} already in soi")
        else:
            print(f"car {a} arrive! : Add Car {a}")
            cis.append(int(a))
    else:
        print(f"car {a} cannot arrive : Soi Full")

else:
    if len(cis) > 0:
        if int(a) in cis:
            print(f"car {a} depart ! : Car {a} was remove")
            cis.remove(int(a))
        else:
            print(f"car {a} cannot depart : Dont Have Car {a}")

    else:
        print(f"car {a} cannot depart : Soi Empty")
print(cis)
