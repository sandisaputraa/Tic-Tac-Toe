import random

def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        for cell in row:
            print("|   " + str(cell) + "   ", end="")
        print("|")
    print("+-------" * 3 + "+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Invalid move. Please choose a number between 1 and 9.")
            
            row, col = divmod(move-1, 3)
            if board[row][col] in ['O', 'X']:
                raise ValueError("This square is already occupied. Choose another one.")
            
            board[row][col] = 'O'
            break
        except ValueError as e:
            print(e)

def make_list_of_free_fields(board):
    free_fields = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell not in ['O', 'X']:
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    
    for condition in win_conditions:
        if all(board[row][col] == sign for row, col in condition):
            return True
    return False

def minimax(board, depth, is_max):
    if victory_for(board, 'X'):
        return 1
    if victory_for(board, 'O'):
        return -1
    if not make_list_of_free_fields(board):
        return 0
    
    if is_max:
        best_score = -float('inf')
        for row, col in make_list_of_free_fields(board):
            board[row][col] = 'X'
            score = minimax(board, depth + 1, False)
            board[row][col] = row * 3 + col + 1
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in make_list_of_free_fields(board):
            board[row][col] = 'O'
            score = minimax(board, depth + 1, True)
            board[row][col] = row * 3 + col + 1
            best_score = min(best_score, score)
        return best_score

def draw_move(board):
    best_score = -float('inf')
    best_move = None
    for row, col in make_list_of_free_fields(board):
        board[row][col] = 'X'
        score = minimax(board, 0, False)
        board[row][col] = row * 3 + col + 1
        if score > best_score:
            best_score = score
            best_move = (row, col)
    if best_move:
        board[best_move[0]][best_move[1]] = 'X'

def choose_starting_player():
    while True:
        choice = input("Do you want to play first or second? (enter 'first' or 'second'): ").strip().lower()
        if choice in ['first', 'second']:
            return choice
        else:
            print("Invalid choice. Please enter 'first' or 'second'.")

def tic_tac_toe():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    player_turn = choose_starting_player()
    
    while True:
        if player_turn == 'first':
            display_board(board)
            enter_move(board)
            if victory_for(board, 'O'):
                display_board(board)
                print("Congratulations! You won!")
                break
            if not make_list_of_free_fields(board):
                display_board(board)
                print("It's a tie!")
                break
            draw_move(board)
            if victory_for(board, 'X'):
                display_board(board)
                print("The computer won. Better luck next time!")
                break
            if not make_list_of_free_fields(board):
                display_board(board)
                print("It's a tie!")
                break
        else:
            draw_move(board)
            display_board(board)
            if victory_for(board, 'X'):
                display_board(board)
                print("The computer won. Better luck next time!")
                break
            if not make_list_of_free_fields(board):
                display_board(board)
                print("It's a tie!")
                break
            enter_move(board)
            if victory_for(board, 'O'):
                display_board(board)
                print("Congratulations! You won!")
                break
            if not make_list_of_free_fields(board):
                display_board(board)
                print("It's a tie!")
                break

if __name__ == "__main__":
    tic_tac_toe()
