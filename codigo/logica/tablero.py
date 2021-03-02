from codigo.logica.preferencias import Preferencias
from codigo.logica.configuracion import *

class Tablero ():
    def __init__(self, configuracion):
        self.__casilleros = self.__inicializarCasilleros(configuracion)

    def __inicializarCasilleros(self, configuracion):
        """Crea la matriz donde se insertarán las fichas a partir de una configuración.
        Si hay casilleros especiales, representados con un diccionario bajo
        el formato {'fila, columna': '*<accion del casillero>'}, graba '*<accion del casillero>' en la matriz,
        según las coordenadas de la clave."""
        matriz = []
        espacios_especiales = configuracion.getEspeciales()
        for f in range(0, configuracion.getFilas()):
            fila = []
            #Crea la fila, moviéndose entre columnas
            for c in range(0, configuracion.getColumnas()):
                #Si la ubicación actual está en el diccionario para espacios
                #especiales, toma el color y lo inserta en la matriz
                if (f'{f}, {c}' in espacios_especiales) or (f'{f},{c}' in espacios_especiales):
                    fila.append(espacios_especiales[f'{f}, {c}'])
                else:
                    fila.append('')
            matriz.append(fila)
        return matriz

    def getCasilleros(self):
        """Devuelve la matriz que representa el tablero"""
        return self.__casilleros

    def setCasilleros(self, casilleros):
        """Recibe una matriz y la asigna como tablero"""
        self.__casilleros = casilleros

    def _calcularPuntaje(self, puntaje, especiales):
        if '*0' in especiales:
            return 0
        else:
            for especial in especiales:
                if especial == '*sum':
                    puntaje = puntaje + 5
                elif especial == '*mult':
                    puntaje = puntaje * 2
                elif especial == '*rest':
                    puntaje = puntaje - 5
                elif especial == '*div':
                    puntaje = puntaje // 2
            if puntaje < 0:
                return 0
        return puntaje

    def insertarPalabra(self, fichas, posicion, sentido):
        """Recibe una lista de fichas en formato diccionario,
        una posicion en formato tupla (fila, columna) y un sentido en formato string
        ("h" o "v"). Luego, si hubiese lugar, inserta la palabra en el tablero
        siguiendo esas indicaciones.
        Además, retorna el puntaje para esa inserción."""
        casilleros = self.getCasilleros()
        #Fila
        f = posicion[0]
        #Columna
        c = posicion[1]
        puntaje = 0
        especiales = []
        indice_fichas = 0
        if (sentido == 'h'):
            while (c < len(casilleros[posicion[0]])) and (c < (posicion[1] + len(fichas))):
                if (self.esFicha(f, c)):
                    break
                puntaje += list(fichas[indice_fichas].values())[0]
                if (self.getCasilleros()[f][c] != ''):
                    especiales.append(self.getCasilleros()[f][c])
                indice_fichas += 1
                c += 1
            if (len(fichas) == c - posicion[1]):
                c = posicion[1]
                for fic in fichas:
                    casilleros[posicion[0]][c] = fic
                    c += 1
                self.setCasilleros(casilleros)
                puntaje = self._calcularPuntaje(puntaje, especiales)
            else:
                puntaje = -1
        else:
            while (f < len(casilleros)) and (f < posicion[0] + len(fichas)):
                if (self.esFicha(f, c)):
                    break
                puntaje += list(fichas[indice_fichas].values())[0]
                if (self.getCasilleros()[f][c] != ''):
                    especiales.append(self.getCasilleros()[f][c])
                indice_fichas += 1
                f += 1
            if (len(fichas) == f - posicion[0]):
                f = posicion[0]
                for fic in fichas:
                    casilleros[f][posicion[1]] = fic
                    f += 1
                self.setCasilleros(casilleros)
                puntaje = self._calcularPuntaje(puntaje, especiales)
            else:
                puntaje = -1
        return puntaje

    def esFicha(self, f=-1, c=-1, ficha=None):
        """Determina si un objeto es o no una ficha, y retorna True o False
        dependiendo de ello.
        Si recibe fila y columna, evalúa lo que hay en esa posición.
        Si recibe una ficha, ignora las coordenadas y evalúa esa ficha en
        particular."""
        if (ficha == None):
            return isinstance(self.getCasilleros()[f][c], dict)
        else:
            return isinstance(ficha, dict)

    def imprimirCasilleros(self):
        """Imprime la matriz en formato string.
        Tiene propositos de testeo."""
        casilleros = self.getCasilleros()
        for fila in casilleros:
            for dato in fila:
                if (self.esFicha(ficha=dato)):
                    print(list(dato.keys())[0], end='   ')
                else:
                    if (dato == ''):
                        print('-', end='   ')
                    else:
                        print(dato[0:2].upper(), end='  ')
            print()

    def buscarEspacio(self, fichas, preferencias):
        '''Recibe una lista de fichas y localiza una coordenada en la que quepa
        la palabra. Si existiese más de un espacio disponible, evalúa cada camino
        y selecciona el que aporte el máximo interés (mayor puntaje).
        Retorna un diccionario que contiene la coordenada y el sentido en el que
        debería ser insertada, además del interés que generó.
        Si no se encontró ningún espacio, devuelve "-1" como coordenada.'''

        dificultad = preferencias.getNivel()
        tablero = self.getCasilleros()
        longitud_palabra = len(fichas)
        cant_columnas = len(tablero[0])
        cant_filas = len(tablero)
        puntaje_bruto = sum([list(punto.values())[0] for punto in fichas])
        espacio_optimo = {'coordenada': -1, 'interes': -1, 'sentido': ''}

        for f in range(0, cant_filas):
            for c in range (0, cant_columnas):
                fila = f
                for sentido in ['h', 'v']:
                    camino = []
                    columna = c
                    longitud_palabra = len(fichas)
                    encontro_obstaculo = False
                    #Mientras no se haya recorrido la longitud de la palabra...
                    while (longitud_palabra != 0) and not (encontro_obstaculo):
                        #Si en la ubicación actual hay una ficha, se detiene la búsqueda
                        if (self.esFicha(fila, columna)):
                            encontro_obstaculo = True
                        else:
                            #Si no, reduce en 1 la cantidad de letras restantes
                            longitud_palabra = longitud_palabra - 1
                            #Si se está parado en un casillero especial, agrega su efecto a una lista
                            if (tablero[fila][columna] != ''):
                                camino.append(tablero[fila][columna])
                            #Indica en qué sentido debe continuar el recorrido
                            if (sentido == 'h'):
                                columna = columna + 1
                                #Al alcanzar el límite del tablero, la búsqueda finaliza
                                if (columna == cant_columnas):
                                    encontro_obstaculo = True
                            else:
                                fila = fila + 1
                                if (fila == cant_filas):
                                    encontro_obstaculo = True               
                    if (longitud_palabra == 0):
                        puntaje_final = self._calcularPuntaje(puntaje_bruto, camino)
                        if (puntaje_final > espacio_optimo['interes']):
                            espacio_optimo['interes'] = puntaje_final
                            espacio_optimo['coordenada'] = (f, c)
                            espacio_optimo['sentido'] = sentido
                if (espacio_optimo['interes'] != -1):
                    if (dificultad == 'facil') or ((dificultad == 'personalizado') and not (preferencias.getIA()['espacio_inteligente'])):
                        return espacio_optimo
        return espacio_optimo