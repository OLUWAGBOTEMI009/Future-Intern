# Tic Tac Toe game 


# create a function that prints the game board.
def print_board(board):
    """Function to print the Tic Tac Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


# create a function that set the boards and the rules of the game.
def check_win(board, player):
    # Function to check if a player has won.
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    # Function to check if the game is a draw.
    return all(space != ' ' for space in board)

def get_valid_move(board):
    # Function to get a valid move from the player.
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Please try again.")
            else:
                return move
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def play_game():
    # Function to play a single game of Tic Tac Toe.
    board = [' ' for _ in range(9)]  # Initial empty board
    current_player = 'X'  # X always goes first
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get the player's move and update the board
        move = get_valid_move(board)
        board[move] = current_player
        
        # Check for win
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


# create a function that defines the game.
def main():
    # Main function to run the Tic Tac Toe game.
    while True:
        play_game()  # Start a game
        
        # Ask the players if they want to play again or exit
        while True:
            replay = input("Would you like to play again? (yes/no): ").lower()
            if replay in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")
        
        if replay == 'no':
            print("Thanks for playing!")
            break

# Run the game.
if __name__ == "__main__":
    main()
