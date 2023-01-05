import copy

items = [
    {
        'produc': 'playera',
        'price': 20
    },
    {
        'produc': 'pantalon',
        'price': 40
    },
    {
        'produc': 'calcetin',
        'price': 10  
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

productos = list(map(lambda item: item['produc'], items))
print(productos)

def add(item):
    ite = item.copy()
    ite['taxes'] = ite['price'] *0.19
    return ite
    
itemsss = list(map(add, items))
print(itemsss)
print(items)


