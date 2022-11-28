from tkinter import Tk, Menu, Label, Frame
class Test():

    def __init__(self):
        self.gui = Tk()
        self.gui.geometry("600x400")
        menu = Menu(self.gui)
        new_item1 = Menu(menu)
        menu.add_cascade(label='File', menu=new_item1)
        new_item1.add_command(label='Add', command=self.addlbl)
        new_item1.add_command(label='View', command=self.viewlbl)
        self.gui.config(menu=menu)
        self.gui.mainloop()

    def addlbl(self):
        self.frame = Frame(self.gui)
        self.frame.pack()
        lbl1 = Label(self.frame, text="Label 1")
        lbl1.grid(row=0, column=0)

    def viewlbl(self):
        print('frame exists {}'.format(self.frame.winfo_exists()))


T=Test()