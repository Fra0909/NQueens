from tkinter import *
import random
root = Tk()

class GUI():

    def __init__(self, size, solutions):
        self.size = size
        self.solutions = solutions

    def createBoard(self, index = 0):
        index = random.randint(0,92)
        solutions = self.solutions[index]
        if index == 92:
            index = 0
        elif index == -92:
            index = 0
        last_colour = True
        for i in range(self.size):
            if last_colour == True:
                last_colour = False
            else:
                last_colour = True
            for j in range (self.size):
                if solutions[i] == j:
                    label = Label(root, text = '♛', font=("courier",self.size), width = 8, height = 4, fg='yellow')
                else:
                    label = Label(root, text='', font=("courier", self.size), width=8, height=4)

                if last_colour == True:
                    label.config(bg='#000')
                    last_colour = False
                else:
                    label.config(bg='#FFF')
                    last_colour = True

                label.grid(row = i,column = j)
        prev = Button(root, text ='<', command = lambda: self.createBoard(index-1))
        prev.grid(row = self.size + 1, column = int(self.size/2)-1)
        next = Button(root, text='>', command = lambda: self.createBoard(index+1))
        next.grid(row=self.size + 1, column=int(self.size/2))
        root.mainloop()

