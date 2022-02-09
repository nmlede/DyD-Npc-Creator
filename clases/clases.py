import herramientas.herramienta_utils as hu

class Npc():
    nombre = ''
    raza = ''
    fuerza = 0
    destreza = 0
    constitucion = 0
    inteligencia = 0
    sabiduria = 0
    carisma = 0

    peso_minimo = 0
    peso_medio = 0
    peso_maximo = 0

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        self.fuerza = self.set_stats(6,5)
        self.destreza = self.set_stats(6,5)
        self.constitucion = self.set_stats(6,5)
        self.inteligencia = self.set_stats(6,5)
        self.sabiduria = self.set_stats(6,5)
        self.carisma = self.set_stats(6,5)


    def set_stats(self, caras, tiradas):
        resultados = 0
        dados = []
        
        for i in range(tiradas):
            resultados = hu.tirar_dados(caras)
            dados.append(resultados)
        menor = dados[0]
        
        for valor in dados:
            if valor < menor:
                menor = valor  
        
        dados.pop(menor) 
        resultados = 0
        
        for i in range(len(dados)):
            resultados += dados[i]

        return resultados

    def show_nombre_raza(self):
        print(f'{self.nombre}, {self.raza}')

    def show_fuerza(self):
        print(f'Fuerza = {self.fuerza}')

    def show_destreza(self):
        print(f'Destreza = {self.destreza}')

    def show_constitucion(self):
        print(f'Constitucion = {self.constitucion}')

    def show_inteligencia(self):
        print(f'Inteligencia = {self.inteligencia}')

    def show_sabiduria(self):
        print(f'Sabiduria = {self.sabiduria}')

    def show_carisma(self):
        print(f'Carisma = {self.carisma}')

    
    def show_all_stats(self):
        self.show_nombre_raza()
        self.show_fuerza()
        self.show_destreza()
        self.show_constitucion()
        self.show_inteligencia()
        self.show_sabiduria()
        self.show_carisma()

    def set_peso(self):
        pass

    def show_peso(self):
        pass