import tkinter as tk
from tkinter import messagebox
# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")
# Global variables
current_player = "X"
game_board = [""] * 9
buttons = []
# Switch player
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
# Check for a win
def check_win():
    # Winning combinations
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)]
    
    for a, b, c in wins:
        if game_board[a] == game_board[b] == game_board[c] != "":
            return game_board[a]
    return ""
# Reset the game
def reset_game():
    global game_board, current_player
    game_board = [""] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="")
# Button click event
def button_click(idx):
    global game_board
    if game_board[idx] == "":
        game_board[idx] = current_player
        buttons[idx].config(text=current_player)
        
        winner = check_win()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif "" not in game_board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            switch_player()
# Create buttons
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 20), width=8, height=4,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)
root.mainloop()
