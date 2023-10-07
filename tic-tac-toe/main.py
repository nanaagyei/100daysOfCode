# Function to print the current state of the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Function to check if there is a win condition on the board
def check_win(board):
    # Check rows for win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    # Check columns for win
    for col in range(len(board)):
        check_col = []
        for row in board:
            check_col.append(row[col])
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != ' ':
            return True
    # Check diagonals for win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

# Function for AI to make a move


def ai_move(board, player):
    # AI logic here
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                return

# Main function to run the game


def tic_tac_toe():
    # Initialize the game board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    # Choose game mode
    game_mode = input(
        "Enter 1 to play against another player, enter 2 to play against AI: ")
    while True:
        print_board(board)
        print(f"Player {current_player}, it's your turn.")
        # Get player input for move or make AI move
        if game_mode == '2' and current_player == 'O':
            ai_move(board, current_player)
        else:
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))
            # Check if the move is valid
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            # Make the move
            board[row][col] = current_player
        # Check if the current player has won
        if check_win(board):
            print(f"Player {current_player} wins!")
            break
        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'


# Start the game
tic_tac_toe()
