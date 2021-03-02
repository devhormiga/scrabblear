import PySimpleGUI as sg
import time
import os
import platform
from codigo.interfaz import menuPausa
from codigo.interfaz.tema import aviso

class Dibujar():
    '''Clase que construye y actualiza una interfaz gráfica
    de juego a partir de los datos de una partida determinada.'''

    def __init__ (self, tablero, preferencias, atril, jugador):
        '''Inicializa y construye diferentes espacios de la GUI. Además,
        está preparada para recibir un tablero o atril que ya contenía fichas,
        o cualquier otra información que provenga de una sesión ya creada.
        Al finalizar, muestra la ventana en pantalla.
        :param tablero: Objeto que contiene la cantidad de filas y
        columnas, los espacios con casilleros especiales y las fichas insertadas.
        :param preferencias: Objeto que protege información relativa a la dificultad.
        :param atril: Objeto con datos sobre las fichas del atril y la cantidad máxima
        de espacios que posee.
        :param jugador: Objeto que guarda el nombre del jugador, su puntaje y su avatar.'''

        self.tema_tablero()
        self._jugador = jugador
        #Algunos valores por defecto para construir la interfaz del tablero
        self._tamcas = (37, 39)
        self._padin = (0, 0)
        self._botoncolor = ('white','#ece6eb')
        self._ficha_tamano = (39,41)
        #Inicialización de los límites de tiempo
        self._tiempo_inicio = 0
        self._tiempo_fin = 0
        #Directorios con las imágenes necesarias
        self._directorio_media = os.path.join('media','media_ii', '')
        self._directorio_fichas = os.path.join('media', 'Fichas y espacios', '')
        self._directorio_avatars =  os.path.join('media', 'media_ii','avatars','')
        #Prepara y agrega a la columna izquierda de la interfaz todos los casilleros del tablero
        columna_izquierda = []
        #Filas
        f = 0
        #Columnas
        c = 0
        for fila in tablero.getCasilleros():
            insercion = []
            for dato in fila:
                if (tablero.esFicha(ficha=dato)):
                    if (dato['propietario'] == 'jugador'):
                        insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}ficha {list(dato.keys())[0]}.png', pad=self._padin, key=f'tablero {f},{c}', image_size=self._tamcas,button_color=(None, '#06FF64'), enable_events=True))
                    else:
                        insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}ficha {list(dato.keys())[0]}.png', pad=self._padin, key=f'tablero {f},{c}', image_size=self._tamcas,button_color=(None, '#FF0606'), enable_events=True))
                else:
                    if (dato==''):
                        insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}azul.png', pad=self._padin, key=f'tablero {f},{c}', image_size=self._tamcas, button_color=self._botoncolor,enable_events=True))
                    else:
                        insercion.append(sg.Button(image_filename=f'{self._directorio_fichas}{dato[1:]}.png', pad=self._padin, key=f'tablero {f},{c}', image_size=self._tamcas,button_color=self._botoncolor ,enable_events=True))
                c += 1
            f += 1
            c = 0
            columna_izquierda.append(insercion)

        fichas = []
        for i in range(0, atril.get_cant_fichas()):
            letra = list(atril.get_ficha(i).keys())[0]
            punto = atril.get_ficha(i)[letra]
            fichas.append(sg.Button(image_filename=f'{self._directorio_fichas}ficha {letra}.png', key=f'ficha {str(i)}', pad=(0, None), image_size=self._ficha_tamano, button_color=('white','#4f280a'),tooltip= f'{punto} puntos'))

        temporizador = [[sg.Text('Jugado:', size=(10, 1), font=('Impact', 14), justification='center', text_color='white'), sg.Text('00:00', size=(7, 1), font=('Impact', 20), justification='center', text_color='white',
                        key='timer', background_color='black'), sg.VerticalSeparator(), sg.Text('00:00', size=(7, 1), font=('Impact', 20), justification='center', text_color='white', key='tiempo_total', background_color='black')],
                        [sg.Text('Restante:', size=(10, 1), font=('Impact', 14), justification='center', text_color='white'),sg.ProgressBar(max_value=0, orientation='horizontal', size=(20, 25), key='progreso'),]]

        tiempo = [[sg.Frame(layout= temporizador, title='Tiempo de Juego', title_color='#ece6eb', relief=sg.RELIEF_SUNKEN, font=('Italic', 14), element_justification='center', key='contTiempo')]]

        top = [[sg.Image(f'{self._directorio_media}scrabbleArLogo.png'),
              sg.Column(tiempo),
               sg.Button(image_filename=f'{self._directorio_media}pausa.png',button_color=('black','#4f280a'), pad=self._padin, border_width=0,
                          key='pausar'),
               sg.Button(image_filename=f'{self._directorio_media}AYUDA.png', button_color=('black', '#4f280a'),
                         pad=self._padin, border_width=0, tooltip='Obtenga ayuda clickeando aquí',
                         key='ayuda'),
                sg.Button(image_filename=f'{self._directorio_media}fullscreen.png', font=('Arial', 14), border_width=0, tooltip='Cambiar a pantalla completa',key='pantallaCompleta')
               ]]

        #Contenedores para los avatares, el nombre y el puntaje
        avatarJ = [[sg.Image(filename=self._jugador.getAvatar(), size=(200, 200), background_color='#4f280a', key='avatar_j')],
                  [sg.Text(text=self._jugador.getNombre(), border_width=2, justification='center', font=('Arial', 20), key='nombre_jugador')],
                  [sg.Text(text=f'  {self._jugador.getPuntaje()}  ', border_width=2, justification='center', font=('Arial', 20), key='puntaje')], ]

        #(Implementar un random para el avatar de la pc, por ahora se le selecciona uno explicitamente)
        avatarPC = [[sg.Image(filename=f'{self._directorio_avatars}avatar1.png', size=(200, 200), background_color='#4f280a', key='avatar_pc')],
                  [sg.Text(text='PC', border_width=2, justification='center', font=('Arial', 20), key='nombre_pc')],
                  [sg.Text(text='  0  ', border_width=2, justification='center', font=('Arial', 20), key='puntaje_pc')]]

        columna_derecha = [[sg.Button(button_text=f'Nivel: {preferencias.getNivel().capitalize()}', font=('Arial', 14),border_width=1,tooltip='Configuración de la partida',key='infoPartida')],
                            [sg.Column(avatarJ, element_justification='center'),sg.Column(avatarPC, element_justification='center')],
                            [sg.Text(f'                 ¡Comencemos el juego!                  ', background_color='black', font=('Arial', 14), text_color='White', key='textoPC')],
                            [sg.Text('                ---TUS FICHAS---              ', font=('Arial', 14), background_color='Black', text_color='White', key='textoJugador')],
                            fichas,
                            [sg.Text('_'*30)],
                            [sg.Button(image_filename=f'{self._directorio_media}validar.png', border_width=0, key='validar'),
                            sg.Button(image_filename=f'{self._directorio_media}bolsallenaP.png', border_width=0, key='cambiar'),
                            sg.Button(image_filename=f'{self._directorio_media}deshacer.png', border_width=0,disabled=True, key='deshacer'),]]
        #Crea la ventana y la muestra
        diseño = [[sg.Column(top, justification='center')],[sg.Column(columna_izquierda,background_color='#ece6eb',justification='left'), sg.Column(columna_derecha, element_justification='center',justification='center',size=(450,600), pad=(10, 0))]]
        self._interfaz = sg.Window('ScrabbleAR', diseño, resizable=(True if platform.system() == 'Linux' else False), no_titlebar=False)
        self._pantallaCompleta = False
        self._interfaz.Finalize()
        #Llamada a tkinter para contorlar el evento sobre el boton X
        self._interfaz.TKroot.protocol("WM_DELETE_WINDOW", self.click_X)

    def tema_tablero(self):
        '''Define un tema para la interfaz de PySimpleGUI y lo actualiza.'''
        sg.LOOK_AND_FEEL_TABLE['Tablero'] = {'BACKGROUND': '#4f280a',  ##133d51',
                                              'TEXT': '#fff4c9',
                                              'INPUT': '#c7e78b',
                                              'TEXT_INPUT': '#000000',
                                              'SCROLL': '#c7e78b',
                                              'BUTTON': ('black', '#f75404'),#4f280a
                                              'PROGRESS': ('#01826B', '#D0D0D0'),
                                              'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                              }

        sg.theme('Tablero')

    def setTimer(self, minutos):
        '''Setea la cantidad de tiempo disponible para jugar, recibida en el
        parámetro 'minutos'.
        Ejemplo: 0.5 = 30 segundos, 1 = 60 segundos, etc.'''
        #Establece el tiempo de inicio del juego
        self._setTiempoInicio(time.time())
        #Y el tiempo de finalización
        self._setTiempoFin(self._getTiempoInicio() + (minutos * 60))
        self._getInterfaz()['progreso'].UpdateBar(0, max=(self._getTiempoFin() - self._getTiempoInicio()))
        #Actualiza el tiempo total en la interfaz
        restante = self.getTiempoRestante()
        self._getInterfaz()['tiempo_total'].Update('{:02d}:{:02d}'.format(int(restante // 60), int(restante % 60)))

    def actualizarTimer(self):
        '''Actualiza el timer en la interfaz.'''
        tiempo_actual = time.time() - self._getTiempoInicio()
        self._getInterfaz()['timer'].Update('{:02d}:{:02d}'.format(int(tiempo_actual // 60), int(tiempo_actual % 60)))
        self._getInterfaz()['progreso'].UpdateBar(self._getTiempoFin()-time.time())

    def terminoTimer(self):
        '''Retorna True o False dependiendo de si el timer llegó a su tiempo límite.'''
        return time.time() > self._getTiempoFin()

    def paralizarTimer(self, instante):
        '''Recibe el instante, en segundos, a partir del cual se dejó de tener
        en cuenta el timer. Luego, cálcula el tiempo perdido desde ese momento
        hasta la llamada de la función, y lo añade al tiempo de inicio y final,
        permitiendo reestablecer el cronómetro como si no hubiera avanzado el tiempo.
        Retorna el momento siguiente a ese cálculo.
        Si el resultado se utiliza en un búcle, el timer se paraliza indefinidamente'''
        if instante < time.time():
            instante = time.time() - instante
            self._setTiempoInicio(self._getTiempoInicio() + instante)
            self._setTiempoFin(self._getTiempoFin() + instante)
            instante = time.time()
        return instante

    def getTiempoRestante(self):
        '''Devuelve el tiempo que falta para que termine la partida'''
        return self._getTiempoFin() - time.time()

    def leer(self):
        '''Retorna en formato de tupla el último evento de la interfaz, si
        lo hubiese, y su respectivo valor. Si ningún evento ocurrió, el
        programa sigue su curso con normalidad.
        Los eventos posibles son:
        "tablero f,c", donde f y c son la fila y columna donde está el botón;
        "ficha i", donde i representa el número de ficha elegido, siendo i >= 0 & i <= cant_total_fichas'''
        return self._getInterfaz().Read(timeout=0)

    def actualizarTablero(self, tablero):
        '''Analiza toda la matriz y la proyecta en la GUI. Si durante el proceso
        se topa con una ficha, busca la imagen PNG que le corresponde.'''
        #Filas
        f = 0
        #Columnas
        c = 0
        for fila in tablero.getCasilleros():
            for dato in fila:
                if (tablero.esFicha(ficha=dato)):
                    if (dato['propietario'] == 'jugador'):
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(dato.keys())[0]}.png', image_size=self._getCasilleroTamano(), button_color=(None, '#06FF64'))
                    else:
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(dato.keys())[0]}.png', image_size=self._getCasilleroTamano(), button_color=(None, '#FF0606'))
                else:
                    if (dato == ''):
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}azul.png' , image_size=self._getCasilleroTamano())
                    else:
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}{dato[1:]}.png' , image_size=self._getCasilleroTamano())
                c += 1
            c = 0
            f += 1

    def actualizarTableroCoordenada(self, tablero, coordenada, sentido, longitud_palabra, velocidad=0.2):
        '''Actualiza, a partir de una coordenada, sentido y longitud, un espacio
        específico del tablero.
        :param tablero: Matriz que contiene los datos del tablero.
        :param coordenada: Tupla de enteros con formato (x, y) que indica la coordenada.
        :param sentido: "h" para horizontal o "v" para vertical.
        :param longitud_palabra: entero que indica la cantidad de espacios a moverse por
        el tablero.
        :param velocidad: Velocidad a la que se refrescan los casilleros. A menor número,
        mayor velocidad.'''
        f = coordenada[0]
        c = coordenada[1]
        casilleros = tablero.getCasilleros()
        for largo in range(0, longitud_palabra):
            dato = casilleros[f][c]
            if (tablero.esFicha(ficha = dato)):
                if (dato['propietario'] == 'jugador'):
                        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(dato.keys())[0]}.png', image_size=self._getCasilleroTamano(), button_color=(None, '#06FF64'))
                else:
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(dato.keys())[0]}.png', image_size=self._getCasilleroTamano(), button_color=(None, '#FF0606'))
            else:
                if (dato == ''):
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}azul.png' , image_size=self._getCasilleroTamano())
                else:
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}{dato[1:]}.png' , image_size=self._getCasilleroTamano())
            if (sentido == 'h'):
                c += 1
            else:
                f += 1
            self._getInterfaz().Refresh()
            time.sleep(velocidad)


    def actualizarAtril(self, atril):
        '''Actualiza el atril en la interfaz gráfica.'''
        for f in range(0, atril.get_cant_fichas()):
            letra = list(atril.get_ficha(f).keys())[0]
            punto = atril.get_ficha(f)[letra]
            self._getInterfaz()[f'ficha {f}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {letra}.png', disabled=False, image_size=self._getFichaTamano())
            self._getInterfaz()[f'ficha {f}'].SetTooltip(f'{punto} puntos')
        if (atril.get_cant_fichas() < atril.getCantMaxima()):
            for f in range(atril.get_cant_fichas(), atril.getCantMaxima()):
                self.borrarElemento(f'ficha {f}')

    def actualizarPuntaje(self, nuevo_puntaje):
        self._getInterfaz()['puntaje'].Update(f'{nuevo_puntaje}', font=('Arial', 20))

    def actualizarPuntajePC(self, nuevo_puntaje):
        self._getInterfaz()['puntaje_pc'].Update(f'{nuevo_puntaje}', font=('Arial', 20))

    def seleccionarOrientacion(self, coordenada, pref):
        '''Una vez validada la palabra, permite mostrar los botones para
        seleccionar su orientación. La coordenada recibida por parámetro, en
        formato string "f,c", se corresponde con la fila y columna del tablero
        a partir de las cuáles se seleccionará el sentido.
        Las preferencias son necesarias para no insertar un botón de
        "sentido" fuera del límite.'''
        f = int(coordenada.split(",")[0])
        c = int(coordenada.split(",")[1])
        self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}orientacion.png', image_size=self._getCasilleroTamano())
        c_contiguo = c + 1
        if (c_contiguo < pref.getColumnas()):
            self._getInterfaz()[f'tablero {f},{c_contiguo}'].Update(image_filename=f'{self._getDirectorioFicha()}orientacionDerecha.png', image_size=self._getCasilleroTamano())
        f_inferior = f + 1
        if (f_inferior < pref.getFilas()):
            self._getInterfaz()[f'tablero {f_inferior},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}orientacionAbajo.png', image_size=self._getCasilleroTamano())

    def reestablecerOrientacion(self, coordenada, tablero, preferencias):
        '''Desvanece los botones de selección de orientación en la coordenada
        "f,c" indicada. Además, utiliza el tablero (que lo recibe como parámetro)
        para conocer lo que había en ese casillero, y las preferencias para no
        intentar reestablecer un botón de "sentido" fuera del límite.'''
        casilleros = tablero.getCasilleros()
        f = int(coordenada.split(",")[0])
        c = int(coordenada.split(",")[1])
        reestablecer = [{'f': f, 'c': c}, {'f': f, 'c': c + 1}, {'f': f + 1, 'c': c}]
        for coords in reestablecer:
            f = coords['f']
            c = coords['c']
            if (f < preferencias.getFilas()) and (c < preferencias.getColumnas()):
                if (tablero.esFicha(f=f, c=c)):
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}ficha {list(casilleros[f][c].keys())[0]}.png', image_size=self._getCasilleroTamano())
                elif (casilleros[f][c] == ''):
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}azul.png', image_size=self._getCasilleroTamano())
                else:
                    self._getInterfaz()[f'tablero {f},{c}'].Update(image_filename=f'{self._getDirectorioFicha()}{casilleros[f][c][1:]}.png', image_size=self._getCasilleroTamano())

    def actualizarTexto(self, texto, color=None, fondo=None, tamaño=24, pc=False):
        '''Actualiza el elemento que muestra texto relativo a las interacciones del
        jugador, o actualiza los diálogos de la PC si :param: pc=True.
        :param texto: String. Nuevo texto que contendrá la caja de mensajes.
        :param color: String. Color de texto.
        :param fondo: String. Color de fondo del texto.
        :param tamaño: Int. Tamaño de la fuente.
        :param pc: Booleano.Si es True, actualiza la caja de diálogos de la PC.
            Por defecto es False.'''
        self._getInterfaz()['textoJugador' if not pc else 'textoPC'].Update(texto, font=('Arial', tamaño), text_color=color, background_color=fondo)

    def actualizarTextoProgresivo(self, dialogo, tamaño, color, fondo, pc=False, velocidad=0.02):
        '''Muestra progresivamente el diálogo recibido como parámetro en el cuadro de
        texto de la PC o en el del jugador. El tamaño, color y fondo del texto
        son ajustables, así como también la velocidad y su destino.'''
        frase = ''
        for letra in range(0, len(dialogo)):
            frase += dialogo[letra]
            self.actualizarTexto(frase, tamaño=tamaño, color=color, fondo=fondo, pc=pc)
            self._getInterfaz().Refresh()
            #A menor número, mayor velocidad
            time.sleep(velocidad)

    def textoEstandar(self):
        '''Actualiza con su texto por defecto el elemento que muestra información relativa
        a las interacciones del jugador.'''
        self._getInterfaz()['textoJugador'].Update('                ---TUS FICHAS---              ', font=('Arial', 14), background_color='black', text_color='White')
    
    def inhabilitarElemento(self, clave):
        '''Inhabilita un elemento de la interfaz.
        :param clave: String con el nombre del elemento.'''
        self._getInterfaz()[clave].Update(disabled=True)

    def habilitarElemento(self, clave):
        '''Habilita un elemento de la interfaz.
        :param clave: String con el nombre del elemento.'''
        self._getInterfaz()[clave].Update(disabled=False)

    def borrarElemento(self, clave):
        '''Vuelve invisible un elemento de la interfaz.'''
        self._getInterfaz()[clave].Update(visible=False)

    def habilitarFinalizacion(self):
        '''Convierte el botón de cambiar fichas en un botón
        para finalizar la partida.'''
        self._getInterfaz()['cambiar'].Update(image_filename=f'{self._directorio_media}bolsafichasvacia.png')

    def popUp(self, cadena):
        '''Imprime una determinada cadena en una ventana simple.
        Su implementación fue realizada en el módulo "tema", dada su utilidad general
        y que también se utiliza en el resto de las interfaces del programa.'''
        aviso(cadena)

    def popUpOkCancel(self, cadena, botones):
        '''Ventana PopUp simple que imprime un string y posee uno o más botones.
        Su implementación fue realizada en el módulo "tema", dada su utilidad general
        y que también se utiliza en el resto de las interfaces del programa.'''
        evento = aviso(cadena, botones)
        return evento

    def turnoJugador(self, turno_jugador):
        if (turno_jugador):
            self._getInterfaz()['nombre_pc'].Update(background_color='#4f280a')
            self._getInterfaz()['nombre_jugador'].Update(background_color='Green')
        else:
            self._getInterfaz()['nombre_jugador'].Update(background_color='#4f280a')
            self._getInterfaz()['nombre_pc'].Update(background_color='Green')

    def ventanaPausa(self):
        event = menuPausa.menu_pausa()
        return event
    
    def cerrar(self):
        self._getInterfaz().Close()

    def click_X(self):
        '''Controla lo que ocurre al intentar cerrar la ventana desde el botón "X"'''
        instante = time.time()
        mensaje ="ATENCIÓN: ESTA PARTIDA SE PERDERÁ POR COMPLETO.\nPara guardar, diríjase al menú de pausa.\n¿Está seguro/a que desea salir?"
        if aviso(mensaje, ['Confirmar', 'Cancelar']) == '_Confirmar':
            #TKrootDestroyed es una variable de clase que indica si la ventana se destruyó.
            #Si es True, en el próximo read() de PySimpleGUI se retornará None, provocando que
            #el juego se cierre en el lazo principal.
            self._getInterfaz().TKrootDestroyed = True
        self.paralizarTimer(instante)

    def pantallaCompleta(self):
        if not (self._esPantallaCompleta()):
            self._getInterfaz().Maximize()
            self._setPantallaCompleta(True)
        else:
            self._getInterfaz().Normal()
            self._setPantallaCompleta(False)

    def _getDirectorioFicha(self):
        return self._directorio_fichas
    def _getDirectorioMedia(self):
        return self._directorio_media
    def _getCasilleroTamano(self):
        return self._tamcas
    def _getFichaTamano(self):
        return self._ficha_tamano
    def _getInterfaz(self):
        return self._interfaz
    def _setInterfaz(self, unaInterfaz):
        self._interfaz = unaInterfaz
    def _getTiempoInicio(self):
        return self._tiempo_inicio
    def _setTiempoInicio(self, segundos):
        self._tiempo_inicio = segundos
    def _getTiempoFin(self):
        return self._tiempo_fin
    def _setTiempoFin(self, segundos):
        self._tiempo_fin = segundos
    def _esPantallaCompleta(self):
        return self._pantallaCompleta
    def _setPantallaCompleta(self, valor):
        self._pantallaCompleta = valor