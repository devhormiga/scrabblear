from codigo.logica.configuracion import *

def crear_bolsa(cant, puntos, propietario='jugador'):
    '''
    Esta funcion returna una bolsa de fichas (una lista, donde cada ficha
    es un diccionario' donde la clave es la letra y el valor su puntaje)
    recibe la cantidad y los puntos segun el nivel, el nivel no se determina en este modulo
    '''
    bolsa = []

    #l = cantidad de veces que aparece una ficha
    #k = puntaje de una ficha
    for l in cant:
        ok = False
        k = 1
        while not ok:
            if k in puntos:
                if l in puntos[k]:
                    #Arma la ficha
                    puntaje = k
                    ok = True
                else:
                    k += 1
            else:
                k += 1
        #Agrega la cantidad de veces especificada según la dificultad a la bolsa
        for f in range(cant[l.upper()]):
            #La ficha posee un puntaje y un indicador de a quién pertenece
            bolsa.append({l.lower(): puntaje, 'propietario': propietario})
    return bolsa


if __name__ == '__main__' :
    nivel = nivel_facil()
    bolsa= crear_bolsa(nivel['cant_fichas'],nivel['puntaje_ficha'])
    n=nivel['nivel']
    print(f'bolsa ocnfiurada en nivel: {n}')
    print(f'la bolsa contiene: {len(bolsa)} fichas.\n El contenid oes el siguiente:')
    print(bolsa)
