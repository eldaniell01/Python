name = "Daniel"
last_name= "Montepeque"
age = 25

print(name)
print(last_name)

full_name = name +" "+last_name
print(full_name)

quote = "2'hola'"
print(quote)

quote2 = 'ella dijo "xd"'

print(quote2)

"""
    formato
"""

template = "hola mi nombre es "+name+ " y mi apellido es "+ last_name
print(template)

template = "hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

templete = f"hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

template = f"hola, mi nombre es {name} y mi apellido es {last_name} y tengo {age} años"
print(template)