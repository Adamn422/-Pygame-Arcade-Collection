import tkinter as tk
from tkinter import messagebox

# Function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to handle button clicks
def button_click(row, col):
    global active_player, board_buttons, game_board

    # Check if the clicked button is already occupied
    if board_buttons[row][col]["text"] != " ":
        return

    # Update the clicked button with the active player's symbol
    board_buttons[row][col]["text"] = active_player

    # Update the game board
    game_board[row][col] = active_player

    # Check for a win
    if check_win(game_board, active_player):
        messagebox.showinfo("Game Over", f"Player {active_player} wins!")
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            reset_game()
        else:
            root.quit()
        return

    # Check for a tie
    if all(cell != " " for row in game_board for cell in row):
        messagebox.showinfo("Game Over", "It's a tie!")
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            reset_game()
        else:
            root.quit()
        return

    # Switch active player
    active_player = "O" if active_player == "X" else "X"

# Function to reset the game
def reset_game():
    global active_player, board_buttons, game_board

    # Clear the game board
    game_board = [[" " for _ in range(3)] for _ in range(3)]

    # Reset button text and state
    for row in range(3):
        for col in range(3):
            board_buttons[row][col]["text"] = " "
            board_buttons[row][col]["state"] = tk.NORMAL

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the game board buttons
board_buttons = [[None] * 3 for _ in range(3)]
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=" ", width=10, height=5, font=("Arial", 20, "bold"),
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        board_buttons[row][col] = button

# Create the game board
game_board = [[" " for _ in range(3)] for _ in range(3)]

# Set the active player
active_player = "X"

# Start the main event loop
root.mainloop()
