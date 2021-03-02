import pickle
from codigo.logica.tablero import*
from codigo.logica.configuracion import*

class Juego_Guardado:
    '''
    Recibe tablero los datos del usuario, los atriles de juego, bolsa de ficha, ambos puntajes, tiempo restante,
    configuración de la partida, palabras utilizadas por ambos jugadores y los almacena en un archivo .pckl
    Permite múltiples usuarios.
    '''
    juego = []
    def __init__(self, ruta_guardado, tablero=None, jugador_user=None, atril=None, atril_pc=None, b_fichas=None,
                puntaje=None, puntaje_pc=None, tiempo_restante=None, pref=None, cant_cambiar=None, avatar=None,
                palabras_jugador=None, palabras_pc=None, dificultad=None, pc_puede_cambiar=None):
        self.tablero = tablero
        self.jugador_user = jugador_user
        self.atril = atril
        self.bolsa_fichas = b_fichas
        self.atril_pc = atril_pc
        self.puntaje = puntaje
        self.tiempo_restante = tiempo_restante
        self.preferencias = pref
        self.cant_cambiar = cant_cambiar
        self.puntaje_pc = puntaje_pc
        self.ruta_guardado = ruta_guardado
        self.avatar = avatar
        self.palabras_jugador = palabras_jugador
        self.palabras_pc = palabras_pc
        self.dificultad = dificultad
        self.pc_puede_cambiar = pc_puede_cambiar

    def getTablero (self):
        return self.tablero
    def getJugadorUser (self):
        return self.jugador_user
    def getAtril (self):
        return self.atril
    def getBolsaFichas (self):
        return self.bolsa_fichas
    def getPuntaje (self):
        return self.puntaje
    def getTiempoRestante(self):
        return self.tiempo_restante
    def getPreferencias(self):
        return self.preferencias
    def getCantCambiar(self):
        return self.cant_cambiar
    def getPuntajePC(self):
        return self.puntaje_pc
    def getRutaGuardado(self):
        return self.ruta_guardado
    def getAtrilPC(self):
        return self.atril_pc
    def getAvatar(self):
        return self.avatar
    def getPalabrasJugador(self):
        return self.palabras_jugador
    def getPalabrasPC(self):
        return self.palabras_pc
    def getDificultad(self):
        return self.dificultad
    def getCambiosPC(self):
        return self.pc_puede_cambiar

    def crear_guardado(self):
        '''
        Cada vez que se lo invoca sobreescribe el archivo. Guarda una única partida con el nombre del usuario
        '''
        fichero = open(f'{self.getRutaGuardado()}', 'wb')
        self.juego = [self.tablero, self.jugador_user, self.atril, self.bolsa_fichas, self.puntaje,
                    self.tiempo_restante, self.preferencias, self.cant_cambiar, self.puntaje_pc, self.atril_pc,
                    self.avatar, self.palabras_jugador, self.palabras_pc, self.dificultad, self.pc_puede_cambiar]
        pickle.dump(self.juego, fichero)
        fichero.close()

    def cargar_guardado(self):
        try:
            fichero = open(f'{self.getRutaGuardado()}', 'rb')
            self.juego = pickle.load (fichero)
            fichero.close()
            self.tablero = self.juego[0]
            self.jugador_user = self.juego[1]
            self.atril = self.juego[2]
            self.bolsa_fichas = self.juego[3]
            self.puntaje = self.juego[4]
            self.tiempo_restante = self.juego[5]
            self.preferencias = self.juego[6]
            self.cant_cambiar = self.juego[7]
            self.puntaje_pc = self.juego[8]
            self.atril_pc = self.juego[9]
            self.avatar = self.juego[10]
            self.palabras_jugador = self.juego[11]
            self.palabras_pc = self.juego[12]
            self.dificultad = self.juego[13]
            self.pc_puede_cambiar = self.juego[14]
            return True
        except:
            print ('No hay partidas guardadas')
            return False
