
password='123'

def pass_requiere(func):
    def wrapper():
        password2 = input('contraseña: ')
        if password2 == password:
            return func()
        else:
            print('contraseña incorrecta')
    return wrapper
@pass_requiere
def password1():
    print('la contraseña es correcta')

def nombre (name):
    print ('hola, {}'.format(name))
    
    
if __name__== '__main__':
    
    password1()