conjuntoA =  {'col', 'mex', 'bol'}
conjuntoB = {'pe', 'bol'}

conjunto = conjuntoA.union(conjuntoB)

print(conjunto)

print(conjuntoA | conjuntoB)

conjunto = conjuntoA.intersection(conjuntoB)

print((conjunto))

print(conjuntoA & conjuntoB)

conjunto = conjuntoA.difference(conjuntoB)

print(conjunto)

print(conjuntoA - conjuntoB)

conjunto = conjuntoA.symmetric_difference(conjuntoB)

print(conjunto)

print(conjuntoA ^ conjuntoB)