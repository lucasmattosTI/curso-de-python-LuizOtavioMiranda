# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host= 'localhost'): # -> método de instância que inicializa os valores da instância, tem o 'self'
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): # -> método 'set_...' usado para setar (configurar um valor) um atributo na instância
        self.user = user

    def set_passward(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection= cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)

usuario1 = Connection()
usuario1.set_user('Admin')
usuario1.set_passward('12345678')
print(f'Endereço: {usuario1.host}\nUsuário: {usuario1.user}\nPassword: {usuario1.password}')

c2 = Connection.create_with_auth('Lucas','1234')
print(c2.user, c2.password)
Connection.log('usuário não encontrado!')