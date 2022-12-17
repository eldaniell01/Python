"""
    CRUD: crear, eliminar, leer, actualizar 
"""

numbers = [1, 2, 3, 4, 5, 6]

print(numbers[1])

numbers[-1] = 10
print(numbers)

numbers.append(100)
print(numbers)

numbers.insert(0, 100)
print(numbers)

numbers.insert(2, 'cambio')
print(numbers)

tareas = ['tarea 1', 'tarea 2', 'tarea 3']
new_tarea = numbers+tareas
print(new_tarea)

print(new_tarea.index('tarea 2'))

index = new_tarea.index('tarea 2')
new_tarea[index]= 'hombreS'
print(new_tarea)


new_tarea.remove('tarea 3')
print(new_tarea)

new_tarea.pop()
print(new_tarea)

new_tarea.pop(0)
print(new_tarea)

new_tarea.reverse()
print(new_tarea)

num = [2, 5, 3, 4, 1]
num.sort()
print(num)