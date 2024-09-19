class nqueens:
    def __init__(self, bsize, q):
        self.bsize = bsize
        self.q = q
        self.board = [0] * bsize  

    def input(self):
        self.bsize = int(input("Enter the size of the matrix: "))
        self.q = int(input("Enter the number of queens: "))
        self.init_board()

    def init_board(self):
        self.board = [0] * self.q

    def calculate_conflicts(self):
        conflicts = 0
        for i in range(self.q):
            for j in range(i + 1, self.q):
                if self.board[i] == self.board[j] or \
                   (self.board[i] - self.board[j]) == (i - j) or \
                   (self.board[j] - self.board[i]) == (i - j):
                    conflicts += 1
        return conflicts

    def hill_climb(self):

        for row in range(self.q):
            best_position = self.board[row]
            best_conflicts = self.calculate_conflicts()

            for position in range(self.bsize):
                self.board[row] = position
                current_conflicts = self.calculate_conflicts()
                if current_conflicts < best_conflicts:
                    best_conflicts = current_conflicts
                    best_position = position

            self.board[row] = best_position

        final_conflicts = self.calculate_conflicts()
        return final_conflicts  

    def print_board(self):
        for i in range(self.bsize):
            row = ['.'] * self.bsize
            if i < self.q:
                row[self.board[i]] = 'Q'
            print(' '.join(row))
        print()


kevin = nqueens(0, 0)
kevin.input()
kevin.hill_climb()
kevin.print_board()
