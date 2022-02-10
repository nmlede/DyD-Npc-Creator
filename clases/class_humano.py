from clases.class_npc import Npc


class Humano(Npc):

    altura_base_masculino = 4.10 
    altura_base_femenino = 4.5 

    def __init__(self, nombre, sexo):
        self.nombre = nombre
        self.sexo = sexo
        self.fuerza = self.set_stats(6,4)
        self.destreza = self.set_stats(6,4)
        self.constitucion = self.set_stats(6,4)
        self.inteligencia = self.set_stats(6,4)
        self.sabiduria = self.set_stats(6,4)
        self.carisma = self.set_stats(6,4)


        
    

    
