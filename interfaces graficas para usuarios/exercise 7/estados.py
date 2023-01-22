from tkinter import *
from PIL import ImageTk, Image
root = Tk()


img1 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallhaven-zmmkkv.png"))
img2 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallpaper_1.jpg"))
img3 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallpaper_2.jpg"))
img4 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallpaper_3.jpg"))
img5 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallpaper_4.jpg"))
img6 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallpaper_5.jpg"))
img7 =  ImageTk.PhotoImage(Image.open("interfaces graficas para usuarios/exercise 6/img/wallpaperflare.com_wallpaper.jpg"))

list_img = [img1,img2,img3,img4,img5,img6,img7]
status = Label(root, text="1 de"+str(len(list_img)))
mostrar = Label(image=img1, width=800, height=600)
mostrar.grid(row=0, column=0, columnspan=3)
status.grid(row=2, column=2)


def atras(num):
    global mostrar
    global button3
    global button1
    global status
    
    mostrar.grid_forget()
    mostrar = Label(image=list_img[num-1], width=800, height=600)
    
    button3 = Button(root, text='>>', command=lambda: siguiente(num+1))
    button1 = Button(root, text='<<', command=lambda: atras(num -1))
    print(num)
    if num == 1:
        button1 = Button(root, text='>>', state=DISABLED)
    mostrar.grid(row=0, column=0, columnspan=3)
    button1.grid(row=1, column=0)
    button3.grid(row=1, column=2)
    
    status = Label(root, text=str(num)+" de "+str(len(list_img)))
    status.grid(row=2, column=2)

def siguiente(num):
    global mostrar
    global button3
    global button1
    mostrar.grid_forget()
    mostrar = Label(image=list_img[num-1], width=800, height=600)
    button3 = Button(root, text='>>', command=lambda: siguiente(num+1))
    button1 = Button(root, text='<<', command=lambda: atras(num -1))
    if num == len(list_img):
        button3 = Button(root, text='>>', state=DISABLED)
    mostrar.grid(row=0, column=0, columnspan=3)
    button1.grid(row=1, column=0)
    button3.grid(row=1, column=2)
    
    status = Label(root, text=str(num)+" de "+str(len(list_img)))
    status.grid(row=2, column=2)




button1 = Button(root, text='<<', command=lambda: atras(2))
button2 = Button(root, text='salir', command=root.quit)
button3 = Button(root, text='>>', command=lambda: siguiente(2))

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

root.mainloop()