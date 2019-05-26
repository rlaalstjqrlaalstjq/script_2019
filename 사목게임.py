from tkinter import *
import tkinter.messagebox
import random


class TicTacToe:
    def refresh(self):
        for row in range(6):
            for col in range(7):
                 self.buttonList[row * 7 + col].configure(image=self.imageList[2])
                 self.buttonList[row * 7 + col].configure(text=' ')

    def pressed(self, row, col):
        for i in range(5,-1,-1):
            if self.buttonList[i*7+col]['text'] == ' ':
                if self.turn:
                    self.buttonList[i * 7 + col].configure(image=self.imageList[0])
                    self.buttonList[i * 7 + col].configure(text='o')
                    self.check()
                else:
                    self.buttonList[i * 7 + col].configure(image=self.imageList[1])
                    self.buttonList[i * 7 + col].configure(text='x')
                    self.check()
                self.turn = not self.turn
                break

    def checkRow(self):
        for i in range(5):
            for j in range(4):
                if self.buttonList[28-(i*7)+j]['text'] == self.buttonList[28 - (i*7)+j+1]['text'] == self.buttonList[28-(i*7)+j+2]['text'] == self.buttonList[28-(i*7)+j+3]['text']:
                    if self.buttonList[28-(i*7)+j]['text'] == "o":
                        tkinter.messagebox.showinfo("O승리")
                    elif self.buttonList[28-(i*7)+j]['text'] == "x":
                        tkinter.messagebox.showinfo("X승리")
                    break

    def checkCol(self):
        for i in range(7):
            for j in range(2):
                if self.buttonList[35-(7*(j+1)+i)]['text'] == self.buttonList[35-(7*(j+2)+i)]['text'] == self.buttonList[35-(7*(j+3)+i)]['text']:
                    if self.buttonList[35-(7*(j+1)+i)]['text'] == 'o':
                        tkinter.messagebox.showinfo("O승리")
                    elif self.buttonList[35-(7*(j+1)+i)]['text'] == 'x':
                        tkinter.messagebox.showinfo("X승리")
    def full(self):
        count = 0
        for i in range(6):
            for j in range(7):
                if self.buttonList[i*7+j]['text'] != ' ':
                    count += 1

        if count == 42:
            tkinter.messagebox.showinfo("비김")

    def check(self):
        self.checkRow()
        self.checkCol()
        self.full()

    def __init__(self):
        window = Tk()
        self.imageList = []
        self.imageList.append(PhotoImage(file='o.gif'))
        self.imageList.append(PhotoImage(file='x.gif'))
        self.imageList.append(PhotoImage(file='empty.gif'))
        self.buttonList = []
        self.turn = True  # T => O, F => X
        frame1 = Frame(window)
        frame1.pack()
        for row in range(6):
            for col in range(7):
                self.buttonList.append(Button(frame1, image=self.imageList[2], text=' ', command=lambda Row=row, Col=col : self.pressed(Row, Col)))
                self.buttonList[row * 7 + col].grid(row=row, column=col)

        frame2 = Frame(window)
        frame2.pack()
        self.judge = Label(frame2, text="0  차례").pack()
        
        window.mainloop()


TicTacToe()