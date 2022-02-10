from clases.class_npc import Npc


class Mediano(Npc):

    def __init__(self, nombre, sexo):
        self.nombre = nombre
        self.sexo = sexo
        self.fuerza = self.set_stats(6,4) - 2
        self.destreza = self.set_stats(6,4) + 2
        self.constitucion = self.set_stats(6,4) 
        self.inteligencia = self.set_stats(6,4)
        self.sabiduria = self.set_stats(6,4)
        self.carisma = self.set_stats(6,4)