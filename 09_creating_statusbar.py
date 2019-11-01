from tkinter import *


def do_something():
    print("DO SOMETHING")


root = Tk()


#  ***** MAIN MENU *****

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

# ***** TOOLBAR *****

toolbar = Frame(root, bg="grey")

btn_insert_image = Button(toolbar, text="Insert Image", command=do_something)
btn_insert_image.pack(side=LEFT, padx=2, pady=2)
btn_print = Button(toolbar, text="Print", command=do_something)
btn_print.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** STATUS BAR *****

status = Label(root, text="Static Status Bar", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()