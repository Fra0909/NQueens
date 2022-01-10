import GUI


class Queens():

    def __init__(self, size):
        self.size = size
        self.solutions = []

    def getAllSolutions(self):
        self.findSolutions([0] * self.size)
        return self.solutions

    def findAllSolutions(self, queens, row=0, column=0):
        if row == self.size:
            self.solutions.append(queens.copy())
            return True
        else:
            while column < self.size:
                if self.isClash(queens, row, column):
                    queens[row] = column
                    self.findSolutions(queens, row + 1, 0)
                column += 1

    def isClash(self, queens, row, column):
        for i in range(row):
            if queens[i] == column or column + row == queens[i] + i or column - row == queens[i] - i:
                return False
        return True


if __name__ == '__main__':
    size = 6
    board = Queens(size)
    solutions = board.getSolutions()
    print(len(solutions))
    gui = GUI.GUI(solutions)
