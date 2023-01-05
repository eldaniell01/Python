import utils

result = utils.people()

print(result)

data = [
    {
        'country': 'guatemala',
        'people': 4000
    },
    {
        'country': 'mexico',
        'people': 8000
    },
    {
        'country': 'españa',
        'people': 6000
    },
    {
        'country': 'el salvador',
        'people': 3000
    },
]

inpt = input('ingrese el país: ')

result = utils.calculate(data, inpt.lower())

print(result)