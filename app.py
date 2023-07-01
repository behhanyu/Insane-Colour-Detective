from flask import Flask, render_template
import tkinter as tk
import tkinter.font as tkFont
import math
import random
import time

app = Flask(__name__)

class Game(tk.Frame):
    shouldReset = True
    answer = 0
    score = 0
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f1 = tkFont.Font(size=48, family="Courier New")
        f2 = tkFont.Font(size=32, family="Courier New")
        self.lblNum = tk.Label(self, text="Press Any to start", height=1, width=18, font=f1) 
        self.lblNum.grid(row=0, column=0, columnspan=4, sticky=tk.NE + tk.SW)

        rgb1 = (183, 247, 49)
        bgcolor = '#{0:02x}{1:02x}{2:02x}'.format(*rgb1)
        self.buttons = {}
        for i in range(16):
            self.buttons[i] = tk.Button(self, height=1, width=1, command=lambda f=i: self.clickBtn(f), font=f1, bg=bgcolor) 
            self.buttons[i].grid(row=1 + i // 4, column=i % 4, sticky=tk.NE + tk.SW, padx=5, pady=5)
    
    def changeColor(self):
        r = random.randint(0, 256)
        g = random.randint(0, 256)
        b = random.randint(0, 256)

        a = 50 - self.score * 2
        if a < 5:
            a = 5
        rgb1 = (r, g, b)
        if r > a:
            rgb2 = (r - a, g, b)
        else:
            rgb2 = (r + a, g, b)
        print(r, g, b)
        bgcolor1 = '#{0:02x}{1:02x}{2:02x}'.format(*rgb1)
        bgcolor2 = '#{0:02x}{1:02x}{2:02x}'.format(*rgb2)
        for i in range(16):
            self.buttons[i].configure(bg=bgcolor1)
        self.answer = random.randint(0, 15)
        self.buttons[self.answer].configure(bg=bgcolor2)
      
    def checkAnswer(self, index):
        if self.answer == index:
            self.score += 1
            self.lblNum.configure(text=self.score)
            self.changeColor()
        else: 
            self.score = 0
            self.lblNum.configure(text=self.score)
            self.changeColor()

    def clickBtn(self, index):
        self.checkAnswer(index)
        self.changeColor()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    game = Game(tk.Tk())
    game.master.title("Insane Colour Detective")
    game.mainloop()
