import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data =[]
        print(header)
        for row in reader:
            dic = list(zip(header, row))
            country = {key: value for key, value in dic}
            data.append(country)
            
        return data 
            

if __name__=='__main__':
    data = read_csv("comprehensions, funciones y manejo de errores/proyecto/world_population.csv")
    print(data[0])