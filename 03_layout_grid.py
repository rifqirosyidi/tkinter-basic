from tkinter import *

root = Tk()

txt_name = Label(root, text="Name")
txt_pass = Label(root, text="Password")
inp_name = Entry(root)
inp_pass = Entry(root)

# Align Using "Sticky" With the value N, W, E, S (North-Top, West-Left, South-Bottom, East-Right)
txt_name.grid(row=0, sticky=E)
txt_pass.grid(row=1, sticky=E)
inp_name.grid(row=0, column=1)
inp_pass.grid(row=1, column=1)

# Checkbox With Column Span
chk_logg = Checkbutton(root, text="Keep me logged in!")
chk_logg.grid(columnspan=2)

root.mainloop()
