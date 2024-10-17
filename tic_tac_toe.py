from tkinter import *
from tkinter import messagebox

# Initialize global variables
Player1 = "X"
stop_game = False


# Function for handling button clicks
def clicked(r, c):
    global Player1, stop_game

    # Check if the button is already clicked or the game is over
    if states[r][c] == 0 and not stop_game:
        # Update the button's text and the game state
        if Player1 == "X":
            b[r][c].configure(text="X")
            states[r][c] = "X"
            Player1 = "O"
        else:
            b[r][c].configure(text="O")
            states[r][c] = "O"
            Player1 = "X"

        check_if_win()  # Check if there's a winner or a tie


# Function for checking if there is a winner or a tie
def check_if_win():
    global stop_game

    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:  # Check rows
            stop_game = True
            messagebox.showinfo("Winner", states[i][0] + " Won!")
            return
        if states[0][i] == states[1][i] == states[2][i] != 0:  # Check columns
            stop_game = True
            messagebox.showinfo("Winner", states[0][i] + " Won!")
            return

    # Check diagonals
    if states[0][0] == states[1][1] == states[2][2] != 0:
        stop_game = True
        messagebox.showinfo("Winner", states[0][0] + " Won!")
        return
    if states[0][2] == states[1][1] == states[2][0] != 0:
        stop_game = True
        messagebox.showinfo("Winner", states[0][2] + " Won!")
        return

    # Check for a tie (if all buttons are filled and no winner)
    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "It's a Tie!")


# Design the window
root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

# Button and state initialization
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Buttons
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # States for tracking moves

# Create buttons for the grid
for i in range(3):
    for j in range(3):
        b[i][j] = Button(
            height=4,
            width=8,
            font=("Helvetica", "20"),
            command=lambda r=i, c=j: clicked(r, c),
        )
        b[i][j].grid(row=i, column=j)

# Start the main loop
mainloop()
