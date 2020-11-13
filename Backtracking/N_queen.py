def createBoard(n):
    return [0] * n * n



n =int(input("Enter Input : "))
board = createBoard(n)
for i in range(len(board)):
    if i % n == 0 and i != 0:
        print(board[i])
    else:
        print(board[i],end=" , ")

    
