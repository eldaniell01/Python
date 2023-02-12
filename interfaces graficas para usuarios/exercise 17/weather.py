from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root. title("weather")
root.geometry("600x400")

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=BBE3AEC6-0FF9-4A1A-AEC3-F9A9B0B83232


def localizar():
    """caja.get()
    ciudad = Label(root, text=caja.get())
    ciudad.grid(row=1, column=0, columnspan=0)"""
    try:
        api = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+caja.get()+"&distance=25&API_KEY=BBE3AEC6-0FF9-4A1A-AEC3-F9A9B0B83232")
        api2 = json.loads(api.content)
        city = api2[0]['ReportingArea']
        calidad = api2[0]['AQI']
        categoria = api2[0]['Category']['Name']
        if categoria == 'Good':
            color = 'green'
        elif categoria == 'Moderate':
            color = 'blue'
        elif categoria == 'Unhealthy for Sensitive Gropus':
            color = 'orange'
        elif categoria == 'Unhealthy':
            color = 'yellow'
        elif categoria == 'Very Unhealthy':
            color = 'red'
        elif categoria == 'Hazardous':
            color = 'black'

        texto = Label(root, text=city +" calidad "+ str(calidad) +" "+ categoria, background=color)
        texto.grid(row=0, column=0)

    except Exception as e:
        api2 = 'error'



caja = Entry(root)
caja.grid(row=2, column=0)

buscar = Button(root, text='buscar', command=localizar)
buscar.grid(row=2, column=1)

root. mainloop()