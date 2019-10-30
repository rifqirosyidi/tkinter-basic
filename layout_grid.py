from tkinter import *

root = Tk()

txt_name = Label(root, text="Name")
txt_pass = Label(root, text="Password")
inp_name = Entry(root)
inp_pass = Entry(root)

txt_name.grid(row=0)
txt_pass.grid(row=1)
inp_name.grid(row=0, column=1)
inp_pass.grid(row=1, column=1)

root.mainloop()
