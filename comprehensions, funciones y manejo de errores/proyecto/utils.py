def people(data):
    dic ={
        '2022': float(data['2022 Population']),
        '2020': float(data['2020 Population']),
        '2015': float(data['2015 Population']),
        '2010': float(data['2010 Population']),
        '2000': float(data['2000 Population']),
        '1990': float(data['1990 Population']),
        '1980': float(data['1980 Population']),
        '1970': float(data['1970 Population']),
    }
    return dic.keys(), dic.values()

def calculate(data, country):
    result = list(filter(lambda item: item['Country/Territory']== country, data))
    return result