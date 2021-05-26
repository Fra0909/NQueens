from tkinter import *
root = Tk()

class GUI():

    def __init__(self, size, solutions):
        self.size = size
        self.solutions = solutions

    def get_new_solution(self, index, step):
        if index == len(self.solutions)-1 and step:
            self.createBoard(0)
            return
        if index == 0 and not step:
            self.createBoard(len(self.solutions)-1)
            return
        if step:
            print(index)
            self.createBoard(index+1)
            return
        self.createBoard(index-1)

    def createBoard(self, index = 0, last_colour = True):
        solutions = self.solutions[index]
        for i in range(self.size):
            last_colour = not last_colour if self.size %2 == 0 else last_colour
            for j in range (self.size):
                if solutions[i] == j:
                    label = Label(root, text = '♛', font=("courier",8), width = 8, height = 4, fg='yellow',)
                else:
                    label = Label(root, text='', font=("courier",8), width=8, height=4)
                if last_colour:
                    label.config(bg='#000')
                    last_colour = False
                else:
                    label.config(bg='#FFF')
                    last_colour = True

                label.grid(row = i,column = j)
        prev = Button(root, text ='<', command = lambda: self.get_new_solution(index,False))
        prev.grid(row = self.size, column = int(self.size)-3)
        zero = Button(root, text='⌂', command=lambda: self.get_new_solution(len(self.solutions)-1, False))
        zero.grid(row=self.size, column=int(self.size) - 2)
        label2 = Label(root,text ='{}/{}'.format(index+1,len(self.solutions)))
        label2.grid(row = self.size,column=0)
        next = Button(root, text='>', command = lambda: self.get_new_solution(index,True))
        next.grid(row=self.size, column=int(self.size)-1)
        root.title("NQueens")
        root.mainloop()
