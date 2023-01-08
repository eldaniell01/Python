from tkinter import *

root = Tk()

def myb():
    mylabel=Label(root, text='este es un boton')
    mylabel.pack()


myButton = Button(root, text='soy un boton')
myButton2 = Button(root, text='soy un boton', state=DISABLED)
myButton3 = Button(root, text='soy un boton', padx=100, pady=100)
myButton4 = Button(root, text='soy un boton', command=myb)
myButton5 = Button(root, text='soy un boton', command=myb, fg="red", bg="#161F30")

myButton.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()
myButton5.pack()



root.mainloop()