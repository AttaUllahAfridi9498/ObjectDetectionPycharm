from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()
#root = Tk()
top.geometry("400x200")

def show():
    name = askstring("Input", "Enter you name")
    print(name)
#var = StringVar()
#L = Label(root,textvariable=var, relief=RAISED )
#var.set("Hey!? How are you doing?")
B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()