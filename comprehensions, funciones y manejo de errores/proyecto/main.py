import utils
import readcsv
import grafica

def run():
    data = readcsv.read_csv('comprehensions, funciones y manejo de errores/proyecto/world_population.csv')
    inpt = input('ingrese el país: ')
    result = utils.calculate(data, inpt)
    if len(result)>0:
        country = result[0]
        key, values = utils.people(country)
        grafica.graficaBarra(key, values)


    
if __name__ == '__main__':
    run()