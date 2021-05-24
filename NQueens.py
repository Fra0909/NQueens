import GUI


class Queens():

    def __init__(self, size):
        self.size = size
        self.answers = 0
        self.solutions = []

    def calculate(self):
        queens = [0] * self.size
        self.solve(queens, 0, 0)
        return self.solutions

    def solve(self, queens, row, column):
        if row == self.size:
            self.answers += 1
            self.solutions.append(queens.copy())
            return True
        else:
            while column < self.size:
                if self.check(queens, row, column):
                    queens[row] = column
                    self.solve(queens, row + 1, 0)
                column += 1

    def check(self, queens, row, column):
        for i in range(row):
            if queens[i] == column:
                return False
            if column + row == queens[i] + i:
                return False
            if column - row == queens[i] - i:
                return False
        return True


if __name__ == '__main__':
    size = 8
    board = Queens(size)
    solutions = board.calculate()
    gui = GUI.GUI(size,solutions)
    gui.createBoard()
