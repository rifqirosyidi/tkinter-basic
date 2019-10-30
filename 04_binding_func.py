from tkinter import *

root = Tk()


def print_something():
    print("something")


button = Button(root, text="Call Func", command=print_something)
button.pack()

root.mainloop()
