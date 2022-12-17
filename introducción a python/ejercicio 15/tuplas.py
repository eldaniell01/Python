numbers = (1,2,3, 4, 4, 4)
text = ('hola', 'hola 2', 'hola 3')

print(numbers)
print(text)
print(type(numbers))
print(type(text))

print(numbers[0])

print(numbers.count(4))

#convertir tupla a lista

my_list = list(text)
print(my_list)
print(type(my_list))


#convertir lista a tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))