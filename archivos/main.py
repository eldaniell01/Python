xfile=open('text.txt')
count = 0
for palabras in xfile:
    count +=1
    print(palabras)
print(count)   
xfile.close()
xfile=open('text.txt')
palabras = xfile.read()
print(len(palabras))
print(palabras[2:6])
xfile.close()
xfile=open('text.txt')
for line in xfile:
    if line.startswith('mundo'):
        print(line)
xfile.close()

xfile=open('text.txt')
for line in xfile:
    line = line.rstrip()
    if not line.startswith('mundo'):
        continue
    print(line)
xfile.close()