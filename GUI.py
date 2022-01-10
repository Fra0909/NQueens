from tkinter import *

root = Tk()


class GUI():

    def __init__(self, solutions):
        self.solutions = solutions
        self.current_solution = solutions[0]
        self.size = len(self.current_solution)
        self.grid = self.getGrid()
        self.placeQueens()

        prev = Button(root, text='<', command=lambda: self.prevSolution())
        prev.grid(row=self.size, column=int(self.size) - 3)
        zero = Button(root, text='⌂', command=lambda: self.firstSolution())
        zero.grid(row=self.size, column=int(self.size) - 2)
        self.counterLabel = Label(root, text='{}/{}'.format(self.solutions.index(self.current_solution) + 1,
                                                            len(self.solutions)))
        self.counterLabel.grid(row=self.size, column=0)
        next = Button(root, text='>', command=lambda: self.nextSolution())
        next.grid(row=self.size, column=int(self.size) - 1)
        root.title("NQueens")
        root.mainloop()

    def getGrid(self):
        labels = [[] for x in range(self.size)]
        colour = False
        for row in range(self.size):
            for column in range(self.size):
                if colour:
                    labels[row].append(Label(root, text='', font=("courier", 8), width=8, height=4, bg='#000'))
                else:
                    labels[row].append(Label(root, text='', font=("courier", 8), width=8, height=4, bg='#FFF'))
                colour = not colour
                labels[row][column].grid(row=row, column=column, sticky='nesw')
            colour = not colour if self.size % 2 == 0 else colour
        return labels

    def placeQueens(self):
        for row in range(self.size):
            self.grid[row][self.current_solution[row]].config(text='', bg='#EB3')

    def eraseBoard(self, grid):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column].cget('bg') == "#EB3" and self.grid[row][column-1].cget('bg') == "#000":
                    self.grid[row][column].config(bg = "#FFF")
                elif self.grid[row][column].cget('bg') == '#EB3' and self.grid[row][column-1].cget('bg') == "#FFF":
                    self.grid[row][column].config(bg = "#000")



    def firstSolution(self):
        self.eraseBoard(self.grid)
        self.current_solution = self.solutions[0]
        self.placeQueens()
        self.counterLabel.config(
            text='{}/{}'.format(self.solutions.index(self.current_solution) + 1, len(self.solutions)))

    def nextSolution(self):
        self.eraseBoard(self.grid)
        if not (self.solutions.index(self.current_solution) + 1 >= len(self.solutions)):
            self.current_solution = self.solutions[self.solutions.index(self.current_solution) + 1]
        else:
            self.current_solution = self.solutions[0]

        self.placeQueens()
        self.counterLabel.config(
            text='{}/{}'.format(self.solutions.index(self.current_solution) + 1, len(self.solutions)))

    def prevSolution(self):
        self.eraseBoard(self.grid)
        if self.solutions.index(self.current_solution) <= 0:
            self.current_solution = self.solutions[-1]
        else:
            self.current_solution = self.solutions[self.solutions.index(self.current_solution) - 1]

        self.placeQueens()
        self.counterLabel.config(
            text='{}/{}'.format(self.solutions.index(self.current_solution) + 1, len(self.solutions)))
