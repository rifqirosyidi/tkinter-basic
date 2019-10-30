from tkinter import *

root = Tk()


def print_something(event):
    print(event)
    print("something")


button = Button(root, text="Call Func")
button.bind("<Button-1>", print_something)
button.pack()

root.mainloop()
