my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇
for numero in my_list:
  if not numero <0:
    new_list.append(numero)

print(new_list)