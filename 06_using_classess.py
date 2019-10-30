from tkinter import *


class SomeClass:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.print_button = Button(self.frame, text="Print Me", command=self.print_message)
        self.print_button.pack(side=LEFT)

        self.close_button = Button(self.frame, text="Close Me", command=self.frame.quit)
        self.close_button.pack(side=LEFT)


    def print_message(self):
        print("Print Me, Hi You Click Print Me")


root = Tk()
b = SomeClass(root)
root.mainloop()