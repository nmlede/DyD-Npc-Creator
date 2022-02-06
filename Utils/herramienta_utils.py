from random import randint

def dados(caras, tiradas):
    print(f'Tirada de {tiradas} dado/s de {caras} caras')
    for index in range(0, tiradas):
        dado = randint(0, caras)
        print(dado)


