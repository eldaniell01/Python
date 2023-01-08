try:
    print(0/0)
    assert 1!=1, 'no es igual a uno'
    age = 10
    if age <18:
        raise Exception('no se permiten menores')
except Exception as e:
    print(e)

print('hola')