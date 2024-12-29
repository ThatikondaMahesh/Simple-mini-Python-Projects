# program to tic Tac Toe
import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.current_player="x"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("TicTacToe")
        self.buttonGrid=[]
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.window,text='',width=20,height=10,command=lambda i=i,j=j:self.move(i,j))
                button.grid(row=i,column=j)
                
                row.append(button)
            self.buttonGrid.append(row)
    def move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.current_player
            self.buttonGrid[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("gameover",f"player {self.current_player} wins")
                self.window.quit()
            elif(self.isboard_full()):
                messagebox.showinfo("gameover", 'draw match')
            else:
                self.current_player='o' if self.current_player=="x" else "x"
    def check_winner(self,player):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]==player :
                    return True
            if self.board[0][i]==self.board[1][i]==self.board[2][i]==player :
                    return True   
            if self.board[0][0]==self.board[1][1]==self.board[2][2]==player :
                        return True 
            if self.board[0][2]==self.board[1][1]==self.board[2][0]==player :
                    return True
                
        return False
    def isboard_full(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    def run(self):
        self.window.mainloop()
       
game=TicTacToe()
game.run()
