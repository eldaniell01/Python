import utils
import readcsv
import grafica

def run():
    data = readcsv.read_csv('comprehensions, funciones y manejo de errores/proyecto/world_population.csv')
    data = list(filter(lambda item: item['Continent'] =='North America', data ))
    paises = list(map(lambda x: x['CCA3'], data))
    porcentajes = list(map(lambda x: x['World Population Percentage'], data))
    grafica.graficaCircular(paises, porcentajes)
    
    
    """inpt = input('ingrese el país: ')
    result = utils.calculate(data, inpt)
    if len(result)>0:
        country = result[0]
        key, values = utils.people(country)
        grafica.graficaBarra(key, values)"""


    
if __name__ == '__main__':
    run()