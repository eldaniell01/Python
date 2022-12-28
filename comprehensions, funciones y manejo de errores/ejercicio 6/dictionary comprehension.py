import random

diccionario = {}
for i in range(1,11):
    diccionario[i] = i *2
    
print(diccionario)


dict_v2 = {i:i*2 for i in range(1, 5)}
print(diccionario)

paises = ['col', 'mes', 'bol', 'pe']

popu = {}

for pais in paises:
    popu[pais] = random.randint(1, 10)

print(popu)


popu2 ={pais: random.randint(1, 10) for pais in paises}

print(popu2)


names = ['daniel', 'marielos', 'angela']
age = [25, 17, 16]

print(list(zip(names, age)))

diccf = {names: age for (names, age) in zip(names, age)}

print(diccf)