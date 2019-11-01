from tkinter import *
import tkinter.messagebox

root = Tk()

# tkinter.messagebox.showinfo("Title", "Hello This is Message Box Test")

answer = tkinter.messagebox.askquestion("Title", "Do You Have a Name?")

if answer == "yes":
    tkinter.messagebox.showinfo("Title", "Hello This is Message Box Test")

root.mainloop()