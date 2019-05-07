from tkinter import *
import tkinter.messagebox
import random

STATE_O_TURN = 0
STATE_X_TURN = 1
STATE_O_GAME_OVER = 2
STATE_X_GAME_OVER =3
STATE_GAME_OVER = 4

window = Tk()
frame2 = Frame(window)
frame2.pack()


class TicTacToe:
    def refresh(self):
        for row in range(3):
            for col in range(3):
                # self.labelList[row * 3 + col].configure(image=self.imageList[random.randint(0, 1)])
                self.buttonList[row * 3 + col]['image'] = self.imageList[random.randint(0, 1)]

    def pressed(self, row, col):
        if self.turn == STATE_O_TURN and self.buttonList[row*3+col]['text'] == "empty":
            self.buttonList[row * 3 + col]['image'] = self.imageList[0]
            self.buttonList[row * 3 + col]['text'] = "o"
            self.turn = STATE_X_TURN

        elif self.turn == STATE_X_TURN and self.buttonList[row*3+col]['text'] == "empty":
            self.buttonList[row * 3 + col]['image'] = self.imageList[1]
            self.buttonList[row * 3 + col]['text'] = "x"
            self.turn = STATE_O_TURN

        if self.has_won() == 0:
            tkinter.messagebox.showinfo("O승리")
        elif self.has_won() == 1:
            tkinter.messagebox.showinfo("X승리")
        if self.has_drow() == True:
            tkinter.messagebox.showinfo("비겼습니다")

    def has_won(self):
            if self.buttonList[0]['text'] == self.buttonList[3]['text'] == self.buttonList[6]['text'] == "o" or \
                    self.buttonList[1]['text'] == self.buttonList[4]['text'] == self.buttonList[7]['text'] == "o" or \
                    self.buttonList[2]['text'] == self.buttonList[5]['text'] == self.buttonList[8]['text'] == "o":
                return 0
            elif self.buttonList[0]['text'] == self.buttonList[3]['text'] == self.buttonList[6]['text'] == "x" or \
                    self.buttonList[1]['text'] == self.buttonList[4]['text'] == self.buttonList[7]['text'] == "x" or \
                    self.buttonList[2]['text'] == self.buttonList[5]['text'] == self.buttonList[8]['text'] == "x":
                return 1

            if self.buttonList[0]['text'] == self.buttonList[1]['text'] == self.buttonList[2]['text'] == "o" or \
                    self.buttonList[3]['text'] == self.buttonList[4]['text'] == self.buttonList[5]['text'] == "o" or \
                    self.buttonList[6]['text'] == self.buttonList[7]['text'] == self.buttonList[8]['text'] == "o":
                return 0
            elif self.buttonList[0]['image'] == self.buttonList[1]['image'] == self.buttonList[2]['image'] == "x" or \
                    self.buttonList[3]['image'] == self.buttonList[4]['image'] == self.buttonList[5]['image'] == "x" or\
                    self.buttonList[6]['image'] == self.buttonList[7]['image'] == self.buttonList[8]['image'] == "x":
                return 1

            if self.buttonList[0]['text'] == self.buttonList[4]['text'] == self.buttonList[8]['text'] == "o" or \
                    self.buttonList[2]['text'] == self.buttonList[4]['text'] == self.buttonList[6]['text'] == "o":
                return 0
            elif self.buttonList[0]['text'] == self.buttonList[4]['text'] == self.buttonList[8]['text'] == "x" or \
                    self.buttonList[2]['text'] == self.buttonList[4]['text'] == self.buttonList[6]['text'] == "x":
                return 1

    def has_drow(self):
        count = 0
        for row in range(3):
            for col in range(3):
                if self.buttonList[row * 3 + col]['text'] == "empty":
                    count += 1
        if count == 0:
            return True
        else:
            return False

    def __init__(self):
        self.imageList = []
        self.imageList.append(PhotoImage(file='o.gif'))
        self.imageList.append(PhotoImage(file='x.gif'))
        self.imageList.append(PhotoImage(file='empty.gif'))
        self.buttonList = []
        self.turn = STATE_O_TURN  # T => O, F => X
        frame1 = Frame(window)
        frame1.pack()
        for row in range(3):
            for col in range(3):
                self.buttonList.append(Button(frame1, image=self.imageList[2], text="empty", command=lambda Row=row, Col=col : self.pressed(Row, Col)))
                self.buttonList[row * 3 + col].grid(row=row, column=col)

        window.mainloop()

TicTacToe()