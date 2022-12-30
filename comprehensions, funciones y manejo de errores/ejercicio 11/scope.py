price = 100 # es global

def increment():
    price = 200 # es local dentro de la funcion
    price = price +10
    print(price)
    return price

print(price)
price2 = increment()
print(price2)
