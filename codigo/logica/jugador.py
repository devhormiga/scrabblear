class Jugador():

    def __init__(self, nombre, puntaje = 0, dificultad ='facil', avatar = None):
        self.__nombre = nombre
        self.__puntuacion = puntaje
        self.__dificultad = dificultad
        self.__avatar = avatar


    def __str__(self):
        return f"{self.__nombre} - {self.__puntuacion} - {self.__dificultad}"
    def infoJugador(self):
        return f"{self.__nombre}   -   {self.__puntuacion}   -   {self.__dificultad}"

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getPuntaje(self):
        return self.__puntuacion

    def setPuntaje(self, puntaje):
        self.__puntuacion = puntaje

    def getDificultad(self):
        return self.__dificultad

    def setDificultad(self, dificultad):
        self.__dificultad = dificultad

    def getAvatar(self):
        return self.__avatar
    def setAvatar(self, avatar):
        self.__avatar = avatar
