from tkinter import *

root = Tk()

input = Entry(root, )
input.pack()
def sumar():
    n = input.get()
    lab = Label(root, text=input.get())
    print(type(n))
    lab.pack()
mybutton = Button(root, text='sumar', command=sumar)
mybutton.pack()
root.mainloop() 