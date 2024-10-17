class NQueens:
    def __init__(self, bsize):
        self.bsize = bsize
        self.board = [-1] * bsize  # Initialize the board with -1 (no queen placed)
        self.board[0] = 0  # Place the first queen at (0, 0)

    def is_safe(self, row, col):
        # Check if placing a queen at (row, col) causes a conflict with previously placed queens
        for i in range(row):
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False  # Conflict found
        return True  # Safe to place queen

    def place_queens(self):
        # Start placing queens from row 1, as queen in row 0 is already placed
        for row in range(1, self.bsize):
            for col in range(self.bsize):
                if self.is_safe(row, col):
                    self.board[row] = col  # Place queen if it's safe
                    break  # Move to next row once a queen is placed
        return True

    def print_board(self):
        # Print the board with queens where they are placed
        for i in range(self.bsize):
            row = ['.'] * self.bsize
            if self.board[i] != -1:
                row[self.board[i]] = 'Q'
            print(' '.join(row))
        print()


# Input the board size
n = int(input("Enter the size of the matrix (e.g., 8 for an 8x8 board): "))

# Initialize and solve the N-Queens problem
nqueens_solver = NQueens(n)
nqueens_solver.place_queens()
print("Current board configuration:")
nqueens_solver.print_board()
