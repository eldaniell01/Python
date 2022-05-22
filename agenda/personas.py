class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def hello(self):
        print('hola mi nombre es {}, mi apelllido es {} y mi edad es {}'.format(self.nombre, self.apellido, self.edad))
        

if __name__=='__main__':
    persona = Persona('Daniel', 'Montepeque', 24)
    
    print('edad: {}'.format(persona.edad))
    persona.hello()