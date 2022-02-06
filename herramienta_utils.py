from random import randint

def dados(caras, tiradas):
    resultado = 0 
    print(f'Tirada de {tiradas} dado/s de {caras} caras')
    for index in range(0, tiradas):
        dado = randint(0, caras)
        print(dado)
        resultado = resultado + dado

    if resultado < 10:
        dados(caras, tiradas)
    else:    
        return resultado
    

'''def set_stats():
    resultado = dados(6, 5)
    

    return resultado
'''
    


