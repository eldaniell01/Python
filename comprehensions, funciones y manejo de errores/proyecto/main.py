import utils

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


def run():
    result = utils.people()

    print(result)



    inpt = input('ingrese el país: ')

    result = utils.calculate(data, inpt.lower())

    print(result)
    
if __name__ == '__main__':
    run()