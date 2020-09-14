def cal_blue_bomb(bomb_str):
    bomb = []
    for i in bomb_str:
        bomb.append(i)
    n = 0
    boom = []
    grenade = []
    while n < len(bomb):
        boom.append(bomb[n])
        if boom[0] == bomb[n]:
            if len(boom) == 3 and boom[0] == boom[1] and boom[0] == boom[2]:
                grenade.append(boom[0])
                for i in range(3):
                    bomb.remove(bomb[n-2])
                boom.clear()
                n = 0
            else:
                n += 1
        else:
            boom.pop(0)
            n += 1
    return (bomb, grenade)


def cal_red_bomb(bomb_str, b_bomb):
    n = 0
    bomb = []
    boom = []
    grenade = []
    remain_bomb_str = ""
    mistake = 0
    current_bomb = ''
    for i in bomb_str:
        bomb.append(i)
    while n < len(bomb):
        boom.append(bomb[n])
        if boom[0] == bomb[n]:
            if len(boom) == 3 and boom[0] == boom[1] and boom[0] == boom[2] and len(b_bomb) != 0 and current_bomb != boom[2]:
                bomb_attack = b_bomb.pop(0)
                bomb.insert(n, bomb_attack)
                current_bomb = boom[0]
                boom = []
                n = 0

            if len(boom) > 3:
                boom.clear()

            elif len(boom) == 3 and boom[0] == boom[1] and boom[0] == boom[2] and current_bomb == boom[0]:
                mistake += 1
                for _ in range(3):
                    bomb.remove(bomb[n-2])
                boom = []
                current_bomb = ''
                n = 0
            elif len(boom) == 3 and boom[0] == boom[1] and boom[0] == boom[2] and len(b_bomb) == 0:
                grenade.append(boom[0])
                for _ in range(3):
                    bomb.remove(bomb[n-2])
                boom = []
                current_bomb = ''
                n = 0
            else:
                n += 1
        elif len(boom) > 3:
            boom.clear()
        else:
            boom.pop(0)
            n += 1

    for i in bomb:
        remain_bomb_str += i

    return (remain_bomb_str, grenade, mistake)


if __name__ == "__main__":
    red_team, blue_team = input("Enter Input (Normal, Mirror) : ").split()
    b_bomb = cal_blue_bomb(blue_team)
    b_remain_bomb = ""
    for i in b_bomb[0]:
        b_remain_bomb += i
    b_bomb[1].reverse()
    b_bomb_clone = len(b_bomb[1])
    a_bomb = cal_red_bomb(red_team, b_bomb[1])
    print("NORMAL :")
    print(len(a_bomb[0]))
    if len(a_bomb[0]) == 0:
        print("Empty")
    else:
        print(a_bomb[0][::-1])
    print(f"{len(a_bomb[1])} Explosive(s) ! ! ! (NORMAL)")
    if a_bomb[2] > 0:
        print(f"Failed Interrupted {a_bomb[2]} Bomb(s)")
    print("------------MIRROR------------")
    print(": RORRIM")
    if len(b_bomb[0]) == 0:
        print(0)
        print("Empty"[::-1])
    else:
        print(len(b_bomb[0]))
        print(b_remain_bomb)
    print("(RORRIM) ! ! ! (s)evisolpxE {}".format(b_bomb_clone))
