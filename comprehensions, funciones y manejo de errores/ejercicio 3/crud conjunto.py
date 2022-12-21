paises = {'col', 'mex', 'bol'}

size = len(paises)
print(size)

print('mex' in paises)

#add

paises.add('gua')
print(paises)

#update

paises.update({'arg', 'ecu'})
print(paises)

#remove

paises.remove('gua')
print(paises)

#discard

paises.discard('hola')
print(paises)

#clear

paises.clear()
print(paises)