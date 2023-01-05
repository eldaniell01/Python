def people():
    keys=['col', 'bol']
    values = [300, 5000]
    return keys, values

def calculate(data, country):
    result = list(filter(lambda item: item['country']== country, data))
    return result