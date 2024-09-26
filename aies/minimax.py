def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float("inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "X"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("aies assignment 2")
    print_board(board)

    while True:
        # Player's turn
        row = int(input("enter row"))
        col = int(input("enter column"))
        if board[row][col] != " ":
            print("invalid move")
            continue
        board[row][col] = "O"
        print_board(board)

        if is_winner(board, "O"):
            print("you win!")
            break
        if is_board_full(board):
            print("tie!")
            break

        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "X"
        print_board(board)

        if is_winner(board, "X"):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()