class Preferencias():
    def __init__ (self, cant_filas=5, cant_columnas=5, especiales={}, nivel='', categorias=[], IA={}):
        self._filas = cant_filas
        self._columnas = cant_columnas
        self._especiales = especiales
        self._nivel = nivel
        self._categorias_personalizadas = categorias
        self._IA = IA

    def getFilas(self):
        return self._filas

    def getColumnas(self):
        return self._columnas

    def getEspeciales(self):
        return self._especiales

    def getNivel(self):
        return self._nivel
    
    def getCategoriasPersonalizadas(self):
        return self._categorias_personalizadas

    def getIA(self):
        return self._IA

    def setIA(self, IA):
        self._IA = IA
    
    def setCategoriasPersonalizadas(self, categorias):
        self._categorias_personalizadas = categorias

    def setNivel(self, nivel):
        self._nivel = nivel

    def setFilas(self, filas):
        self._filas = filas

    def setColumnas(self, columnas):
        self._columnas = columnas

    def setEspeciales(self, especiales):
        self._especiales = especiales
