import tkinter as tk

def create_game_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", width=6, height=2,
                               command=lambda row=i, col=j: button_click(row, col))
            button.grid(row=i, column=j)
            buttons[i][j] = button

def button_click(row, col):
    if buttons[row][col]["text"] == "":
        if current_player == "X":
            buttons[row][col]["text"] = "X"
            buttons[row][col]["fg"] = "blue"
        else:
            buttons[row][col]["text"] = "O"
            buttons[row][col]["fg"] = "red"
        check_winner()
        switch_player()

def check_winner():
    global game_over
    # Check rows
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            game_over = True
            winner_label.config(text=f"{buttons[i][0]['text']} wins!")
            break
    # Check columns
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            game_over = True
            winner_label.config(text=f"{buttons[0][i]['text']} wins!")
            break
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        game_over = True
        winner_label.config(text=f"{buttons[0][0]['text']} wins!")
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        game_over = True
        winner_label.config(text=f"{buttons[0][2]['text']} wins!")
    # Check for draw
    if not game_over and all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        game_over = True
        winner_label.config(text="It's a draw!")

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def reset_game():
    global game_over, current_player
    game_over = False
    current_player = "X"
    winner_label.config(text="")
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create the game board and buttons
buttons = [[None] * 3 for _ in range(3)]
create_game_board()

# Create a label to display the winner
winner_label = tk.Label(window, text="", font=("Arial", 16))
winner_label.grid(row=3, column=0, columnspan=3)

# Create a reset button
reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the game
current_player = "X"
game_over = False
window.mainloop()