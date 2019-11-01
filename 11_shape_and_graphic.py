from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=200)
canvas.pack()

# ***** LINE *****
# create_line (x_start, y_start, x_end, y_end)
black_line = canvas.create_line(0, 0, 100, 100)
blue_line = canvas.create_line(100, 100, 100, 200, fill="blue")
red_line = canvas.create_line(100, 100, 200, 0, fill="red")


# ***** RECTANGLE *****
# create_rectangle(x_start_point, y_start_point, +width, +height)
blue_box = canvas.create_rectangle(50, 50, 150, 150, fil="blue")


# ***** DELETE *****
# canvas.delete(red_line)
# canvas.delete(ALL)


root.mainloop()
