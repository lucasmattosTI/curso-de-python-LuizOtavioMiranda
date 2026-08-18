# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar')
            return
        print(f'{self.nome} está fotografando...')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando!')
            return
        print(f'{self.nome} está parando de filmar.')
        self.filmando = False

c1 = Camera('Cannon')
c2 = Camera('Sony')
print(c2.nome)
print(c2.filmando)

c2.filmar()
print(c2.filmando)
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()
