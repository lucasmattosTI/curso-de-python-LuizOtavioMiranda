# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def set_user_admin(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('Log: ', msg)

    
# c1 = Connection()
c1 = Connection.set_user_admin('Admin', 'admin')
# c1.set_user('lucasmattos')
# c1.set_password('1234')
print(c1.user, c1.password)
Connection.log('Mensagem de log')