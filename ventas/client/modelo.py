import uuid

class Model_cliente:
    def __init__(self, name, trabajo, email, idx=None):
        self.name = name
        self.trabajo = trabajo
        self.email = email
        self.idx = idx or uuid.uuid4()
    
    
    def to_dict(self):
        return vars(self)
    
    
    @staticmethod
    def schema():
        return['name', 'trabajo', 'email', 'idx']