print(not True)
print(not False)

"""
    and
"""

print('AND')
print('true and true', not (True and True))
print('true and false', not (True and False))
print('false and true', not (False and True))
print('false and false', not (False and False))


stock = int(input("ingrese el stock "))

print(not(stock >=100 and stock <=1000))
