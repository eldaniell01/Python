persona ={
    'name': 'daniel',
    'lastname': 'montepeque',
    'edad': 25,
    'langs': ['python', 'javascript']
}
print(persona)


persona['name'] = 'alvaro'
print(persona)

persona['edad'] -= 3
print(persona)

persona['langs'].append('java')
print(persona)

del persona['lastname']
print(persona)

persona.pop('edad')
print(persona)

print(persona.items())

print(persona.keys())

print(persona.values())