numbers = []

"""for element in range(1,11):
    numbers.append(element*2)

print(numbers)


number2 = [element*2 for element in range(1,11)]
print(number2)"""

for element in range(1,11):
    if element%2==0:
        numbers.append(element*2)

print(numbers)


number2 = [element *2 for element in range(1,11) if element%2 ==0]
print(number2)