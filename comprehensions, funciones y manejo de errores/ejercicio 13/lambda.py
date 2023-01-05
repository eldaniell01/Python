def increment(x):
    return x +1

resul = increment(10)

print(resul)

increment2 = lambda x : x+1


result2 = increment2(20)
print(result2)

fullname = lambda x, j : x +" " + j

res = fullname('daniel', 'montepeque')
print(res)