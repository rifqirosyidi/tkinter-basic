from tkinter import *

root = Tk()

photo = PhotoImage(file="image/person-male.png")
label = Label(root, image=photo)

label.pack()

root.mainloop()
