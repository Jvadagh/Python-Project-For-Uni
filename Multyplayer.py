from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser


def Multytictactoe():
    root = Tk()
    root.title('Tic-Tac-Toe')

    defultcolor = 'red'
    clicked = True
    count = 0

    def color_changer1():
        color_changer1 = colorchooser.askcolor()[1]
        if color_changer1:
            # Build our buttons again
            b1.config(background=color_changer1)
            b2.config(background=color_changer1)
            b3.config(background=color_changer1)

            b4.config(background=color_changer1)
            b5.config(background=color_changer1)
            b6.config(background=color_changer1)

            b7.config(background=color_changer1)
            b8.config(background=color_changer1)
            b9.config(background=color_changer1)

    def color_changer2():
        global color_changer2
        global defultcolor
        color_changer2 = colorchooser.askcolor()[1]
        if color_changer2:
            defultcolor = color_changer2

    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    def checkifwon(color2):
        global winner
        winner = False
        # check for "X"s Win
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg=color2)
            b2.config(bg=color2)
            b3.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg=color2)
            b5.config(bg=color2)
            b6.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg=color2)
            b8.config(bg=color2)
            b9.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg=color2)
            b4.config(bg=color2)
            b7.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg=color2)
            b5.config(bg=color2)
            b8.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg=color2)
            b6.config(bg=color2)
            b9.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg=color2)
            b5.config(bg=color2)
            b9.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg=color2)
            b5.config(bg=color2)
            b7.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS X Wins !!")
            disable_all_buttons()

        # check for "O"s Win

        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg=color2)
            b2.config(bg=color2)
            b3.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg=color2)
            b5.config(bg=color2)
            b6.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg=color2)
            b8.config(bg=color2)
            b9.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg=color2)
            b4.config(bg=color2)
            b7.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg=color2)
            b5.config(bg=color2)
            b8.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg=color2)
            b6.config(bg=color2)
            b9.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg=color2)
            b5.config(bg=color2)
            b9.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg=color2)
            b5.config(bg=color2)
            b7.config(bg=color2)
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS O Wins !!")
            disable_all_buttons()

        if count == 9 and winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
            disable_all_buttons()

    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked is True:
            b["text"] = "X"
            clicked = False
            count += 1
            checkifwon(defultcolor)


        elif b["text"] == " " and clicked is False:
            b["text"] = "O"
            clicked = True
            count += 1
            checkifwon(defultcolor)


        else:
            messagebox.showerror("Tic Tac Toe", "Hey ! That box has already been selected\nPick Another box... ")

    # Start the game over !
    def reset():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count
        clicked = True
        count = 0
        Color1 = "grey"
        # Build our buttons
        b1 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b3))

        b4 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b6))

        b7 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 35), height=3, width=6, bg=Color1,
                    command=lambda: b_click(b9))

        # Grid our buttons to screen
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)

        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)

        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    # Create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Options Menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Rest Game", command=reset)
    options_menu.add_command(label="Change Primary Colors", command=color_changer1)
    options_menu.add_command(label="Change Secondary Colors", command=color_changer2)
    options_menu.add_separator()
    options_menu.add_command(label="Exit", command=root.quit)
    reset()
    root.mainloop()
