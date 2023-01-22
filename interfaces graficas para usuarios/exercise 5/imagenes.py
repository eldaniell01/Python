from tkinter import *
from PIL import ImageTk, Image
root = Tk()
ico = PhotoImage(file="interfaces graficas para usuarios/exercise 5/sds.png")
root.iconphoto(True, ico)


img = ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 5/sds.png"))
mostrar = Label(image=img)
mostrar.pack()

button = Button(root, text='salir', command=root.quit)
button.pack()
root.mainloop()