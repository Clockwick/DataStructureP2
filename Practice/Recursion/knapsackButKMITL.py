def printSack(sack, maxi):
    global good
    global name
    for i in range(maxi+1):
        print(good[sack[i]], end=' ')
    # print(name[sack[i]],good[sack[i]], end = ' ')
    print()


def pick(sack, i, mLeft, ig):
    global N
    global good
    if ig < N:  # have something left to pick
        price = good[ig]  # good-price
        if mLeft < price:  # cannot afford that ig
            pick(sack, i, mLeft, ig+1)  # try to pick next good
        else:  # can buy
            mLeft -= price  # pay
            sack[i] = ig  # pick that ig to the sack at i
            if mLeft == 0:  # done
                printSack(sack, i)
            else:  # still have moneyLeft
                pick(sack, i+1, mLeft, ig+1)
            # take the item off the sack for other solutions
            pick(sack, i, mLeft+price, ig+1)


good = [20, 10, 5, 5, 3, 2, 20, 10]
name = ['soap', 'potato chips', 'loly pop',
        'toffy', 'pencil', 'rubber', 'milk', 'cookie']
N = len(good)  # numbers of good
sack = N*[-1]  # empty sack
mLeft = 20  # money left
i = 0  # sack index
ig = 0  # good index
pick(sack, i, mLeft, ig)
