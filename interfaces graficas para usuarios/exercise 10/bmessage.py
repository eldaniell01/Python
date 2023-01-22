from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('frames')

def mensaje():
    #devuelve ok
    messagebox.showinfo('mensaje de salid', "hola mundo")
    #devuelve ok
    messagebox.showwarning('mensaje de cuidad', "error")
    #devuelve ok
    messagebox.showerror('mensaje de error', "error d")
    #devuelve yes o no
    messagebox.askquestion('mensaje de pregunta', "error d")
    #devuelve 1 o 0
    messagebox.askokcancel('mensaje de error', "error d")
    #devuelve 1 o 0
    messagebox.askyesno('mensaje de error', "error d")


Button(root, text='mensaje', command=mensaje).pack()

root.mainloop()