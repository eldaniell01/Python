calificaciones ={}

calificaciones['matematicas'] = 10
calificaciones['informatica'] = 6
calificaciones['lenguaje'] = 5
calificaciones['programacion'] = 9

for key in calificaciones:
    print(key)
    
for value in calificaciones.values():
    print(value)
    
for key, value in calificaciones.items():
    print('llave: {}, valor: {}'.format(key, value))
cont = 0  
promedio=0 
for value in calificaciones.values():
    promedio=promedio+value
    cont +=1
promedio =promedio/cont
print("el promedio es: {}".format(promedio))