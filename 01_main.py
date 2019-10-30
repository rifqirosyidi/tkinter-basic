from tkinter import *

root = Tk()

# Create Frame
top_frame = Frame(root)
bot_frame = Frame(root)

# Pack The Frame
top_frame.pack()
bot_frame.pack(side=BOTTOM)

# Create 3 Button ( Top = 2, Bottom = 1)
button_1 = Button(top_frame, text="button 1", fg="red")
button_2 = Button(top_frame, text="button 2", fg="blue")
button_3 = Button(top_frame, text="button 3", fg="green")
button_4 = Button(bot_frame, text="button 4", fg="purple")

# Pack The Button
button_1.pack(side=LEFT)
button_2.pack(side=LEFT)
button_3.pack(side=LEFT)
button_4.pack()

root.mainloop()  # Make the windows constantly display
