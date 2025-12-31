import random
# print game board
board=["-","-","-",
        "-","-","-",
        "-","-","-"]
currentplayer="x"
winner=None
gamerunning=True
def gameboard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("---------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("---------")
    print(board[6]+"|"+board[7]+"|"+board[8])

#take player input
def playerinput(board):
    inp=int(input("Enter a number 1-9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=currentplayer
    else:
        print("Player is a already stop!")

#check for win or tie
def checkhorizontle(board):
    global winner
    if board[0]==board[1]==board[2]and board[1] !="-":
       winner=board[0]
       return True
    elif board[3]==board[4]==board[5]and board[3] !="-":
       winner=board[3]
       return True
    if board[6]==board[7]==board[8]and board[6] !="-":
       winner=board[6]
       return True

def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0] !="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1] !="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2] !="-":
        winner=board[2]
        return True
def checkdiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0] !="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2] !="-":
        winner=board[2]
        return True
def checktie(board):
    global gamerunning
    if "-" not in board:
        gameboard(board)
        print("It is a tie!")
        gamerunning=False
def checkwin( ):
    global gamerunning
    if checkdiag(board) or checkhorizontle(board) or checkrow(board):
        print(f"The winner is {winner}")
        gamerunning=False
# switch the player
def switchplayer():
    global currentplayer
    if currentplayer=="x":
        currentplayer="O"
    else:
        currentplayer="x"
#computer
def computer(board):
    while currentplayer=="O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchplayer()
#check for win or tie again
while gamerunning:
    gameboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
