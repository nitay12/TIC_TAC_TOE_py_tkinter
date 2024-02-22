import tkinter.messagebox
from tkinter import *
from tkinter import ttk

current_player = "X"
buttons = []

root = Tk()
root.title("Tic Tac Toe")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
current_player_label = ttk.Label(mainframe, text="Current player: X")
current_player_label.grid(column=0, row=0, sticky=W)


def reset_game():
    global current_player
    current_player = "X"
    current_player_label["text"] = f"Current player: {current_player}"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""


def check_draw():
    return all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))


def on_button_pressed(col, row):
    global current_player
    # switch the button label to the current player shape
    if buttons[col][row]["text"] == "":
        buttons[col][row]["text"] = current_player
        if check_winning(col, row):
            tkinter.messagebox.showinfo("Winner", f"{current_player} won!")
            reset_game()
            return
        if check_draw():
            tkinter.messagebox.showinfo("Draw", "It's a draw!")
            reset_game()
            return
            # switch current player to the other shape
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        current_player_label["text"] = f"Current player: {current_player}"

        pass


def check_winning(col, row):
    # Check column
    if all(buttons[col][i]["text"] == current_player for i in range(3)):
        return True
    # Check row
    elif all(buttons[i][row]["text"] == current_player for i in range(3)):
        return True
        # Check diagonals
    elif row == col and all(buttons[i][i]["text"] == current_player for i in range(3)):
        return True
    elif row + col == 2 and all(buttons[i][2 - i]["text"] == current_player for i in range(3)):
        return True
    else:
        return False


for i in range(1, 4):
    buttons_row = []
    for j in range(1, 4):
        button = ttk.Button(mainframe, text="", command=lambda row=i - 1, col=j - 1: on_button_pressed(row, col))
        button.grid(column=i, row=j, sticky=W)
        buttons_row.append(button)
    buttons.append(buttons_row)

root.mainloop()
