from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('matplotlib')
root.geometry("400x600")
def grafica():
    calquiera = np.random.normal(20000, 25000, 5000)
    plt.polar(calquiera)
    plt.show()
    
graficar = Button(root, text='graficar', command=grafica)
graficar.pack()
root.mainloop()