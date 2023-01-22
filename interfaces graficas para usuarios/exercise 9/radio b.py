from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('radio buttons')
r = StringVar()

lista = [
    ("carne","carne"),
    ("frijol","frijol"),
    ("mushroom","mushroom"),
    ("onion","onion"),
]

for text, valor in lista:
    Radiobutton(root, text=text, variable=r, value=valor).pack()

def opcion(valor):
    mostrar = Label(root, text=valor)
    mostrar.pack()

"""Radiobutton(root, text='option1', variable=r, value=1, command=lambda: opcion(r.get())).pack()
Radiobutton(root, text='option2', variable=r, value=2, command=lambda: opcion(r.get())).pack()"""

mostrar = Label(root, text=r.get())
mostrar.pack()

guardar = Button(root, text='guardar', command=lambda: opcion(r.get())).pack()


root.mainloop()