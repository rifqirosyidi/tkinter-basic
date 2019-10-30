from tkinter import *

root = Tk()

one = Label(root, text="One", fg="white", bg="black")
one.pack()

two = Label(root, text="Two", fg="white", bg="green")
two.pack(fill=X)

three = Label(root, text="Three", fg="black", bg="yellow")
three.pack(side=LEFT, fill=Y)

root.mainloop()

