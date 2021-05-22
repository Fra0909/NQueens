import time
time_1 = time.time()

class Queens():

    def __init__(self,size):
        self.size = size
        self.answers = 0
        self.sol = []
        self.calculate()
        print("There are", self.answers, "answers for this size.")


    def printBoard(self, queens):
        self.board = []
        for i in range(self.size):
            self.board.append((["■"] * self.size))
            temp = queens[i]
            self.board[i][temp] = "♛"
            print(self.board[i])
        print("\n")
        self.sol.append(self.board)



    def calculate(self):
        queens = [0] * self.size
        self.solve(queens, 0, 0)


    def solve(self, queens, row, column):
        if row == self.size:
            self.answers +=1
            self.printBoard(queens)
            return True
        else:
            while column < self.size:
                if self.check(queens, row, column):
                    queens[row] = column
                    self.solve(queens, row + 1, 0)
                    column+=1
                else:
                    column+=1

    def check(self, queens ,row ,column):
        for i in range (row):
            if queens[i] == column:
                return False
            if column + row == queens[i] + i:
                return False
            if column - row == queens[i] - i:
                return False
        return True



Queens(int(input("Size of the chess table: ")))
time_2 = time.time()
print("It took", time_2 - time_1, "seconds to run the program!")
