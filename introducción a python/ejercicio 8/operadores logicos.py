"""
    and
"""

print('AND')
print('true and true', True and True)
print('true and false', True and False)
print('false and true', False and True)
print('false and false', False and False)


print(10>5 and 5<10)
print(10>5 and 5>10)

stock = int(input("ingrese el stock "))

print(stock >=100 and stock <=1000)


"""
    or
"""

print('OR')
print('true or true', True or True)
print('true or false', True or False)
print('false or true', False or True)
print('false or false', False or False)

rol = input("ingrese un rol ")

print(rol =='admin' or rol == "vendedor")