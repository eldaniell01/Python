from tkinter import *

root = Tk()
root.title("Calculadora simple")
root.configure(background='#22BABB')

e = Entry(root, width=50, font='Arial')
e.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

def agregar(num):
    """agregar _summary_

    agrega numeros al cuadro de texto

    Args:
        num (enteros): numeros por cada boton
    """
    add = e.get()
    e.delete(0,END)
    e.insert(0, str(add)+str(num))
count = 0
def sumar():
    global num1
    global operador 
    n = e.get()
    num1 = float(n)
    e.delete(0,END)
    operador = '+'
    
def restar():
    global num1
    global operador 
    n = e.get()
    num1 = float(n)
    e.delete(0,END)
    operador = '-'

def resultado():
    num2 = e.get()
    e.delete(0, END)
    if operador=='+':
        e.insert(0, num1+float(num2))
    elif operador=='-':
        e.insert(0,num1-float(num2))
    
def clear():
    e.delete(0,END)
   

num = Button(root, text="0", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(0))
num.grid(row=1, column=0)
num1 = Button(root, text="1", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(1))
num1.grid(row=1, column=1)
num2 = Button(root, text="2", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(2))
num2.grid(row=1, column=2)
num3 = Button(root, text="3", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(3))
num3.grid(row=2, column=0)
num4 = Button(root, text="4", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(4))
num4.grid(row=2, column=1)
num5 = Button(root, text="5", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(5))
num5.grid(row=2, column=2)
num6 = Button(root, text="6", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(6))
num6.grid(row=3, column=0)
num7 = Button(root, text="7", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(7))
num7.grid(row=3, column=1)
num8 = Button(root, text="8", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(8))
num8.grid(row=4, column=0)
num9 = Button(root, text="9", padx=40, pady=10, bg='#FA7F08', command=lambda: agregar(9))
num9.grid(row=4, column=1)
num10 = Button(root, text="+", padx=40, pady=10, bg='#FA7F08', command=sumar)
num10.grid(row=5, column=0)
num11 = Button(root, text="-", padx=40, pady=10, bg='#FA7F08', command=restar)
num11.grid(row=5, column=1)
num12 = Button(root, text="=", height=3, padx=40, pady=10, bg='#FA7F08', command=resultado)
num12.grid(row=3, column=2, rowspan=2)
num13 = Button(root, text="C", height=1, padx=40, pady=10, bg='#FA7F08', command=clear)
num13.grid(row=5, column=2)
root.mainloop()