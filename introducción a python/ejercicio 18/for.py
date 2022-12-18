for element in range(10):
    print(element)
    
for element2 in range(1,10):
    print(element2)
    
mi_lis= [1, 2,3,4,5,6]

for element3 in mi_lis:
    print(element3)
    
mi_tupla = ('daniel', 'angela', 'marielos')
for element4 in mi_tupla:
    print(element4)

persona = {
    'name': 'daniel',
    'lastname': 'montepeque',
    'edad': 25
}

for element5 in persona:
    print(persona[element5])
    
for key, value in persona.items():
    print(key, '=', value)


personas = [
    {
        'name': 'daniel',
        'age': 25
    },
    {
        'name': 'angela',
        'age': 16
    }
]

count = len(personas)
print(count)
for person in personas:
    print(person['name'])