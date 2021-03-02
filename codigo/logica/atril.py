from codigo.logica.configuracion import*
from codigo.logica.bolsa_fichas import*
import random

class Atril():
    '''
        Recibe la bolsa de fichas y la cantidad de fichas
        que se deben repartir en la partida.
        Sus métodos son devolver una ficha determinando su posición,
        cambiar todas las fichas del atril si es que hay fichas en la bolsa
        mostrar el atril íntegro
        devolver la cantidad de fichas disponibles
    '''
    def __init__ (self, bolsa_fichas, cant_fichas):
        '''
        El atributo cant_maxima es recibido al crearse el atril, de esta forma se lo puede utilizar en cualquier
        otra aplicación que utilice atriles
        '''
        random.shuffle(bolsa_fichas)
        self._cant_maxima = cant_fichas
        self._cant_Fichas = cant_fichas
        self._lista_Fichas = []
        for i in range(cant_fichas):
            self._lista_Fichas.append(bolsa_fichas[0])
            bolsa_fichas.remove(bolsa_fichas[0])

    def get_ficha(self, pos):
        return self._lista_Fichas[pos]

    def cambiar_fichas (self, bolsa_fichas):
        '''
        Utiliza la cantidad de fichas configuradas para este juego como control.
        '''
        for i in range(self._cant_Fichas):
            bolsa_fichas.append(self._lista_Fichas[i])
        self._cant_Fichas = 0
        self._lista_Fichas = []
        #Vuelve a mezclar la bolsa para evitar que se entreguen las mismas fichas recién descartadas
        random.shuffle(bolsa_fichas)
        while bolsa_fichas and self._cant_Fichas < self._cant_maxima:
            self._lista_Fichas.append(bolsa_fichas[0])
            bolsa_fichas.remove(bolsa_fichas[0])
            self._cant_Fichas += 1

    def usar_ficha (self,pos):
        self._lista_Fichas.pop(pos)
        self._cant_Fichas = self._cant_Fichas - 1

    def llenar_atril (self, bolsa_fichas):
        total = self._cant_maxima - self._cant_Fichas
        for i in range(total):
            if len(bolsa_fichas)>0:
                self._lista_Fichas.append(bolsa_fichas[0])
                self._cant_Fichas += 1
                bolsa_fichas.remove(bolsa_fichas[0])
            else:
                break

    def ver_atril(self):
        return self._lista_Fichas

    def get_cant_fichas(self):
        return self._cant_Fichas

    def getCantMaxima(self):
        return self._cant_maxima
