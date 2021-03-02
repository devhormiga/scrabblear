import pickle
import os
from codigo.logica.jugador import*

class Puntuacion_Maxima():
    ruta_guardado = os.path.join("guardados", "puntuacion_maxima.pckl")
    MAXIMOS = 10

    def __init__ (self):
        '''
        Crea una lista vacía de puntajes y luego carga los puntajes almacenados, si los hay
        '''        
        self.puntajes = []
        self.cargar()

    def guardar(self):
        fichero = open(self.ruta_guardado, 'wb')
        pickle.dump(self.puntajes, fichero)
        fichero.close()

    def agregar(self,jug):
        '''
        Recibe un jugador y evalúa si su puntuación es mayor a las guardadas. Produce el desplazamiento y elimina a la posición 11
        '''
        self.puntajes.append(jug)
        self.puntajes.sort(key=lambda jugador: jugador.getPuntaje(),reverse=True)
        self.puntajes.pop()
        self.guardar()

    def crear(self):
        '''
        Al crear invoca a vaciar_puntajes() para setear todos en '0'
        '''        
        fichero = open (self.ruta_guardado, 'wb')
        self._vaciar_puntajes()
        fichero.close()

    def cargar(self):
        '''
        Controla si existe algún archivo 'puntuación máxima' y si no lo crea
        '''
        try:
            fichero = open(self.ruta_guardado, 'rb')
            self.puntajes = pickle.load(fichero)
            fichero.close()
        except:
            self.crear()

    def ver_puntaje(self,pos):
        '''
        Devuelve una posición particular a partir de una posición específica
        '''
        return self.puntajes[pos]

    def _vaciar_puntajes (self):
        '''
            Es un método que solo se invoca desde la propia clase.
            Vacía la lista de puntuaciones
        '''
        self.puntajes = []
        for p in range (10):
            self.puntajes.append(Jugador('Vacío',0, ''))
        self.puntajes = self.puntajes[0:self.MAXIMOS]
        self.guardar()

