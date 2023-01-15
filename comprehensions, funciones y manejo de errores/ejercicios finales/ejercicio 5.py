import functools
original = [1,2,3,4,5] 
new = []

for x in original:
	new.append(x * 2)
 
print(new)

n = list(map(lambda x: x *2, original))
print(n)