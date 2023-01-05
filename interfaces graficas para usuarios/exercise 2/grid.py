from tkinter import *

root = Tk()

mylabel = Label(root, text='hola mundo')
mylabe2 = Label(root, text='hola mundo2')

mylabel.grid(row=0, column=0)
mylabe2.grid(row=1, column=1)
root.mainloop()