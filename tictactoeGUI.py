"""
Simple tic tac toe game made with the tkinter GUI toolkit
Enables the players to choose their displayed names, keep track of the score count and reset the game.

Made by David Santos - https://github.com/odavidsons/tictactoe-GUI-python
"""

import tkinter as tk
from time import sleep

class App(tk.Frame):

    board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
    ]
    player1 = ""
    player2 = ""
    turn = player1
    shape = ""

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.config(width=75,padx=20,pady=20)
        self.pack()
        
    def renderBoard(self):
        gameBoard = tk.Frame(self,width=40,pady=15)
        gameBoard.pack()
        tile1 = tk.Button(gameBoard,width=5,height=5,text=self.board[0][0],command=lambda x=0, y=0: self.drawShape(x,y,tile1))
        tile1.grid(row=0,column=0)
        tile2 = tk.Button(gameBoard,width=5,height=5,text=self.board[0][1],command=lambda x=0, y=1: self.drawShape(x,y,tile2))
        tile2.grid(row=0,column=1)
        tile3 = tk.Button(gameBoard,width=5,height=5,text=self.board[0][2],command=lambda x=0, y=2: self.drawShape(x,y,tile3))
        tile3.grid(row=0,column=2)

        tile4 = tk.Button(gameBoard,width=5,height=5,text=self.board[1][0],command=lambda x=1, y=0: self.drawShape(x,y,tile4))
        tile4.grid(row=1,column=0)
        tile5 = tk.Button(gameBoard,width=5,height=5,text=self.board[1][1],command=lambda x=1, y=1: self.drawShape(x,y,tile5))
        tile5.grid(row=1,column=1)
        tile6 = tk.Button(gameBoard,width=5,height=5,text=self.board[1][2],command=lambda x=1, y=2: self.drawShape(x,y,tile6))
        tile6.grid(row=1,column=2)

        tile7 = tk.Button(gameBoard,width=5,height=5,text=self.board[2][0],command=lambda x=2, y=0: self.drawShape(x,y,tile7))
        tile7.grid(row=2,column=0)
        tile8 = tk.Button(gameBoard,width=5,height=5,text=self.board[2][1],command=lambda x=2, y=1: self.drawShape(x,y,tile8))
        tile8.grid(row=2,column=1)
        tile9 = tk.Button(gameBoard,width=5,height=5,text=self.board[2][2],command=lambda x=2, y=2: self.drawShape(x,y,tile9))
        tile9.grid(row=2,column=2)

    #Draw a player shape on the board. It receives the position and the button that was pressed to be able to update it's text
    #Also checks if there is a winner when a shape is drawn
    def drawShape(self,row,col,buttonUpdate):
        if self.player1 and self.player2 != "":
            current_player = self.turn
            if self.board[row][col] == "-":
                self.board[row][col]= self.playerTurn()
                buttonUpdate.config(text=self.board[row][col])

            #Check if there is a winner
            if self.checkWin(self.shape) == True:
                print("Player: "+current_player+" wins!")
                self.addScore(current_player)
                labelTurn.config(text="Player "+current_player+" wins!")
                self.clearBoard()
            else:
                #Check if the board is filled, and call a draw
                if self.checkFilledBoard() == True:
                    print("It's a draw!")
                    labelTurn.config(text="It's a draw!")
                    self.clearBoard()
        else:
            print("Please enter the player names!")
            labelTurn.config(text="Please enter the player names!")

    def addScore(self,winner):
        if winner == player1:
            scoreP1.config(text=scoreP1.cget("text")+1)
        else: scoreP2.config(text=scoreP2.cget("text")+1)

    #Reset the game board
    def clearBoard(self):
        sleep(1)
        for row in self.board:
            for i in range(len(row)):
                row[i] = "-"
        #Get all the widgets in the main window that are buttons, and set their text back to default
        widgets = self.nametowidget("!frame").winfo_children()
        for widget in widgets:
            if str(widget.winfo_name).find("button") != -1 and str(widget.winfo_name).find("button10") == -1:
                widget.config(text="-")

    #Reset the game
    def resetGame(self):
        self.clearBoard()
        scoreP1.config(text=0)
        scoreP2.config(text=0)
        self.turn = self.player1
        labelTurn.config(text="Turn: "+self.turn)

    #Swap player turns
    def playerTurn(self):

        if self.turn == player1:
            self.turn = player2
            labelTurn.config(text="Turn: "+player2)
            self.shape = "X"
            return "X"
        else:
            labelTurn.config(text="Turn: "+player1)
            self.turn = player1
            self.shape ="O"
            return "O"

    #Verify if there is a winner in the current turn
    def checkWin(self,shape):
        win = False
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == shape: #horizontal 1
            win = True
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == shape: #horizontal 2
            win = True
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == shape: #horizontal 3
            win = True
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == shape: #vertical 1
            win = True
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == shape: #vertical 2
            win = True
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == shape: #vertical 3
            win = True
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == shape: #diagonal 1
            win = True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == shape: #diagonal 2
            win = True
        return win

    #Check if the board has been filled
    def checkFilledBoard(self):
        filled = True
        for i in range(len(self.board)):
            for l in range(len(self.board)):
                if self.board[i][l] == "-": filled = False
        return filled

    def inputNamesWindow(self):
        global inputForm,input1,input2

        #Create the window for inputing the player names
        inputForm = tk.Toplevel()
        inputForm.title("Enter names")
        label1 = tk.Label(text="Player 1: ",master=inputForm)
        label1.grid(row=0,column=0)
        input1 = tk.Entry(master=inputForm)
        input1.grid(row=0,column=1)
        label2 = tk.Label(text="Player 2: ",master=inputForm)
        label2.grid(row=1,column=0)
        input2= tk.Entry(master=inputForm)
        input2.grid(row=1,column=1)
        button1 = tk.Button(inputForm,text="OK",command=lambda: self.inputPlayers(input1.get(),input2.get()))
        button1.grid(row=2,column=0,columnspan=2)
        inputForm.attributes('-topmost', True)
    
    #Set the player name variables with the inputs
    def inputPlayers(self,input1,input2):
        global player1,player2

        player1 = input1
        labelP1.config(text=player1+": X")
        player2 = input2
        labelP2.config(text=player2+": O")
        inputForm.destroy()
        self.playerTurn()

#Run application
game = App()
game.master.title('Tic Tac Toe')
labelTurn = tk.Label(game,text="Turn")
labelTurn.pack()

game.renderBoard()

gameInfo = tk.Frame(game)
gameInfo.pack(fill="x")
#Display player names
scoreFrame = tk.Frame(gameInfo,highlightbackground="gray",highlightthickness=1)
scoreFrame.pack(side="right")
label1 =tk.Label(scoreFrame,text="Score")
label1.pack(side="top")
scoreP1 = tk.Label(scoreFrame,text=0)
scoreP1.pack()
scoreP2 = tk.Label(scoreFrame,text=0)
scoreP2.pack()

#Display player scores
playersFrame = tk.Frame(gameInfo,highlightbackground="gray",highlightthickness=1)
playersFrame.pack(side="left")
label2 =tk.Label(playersFrame,text="Players")
label2.pack(side="top")
labelP1 =tk.Label(playersFrame,text="Player 1:")
labelP1.pack()
labelP2 =tk.Label(playersFrame,text="Player 2:")
labelP2.pack()

resetFrame = tk.Frame(game,pady=5)
resetFrame.pack(fill="x")
resetBtn = tk.Button(resetFrame,text="Reset game",command=game.resetGame)
resetBtn.pack()

game.inputNamesWindow()

game.mainloop()
