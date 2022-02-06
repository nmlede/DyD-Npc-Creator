from ..Utils import herramienta_utils as hu

class Npc():
    nombre = ''
    fuerza = 0
    destreza = 0
    constitucion = 0
    inteligencia = 0
    sabiduria = 0
    carisma = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.fuerza = hu.dados(6,1)
        self.destreza = hu.dados(6,1)
        self.constitucion = hu.dados(6,1)
        self.inteligencia = hu.dados(6,1)
        self.sabiduria = hu.dados(6,1)
        self.carisma = hu.dados(6,1)

    def show_stats(self):
        print(f'Nombre = {self.nombre}')
        print(f'Fuerza = {self.fuerza}')
        print(f'Destreza = {self.destreza}')
        print(f'Constitucion = {self.constitucion}')
        print(f'Inteligencia = {self.inteligencia}')
        print(f'Sabiduria = {self.sabiduria}')
        print(f'Carisma = {self.carisma}')
