def increment(x):
    return x +1


def hof(x, func):
    return x+func(x)

resul = hof(2, increment)
print(resul)

increment2 = lambda x: x+1


hof2 = lambda x, func: x+func(x)
resul2= hof2(2, increment2)

print(resul2)