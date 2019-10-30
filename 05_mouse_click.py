from tkinter import *

root = Tk()


def left_click(event):
    print("LEFT")


def right_click(event):
    print("RIGHT")


def middle_click(event):
    print("MIDDLE")


frame = Frame(root, height=250, width=250)

frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)

frame.pack()

root.mainloop()
