from tkinter import *


def do_something():
    print("DO SOMETHING")


root = Tk()

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project...", command=do_something)
file_menu.add_command(label="New...", command=do_something)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=do_something)

edit_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=do_something)

root.mainloop()