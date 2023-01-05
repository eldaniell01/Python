numbers = [1,2,3,4]

numbers2 =[]
for i in numbers:
    numbers2.append(i*2)


numbers3 = list(map(lambda i: i*2, numbers))

print(numbers)
print(numbers2)
print(numbers3)

numbers4= [1,2,3,4]
numbers5 = [5,6,7]

resul = list(map(lambda x, y : x+y, numbers4, numbers5))

print(resul)