import functools

number = [1,2,3,4]
def acc(counte, ites):
    print("NO.",counte)
    print("it",ites)
    return counte + ites

result = functools.reduce(acc, number)

print(result)