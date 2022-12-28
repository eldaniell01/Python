import random

paises = ['col', 'mes', 'bol', 'pe']

popu2 ={pais: random.randint(1, 30) for pais in paises}

print(popu2)

popu3 = {pais: contry for (pais, contry) in popu2.items() if contry <20}

print(popu3)

text = 'hola, soy daniel'

dic ={c: text.count(c) for c in text if c in 'aeiou'}

print(dic)