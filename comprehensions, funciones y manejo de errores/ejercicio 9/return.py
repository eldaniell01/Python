

def rangos(inicio, fin):
    sum = 0
    for x in range(inicio,fin):
        sum+=x
    return sum
    
resul = rangos(1, 4)
print(resul)
rangos(1, 20)