people = [
    {
        'name': 'daniel',
        'age': 25
    },
    {
        'name': 'kevin',
        'age': 25
    },
    {
        'name': 'marielos',
        'age': 17
    },
    {
        'name': 'angela',
        'age': 16
    },
    {
        'name': 'yesenia',
        'age': 26
    }
]

people = list(filter(lambda x: x['name'] == 'yesenia'  , people))

print(dict(people))