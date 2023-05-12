import math,random
board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]

def drawShape(line,col,player):
    board[line][col]=player

#Draw the game board
def drawBoard():
    print("    1     2     3")
    for i in range(len(board)):
        print(i+1, end='')
        for l in range(len(board)):
            print(" | ",board[i][l], end='')
        print(" |\n")

#Set a random player to start first
def randomPlayer():
    return random.randint(0,1)
    
#Swap player turns
def playerTurn(player):
    return "X" if player == "O" else "O"

#Draw shape on the board
def drawShape(input, player):
    occupied = False
    row, col = list(
        map(int, input.split()))
    if board[row-1][col-1] == "-":
        if player == "X":
            board[row-1][col-1] = "X"
        else:
            board[row-1][col-1] = "O"
    else:
        #if position is already occupied
        occupied = True
        print("---------\nThat position is already occupied!\n---------")
    return occupied
def checkWin(player):
    win = False
    if board[0][0] == board[0][1] == board[0][2] == player: #horizontal 1
        win = True
    elif board[1][0] == board[1][1] == board[1][2] == player: #horizontal 2
        win = True
    elif board[2][0] == board[2][1] == board[2][2] == player: #horizontal 3
        win = True
    elif board[0][0] == board[1][0] == board[2][0] == player: #vertical 1
        win = True
    elif board[0][1] == board[1][1] == board[2][1] == player: #vertical 2
        win = True
    elif board[0][2] == board[1][2] == board[2][2] == player: #vertical 3
        win = True
    elif board[0][0] == board[1][1] == board[2][2] == player: #diagonal 1
        win = True
    elif board[0][2] == board[1][1] == board[2][0] == player: #diagonal 2
        win = True
    return win

def checkFilledBoard():
    filled = True
    for i in range(len(board)):
        for l in range(len(board)):
            if board[i][l] == "-": filled = False
    return filled

#Main program
run_game = True
player = "X" if randomPlayer() == 0 else "O"
print("Welcome to Tic Tac Toe!")
print("Made by David Santos utilizing Python\n")
while run_game == True:
    #catching input errors
    while 1:
        try:
            print("----------------------------------------------------------------------")
            drawBoard()
            print("Player",player,"'s turn. Choose a line and a column (ex: 1 1):",end='')
            str_input = input() #get user input
            occupied = drawShape(str_input, player) #call function for handling input and drawing the player shape
            break
        except ValueError: #if the input is a non integer value
            print("------------------\nSelect your row and column in the correct format! (row | column)\n------------------")
            continue
        except IndexError: #if the selected row/column values are out of bounds for the board
            print("------------------\nPlease select a valid game position!\n------------------")
    if checkWin(player) == True: #if a win is detected
        drawBoard()
        print("Congratulations! Player",player," has won!")
        run_game = False
        break
    if checkFilledBoard() == True: #if the board has been filled
        drawBoard()
        print("The board has been filled. It's a draw!")
        run_game = False
        break
    if occupied == False: player = playerTurn(player) #if position is not occupied swap turns