import sys
print(sys.path)

import re
text = 'mi numero de telefono es 212323333, el codigo de pais es 122, mi numero de la suerte es 3'

result = re.findall('[0-9]+', text)

print(result)

import time

tim = time.time()
print(tim)
local = time.localtime()
result = time.asctime(local)

print(result)

import collections
number = [1,2,3,4,1,2,3,4,5]
count = collections.Counter(number)
print(count)