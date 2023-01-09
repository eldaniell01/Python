import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        total = 0
        for row in reader:
            dic = list(row)
            total = total + int(dic[1])
        return total
if __name__ == '__main__':
    response = read_csv('comprehensions, funciones y manejo de errores/ejercicio 26/world_population.csv')
    print(response) 