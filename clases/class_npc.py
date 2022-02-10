import herramientas.utils as ut

class Npc():
    nombre = ''
    fuerza = 0
    destreza = 0
    constitucion = 0
    inteligencia = 0
    sabiduria = 0
    carisma = 0
    altura = 0

    def __init__(self, nombre, sexo):
        self.nombre = nombre
        self.sexo = sexo
        self.fuerza = self.set_stats(6,4)
        self.destreza = self.set_stats(6,4)
        self.constitucion = self.set_stats(6,4)
        self.inteligencia = self.set_stats(6,4)
        self.sabiduria = self.set_stats(6,4)
        self.carisma = self.set_stats(6,4)


    def set_stats(self, caras, tiradas):
        resultados = 0
        dados = [tiradas-1]
        
        try:
            for i in range(tiradas-1):
                resultados = ut.tirar_dados(caras)
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
        except Exception as e:
            print(f'Error al setear atributos. {e}')

    # def set_altura(self, sexo, altura, caras):
    #     if self.sexo == 'Masculino':
    #         altura = self.peso = altura + ut.tirar_dados(caras)*2
    #         return altura
    #     if self.sexo == 'Femenino':
    #         altura = self.peso = altura + ut.tirar_dados(caras)*2
    #         return altura


    def show_nombre(self):
        print(f'{self.nombre}')

    def show_sexo(self):
        print(f'{self.sexo}')

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

    # def show_altura(self):
    #     pass
    
    def show_all_stats(self):
        self.show_nombre()
        self.show_sexo()
        self.show_fuerza()
        self.show_destreza()
        self.show_constitucion()
        self.show_inteligencia()
        self.show_sabiduria()
        self.show_carisma()
        # self.show_altura()