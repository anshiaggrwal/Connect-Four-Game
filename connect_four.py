import random
#initial conditions
rows=6
col=7
user="🟢"
comp="🔴 "
board=[["   ","   ","   ","   ","   ","   ","   "],["   ","   ","   ","   ","   ","   ","   "],["   ","   ","   ","   ","   ","   ","   "],
       ["   ","   ","   ","   ","   ","   ","   "],["   ","   ","   ","   ","   ","   ","   "],["   ","   ","   ","   ","   ","   ","   "]]
game_running=True
t=False
#print the board on screen
def printboard(board):
    print("\n      A      B      C      D      E      F      G",end="")
    for i in range(rows):
        print("\n  +------+------+------+------+------+------+------+")
        print(i,"| ", end="")
        for j in range(col):
            print(board[i][j]," | ",end="")
    print("\n  +------+------+------+------+------+------+------+")
#to check win loose or tie
def wlt(board,dice):
    global game_running,t
    for c in range(col-3):      #horizontal check
        for r in range(rows):
            if board[r][c]==dice and board[r][c+1]==dice and board[r][c+2]==dice and board[r][c+3]==dice:
                game_running=False
                break
    for c in range(col):      #vertical check
        for r in range(rows-3):
            if board[r][c]==dice and board[r+1][c]==dice and board[r+2][c]==dice and board[r+3][c]==dice:
                game_running=False
                break
    for c in range(col-3):    #positive diagonal check
        for r in range(rows-3):
            if board[r][c]==board[r+1][c+1]==board[r+2][c+2]==board[r+3][c+3]==dice:
                game_running=False
                break
    for c in range(col-3):           #negative diagonal check
        for r in range(3,rows):
            if board[r][c]==board[r-1][c+1]==board[r-2][c+2]==board[r-3][c+3] ==dice:
                game_running=False
                break
    if game_running==False:
        print(f"{dice} is winner")
def tie(board):
    global game_running,t
    for r in range(rows):       #checking for tie
        for c in range(col):
            if board[r][c]=="   ":
                game_running=True
                t=False
                return
            else:
                t=True
                game_running=False
    if game_running==False and t==True:
        print("its a tie")
def checkforspace(board,i,j):
    if board[i][j]=="   ":
        if i==rows-1 :
            return True
        elif board[i+1][j]!="   ":
            return True
        else:
            return False
    else:
        return False
#take input from user
def userinput(board):
    global game_running
    us=input("enter the box where you want to put the dice in the order column_alpharow_num ").upper()
    for i in range(rows):
        if "A" in us and str(i) in us :
            if checkforspace(board, i, 0) == True:
                board[i][0] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif "B" in us and str(i) in us :
            if checkforspace(board, i, 1) == True:
                board[i][1] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif "C" in us and str(i) in us :
            if checkforspace(board, i, 2) == True:
                board[i][2] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif "D" in us and str(i) in us :
            if checkforspace(board, i, 3) == True:
                board[i][3] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif "E" in us and str(i) in us :
            if checkforspace(board, i, 4) == True:
                board[i][4] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif "F" in us and str(i) in us:
            if checkforspace(board, i, 5) == True:
                board[i][5] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif "G" in us and str(i) in us:
            if checkforspace(board, i, 6) == True:
                board[i][6] = user
                printboard(board)
                tie(board)
                wlt(board,user)
                if game_running == True:
                    print("its computer's turn")
                    compinput(board)
            else:
                print("invalid input enter again")
                userinput(board)
        elif (us[0] not in "ABCDEFG"):
            print("invalid input enter again")
            userinput(board)
def compinput(board):
    i= random.randint(0, rows-1)
    j = random.randint(0, col-1)
    if checkforspace(board, i, j) == True:
        board[i][j] = comp 
        printboard(board)
        tie(board)
        wlt(board,comp)
        if game_running==True:
            print("its your turn")
            userinput(board)
    else:
        compinput(board)
printboard(board)
userinput(board)