# ------------------ checking for win

class vars:
    p1win = False
    p2win = False

def checkRowWin(gameboard):
    for i in range(3):
        if gameboard[i][0] == 'X' and gameboard[i][1] == 'X' and gameboard[i][2] == 'X':
            vars.p1win = True
        elif gameboard[i][0] == 'O' and gameboard[i][1] == 'O' and gameboard[i][2] == 'O':
            vars.p2win = True
            

def checkColumnWin(gameboard):
    for i in range(3):
        if gameboard[0][i] == 'X' and gameboard[1][i] == 'X' and gameboard[2][i] == 'X':
            vars.p1win = True
        elif gameboard[0][i] == 'O' and gameboard[1][i] == 'O' and gameboard[2][i] == 'O':
            vars.p2win = True

def checkDiagonalWin(gameboard):
    if gameboard[0][0] == 'X' and gameboard[1][1] == 'X' and gameboard[2][2] == 'X':
        vars.p1win = True
    elif gameboard[0][2] == 'X' and gameboard[1][1] == 'X' and gameboard[2][2] == 'X':
        vars.p1win = True
    elif gameboard[2][0] == 'O' and gameboard[1][1] == 'O' and gameboard[0][2] == 'O':
        vars.p2win = True
    elif gameboard[2][0] == 'O' and gameboard[1][1] == 'O' and gameboard[0][2] == 'O':
        vars.p2win = True
        
def checkWin(gameboard):
    checkRowWin(gameboard)
    checkColumnWin(gameboard)
    checkDiagonalWin(gameboard)
    if vars.p1win == True:
        print("Congratulations, Player 1 has won!")
    elif vars.p2win == True:
        print ("Congratulations, Player 2 has won!")

# ---------------------- game input and gameboard

gameboard = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

p1turn = True
remainingspaces = 9

print("Players: Enter two numerical values when it's your turn for the x and y coordinates of where you want to put your marker")
print("---------------------------------------------")

while True:
    if vars.p1win == True or vars.p2win == True:
        break
        
    if p1turn == True:
        if vars.p1win == False or vars.p2win == False or remainingspaces > 0:
            print("Player 1, it's your turn")
    else:
        if vars.p1win == False or vars.p2win == False or remainingspaces > 0:
            print("Player 2, it's your turn")
    pos = input("Where do you want to put your marker? ")

    a = pos.split(", ")

    xcoord = int(a[0]) - 1
    ycoord = int(a[1]) - 1
    if xcoord >= 3 or xcoord <= -1 or ycoord >= 3 or ycoord <= -1:
        print("The position that you input is not on the game board. Please put in a different position")
    elif gameboard[xcoord][ycoord] == 'X' or gameboard[xcoord][ycoord] == 'O':
        print("Your position has already been taken")
    elif remainingspaces == 0:
        print("Game over: All spaces have been taken up")
    else:
        remainingspaces -= 1
        if p1turn == True:
            gameboard[xcoord][ycoord] = 'X'
            print(gameboard[0])
            print(gameboard[1])
            print(gameboard[2])
            checkWin(gameboard)
            print("---------------------------------------------")
            p1turn = False
        elif p1turn == False:
            gameboard[xcoord][ycoord] = 'O'
            print(gameboard[0])
            print(gameboard[1])
            print(gameboard[2])
            checkWin(gameboard)
            print("---------------------------------------------")
            p1turn = True
            
            


