import PySimpleGUI as sg
import os
from codigo.interfaz.tema import mi_tema

def general(dirAyuda):
    sg.theme_text_element_background_color('#4f280a')
    sg.theme_element_background_color('#4f280a')
    col = [[sg.Image(filename=f'{dirAyuda}ayuda 3.png'),sg.Text('Muestra la ayuda',font=('Arial, 16'),text_color='white')], #botón ayuda
           [sg.Image(filename=f'{dirAyuda}ayuda 5.png'),sg.Text('Comenzar a jugar',font=('Arial, 16'),text_color='white')], #botón comenzar a jugar
           [sg.Image(filename=f'{dirAyuda}ayuda 9.png'), sg.Text('Muestra la tabla de puntajes', font=('Arial, 16'), text_color='white')], #botón puntajes
           [sg.Image(filename=f'{dirAyuda}ayuda 6.png'), sg.Text('Inicia una Nueva partida', font=('Arial, 16'), text_color='white')], #botón nueva partida
           [sg.Image(filename=f'{dirAyuda}ayuda 4.png'), sg.Text('Carga una partida guardada', font=('Arial, 16'), text_color='white')], #botón cargar partida
           [sg.Image(filename=f'{dirAyuda}ayuda 10.png'), sg.Text('Vuelve al Menu principal', font=('Arial, 16'), text_color='white')], #botón volver menú principal
           [sg.Image(filename=f'{dirAyuda}ayuda 22.png'), sg.Multiline(default_text=
                                                      'En esta ventana se configuran los datos para la nueva partida: \n'
                                                      'El apodo debe tener entre 3 y 10 caracteres y no se pueden utilizar caracteres especiales.\n' 
                                                      'Se debe elegir una dificultad, las opciones son "fácil", "medio" o "díficil". '
                                                      'También se puede jugar una partida "personalizada".\n'
                                                      'La imagen de avatar se puede cambiar desde este menú.\n' 
                                                      'Al momento de oprimir "Jugar" se muestra un ventana de confirmación, y\n'
                                                      'en todo momento se puede cancelar y volver atrás.\n',
                                                        auto_size_text=True, font=('Arial, 12'), text_color='white', disabled=True, size=(30,10),background_color='#4f280a')],
    ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',vertical_scroll_only=True,size=(700,470))]
    return layout

def juego(dirAyuda):
    col = [     #Ayuda 14 = tablero, ayuda 0 = timer
        [sg.Image(filename=f'{dirAyuda}ayuda 14.png'), sg.Multiline('Vista general del tablero. A continuación se encuentra detallada la información sobre cómo jugar:', font=('Arial, 16'), text_color='white', disabled=True, size=(25,10),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 0.png')], [sg.Multiline('En el area superior se encuentra el indicador de tiempo, el botón de pausa, ayuda y pantalla completa.\n'
                                                                     '\n1) TEMPORIZADOR: A la derecha de "Jugado" se puede visualizar el tiempo transcurrido y el tiempo total. '
                                                                     'La barra de color naranja indica el tiempo restante, que se reduce a medida que progresa la partida.\n'
                                                                     '2) PAUSA: Si se oprime, la partida queda detenida y se despliega un menú de opciones (abajo explicadas).\n'
                                                                     '3) Botón "?": Abre esta misma ayuda.\n'
                                                                     '4) Botón "[ ]" (el último en la fila): Cambia a pantalla completa.', font=('Arial, 12'), text_color='white', disabled=True, size=(40,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 8.png'), #Botón para ver configuración de nivel
         sg.Multiline('Sobre los avatares de los jugadores se encuentra un botón que, al presionarlo, '
                 'mostrará la configuración elegida para la partida.', font=('Arial, 12'), text_color='white', disabled=True, size=(30,6),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 19.png'), #indicadorJugador
         sg.Multiline('A la derecha del tablero se encuentra el avatar de cada jugador. '
                 'Debajo se encuentra el apodo elegido y los puntos acumulados. \n '
                 'El apodo remarcado con color verde indica de quién es el turno.', font=('Arial, 12'), text_color='white',disabled=True, size=(30,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 1.png'), #atril
         sg.Multiline('Debajo de los avatares se encuentra el atril de fichas, '
                  'el boton "Validar" (símbolizado con un ✓) y el botón "Cambiar fichas" (simbolizado con una bolsa).'
                 '\nCuando se seleccione una ficha ésta se pondra transparente, como se indica en la imagen. \n'
                  'En el area superior del atril se comenzará a visualizar la palabra en formación.\n'
                  'Notas: Al seleccionar una ficha no se puede presionar la bolsa para cambiarlas.\n'
                 'Además, si se deja quieto el mouse sobre una ficha se mostrará una etiqueta con su puntaje.\n'
                 'En el botón de preferencias pueden verse todos los puntajes para esa partida.', font=('Arial, 12'), text_color='white',disabled=True, size=(20,8),background_color='#4f280a')],

        [sg.Image(filename=f'{dirAyuda}ayuda 40.png')],  # atril validado
        [sg.Multiline('Al clickear en una o más fichas se habilitará el botón Deshacer, que '
                      'permite corregir errores al momento de formar una palabra '
                      'o deshacerla completamente si se arrepintió. Puede volver atrás con cada ficha '
                      'que necesite.',
                      font=('Arial, 12'), text_color='white', disabled=True, size=(40, 8),
                      background_color='#4f280a')],

        [sg.Image(filename=f'{dirAyuda}ayuda 2.png')], #atril validado
         [sg.Multiline('Una vez que se formó una palabra, se debe dar click en el boton de validar. Si ésta es válida, '
                  'ScrabbleAR le indicará que seleccione dónde insertarla.\n'
                  'En la pestaña "Reglas" podrá consultar las reglas generales de ScrabbleAR, '
                  'como indica la imagen', font=('Arial, 12'), text_color='white',disabled=True, size=(40,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 33.png'), sg.Multiline('Cuando se clickea en un casillero del tablero, se muestra el indicador de orientación.\n'
                                                                       'Una vez seleccionado el sentido (horizontal o vertical),la palabra quedará insertada de manera permanente.',
                                                            font=('Arial, 12'), text_color='white',disabled=True, size=(30,8),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 27.png'), sg.Image(filename=f'{dirAyuda}ayuda 28.png'), ], #palabra pc y palabra jugador
        [sg.Multiline('En el tablero, las palabras con fondo ROJO son las insertadas por el oponente '
                 'y las de VERDE por el jugador',font=('Arial, 12'), text_color='white',disabled=True, size=(40,5),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 7.png'), sg.Multiline('Si el botón para cambiar fichas muestra la leyenda "FINALIZAR", puede que hayan pasado dos cosas:\n'
                                                                     '- No hay mas fichas en la bolsa.\n- No puedes cambiar las fichas (el máximo permitido de cambios es tres). ',
                                                            font=('Arial, 12'), text_color='white',disabled=True, size=(20,10),background_color='#4f280a')],
        [sg.Image(filename=f'{dirAyuda}ayuda 30.png'), sg.Image(filename=f'{dirAyuda}ayuda 29.png'),sg.Image(filename=f'{dirAyuda}ayuda 18.png'),], #pausa, pantalla final, historial palabras
         [sg.Multiline('Aquí puede verse el menu de Pausa.\n'
                  'Se puede retornar a la partida, guardarla o abandonar. \n' 
                  'En caso de abandonar o finalizar, o si se terminó el tiempo, se abrirá la ventana de fin de partida. '
                  'En ésta última, se indicarán los puntos de cada jugador y determinará quién ganó. '
                  'Además, si se presiona en "Listado de palabras" podrán verse las palabras que cada uno insertó '
                  'con sus respectivos puntajes.'
                  ,font=('Arial, 12'), text_color='white',disabled=True, size=(40,8),background_color='#4f280a')],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout

def iconCas(dirAyuda):
    col = [
        [sg.Image(filename=f'{dirAyuda}ayuda 25.png'), sg.Text('Casillero seleccionado para insertar palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 24.png'), sg.Text('Insertar horizontalmente', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 23.png'), #estos tres son la orientación
         sg.Text('Insertar verticalmente', font=('Arial, 18'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 34.png'), #suma
         sg.Text('Incrementa 5 puntos el valor total de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 20.png'), #resta
         sg.Text('Resta 5 puntos al valor total de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 21.png'), #multiplica x 2
         sg.Text('Duplica el valor de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 15.png'), #divide
         sg.Text('Divide a la mitad el valor de la palabra', font=('Arial, 16'), text_color='white')],
        [sg.Image(filename=f'{dirAyuda}ayuda 11.png'), #multiplica x 0
         sg.Text('Anula el valor de la palabra', font=('Arial, 16'), text_color='white')],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout

def otros(dirAyuda):
    logo = os.path.join('media','media_ii','scrabbleArLogo.png')
    licencia = open(os.path.join('licencia.txt'), 'r', encoding="utf8")
    texto = licencia.read()
    licencia.close()
    col = [
        [sg.Image(logo,pad=(50,50))], [sg.Text('Sobre ScrabbleAR', font=('Arial, 18'), text_color='white',justification='center')],
        [sg.Text('Este proyecto es el resultado de un trabajo final.'
                      'Fue desarrollado en el marco académico de la materia '
                      '"Seminario de Lenguaje - Python", de la Facultad de Informática (UNLP)'
                      '' , font=('Arial, 14'), text_color='white',justification='center', size=(40, 8),
                      background_color='#4f280a')],


        [sg.Image(filename=f'{dirAyuda}team.png')],[sg.Text('\tDesarrollado por: ', font=('Arial, 18'), text_color='white',justification='center')],
                                                    [sg.Text('\tDiego Vilardebó \n'
                                                            '\tEnzo Diaz \n'
                                                            '\tIvan Knopoff\n'
                                                            ,font=('Arial, 14'), text_color='white', size=(40, 8),
                                                            background_color='#4f280a', justification='center', )],
        [sg.Text('Github: ')],[sg.Text('https://github.com/enzodiaz25/Scrabble.git')],
        [sg.Multiline(texto,
                      font=('Arial', 12), text_color='white', size=(53, 20),
                      pad=((10, 10), 10), disabled=True, background_color='#4f280a')]
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',justification='center',
                        element_justification='center', vertical_scroll_only=True,size=(700,470))]

    return layout

def reglas():
    imgReglas = os.path.join('media', 'ayuda', 'ayuda 39.png') #reglas
    col = [[sg.Image(filename=imgReglas)],
           [sg.Multiline('¡¿Cómo te va?! Vamos a jugar al ScrabbleAR. Veamos bien cómo se juega... '
                         'Sí, es el famoso juego de mesa donde probarás tu conocimiento acerca de las palabras realmente '
                         'existentes. Frente a tí tendrás al computador. ¿Serás capaz de derrotarlo? Lo primero que debes saber '
                         'es que las distintas dificultades afectan la inteligencia del ordenador. ¿Inteligencia? Dejémoslo así '
                         'por el momento. Puedes elegir entre FÁCIL, MEDIO, DIFÍCIL, o PERSONALIZAR íntegramente la partida. Además de tener un '
                         'adversario más complejo de enfrentar, cambian algunas disposiciones del juego. '
                         'Una vez elegida la dificultad se abrirá el tablero y comenzará la verdadera prueba. En este juego tienes tres cosas para '
                         'hacer:\n •Escoger entre las fichas de tu atril la combinación que forme la mejor palabra (cada letra posee '
                         'una puntuación propia, así que toda palabra tiene un puntaje) y, luego de eso, colocarla en la mejor '
                         'posición del tablero. Un detalle, antes de colocar tu palabra en el tablero deberás '
                         'validarla. No queremos tramposos.\n •Cambiar tus fichas por nuevas. ¡Ojo! Sólo dispones de 3 (tres) '
                         'cambios por partida.\n •Rendirte... Bueno, esto mejor no.\nPresta mucha atención al tablero de juego. Encontrarás '
                         'casilleros especiales donde se sumarán puntos o quizás multipliques el valor de una palabra... Pero '
                         'también hay otros que restan, dividen o hasta multiplican el valor total por CERO. Escoge con mucho '
                         'cuidado dónde colocarás tu palabra. Por suerte para tí esto también afecta al ordenador. Las palabras '
                         'pueden insertarse en vertical u horizonal. En este juego no podrás hacerlo '
                         'en diagonal. Tampoco está permitido que se crucen las palabras entre sí. Calcula muy bien los '
                         'espacios disponibles.\n¿Cuándo termina la partida? Cuando no hay más fichas en algún atril y '
                         'tampoco en la bolsa de fichas, cuando no hay espacios en el Tablero o cuando alguno de los dos '
                         'jugadores han agotado sus cambios de fichas disponibles y aún así no tienen dónde ubicar una nueva '
                         'combinación de letras. Al finalizar se comparan las puntuaciones y... ¡Tenemos un ganador!',
                         font=('Arial',12),text_color='white',size=(53,20),
                         pad=((10,10),10),disabled=True,background_color='#4f280a')],

    ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a',element_justification='center', justification='center', vertical_scroll_only=True,size=(720,470))]
    return layout

def popReglas():
    '''
    Crea la ventana que se invoca antes de cada partida explicando las reglas generales del juego
    '''    
    layout = [reglas(),
              [sg.Button('¡Comenzar!',size=(20,5), font=('Arial', 16), key='comenzar')],]
    ventana = sg.Window('Reglas', layout=layout,element_justification='center',
                        no_titlebar=True,grab_anywhere=True, keep_on_top=True,background_color='#afad71',border_depth=50).Finalize()
    while True:
        event, values = ventana.read()
        if event in ( None,'comenzar'):
            break
    ventana.close()

def niveles(dirAyuda):
    col = [[sg.Frame(
            layout=[[sg.Multiline(' Tamaño del tablero: 15*15.\n'
                             '>Puntajes de las fichas:\n'
                             '\tVocales y consonantes L, N, S, T, R = 5 pts\n' 
                             '\tC, D, G = 2 pts \n'
                             '\tM, B, P = 8 pts \n '
                             '\tF, H, V, Y = 4 pts \n'
                             '\tJ = 6 pts\n'
                             '\tK, Ñ, Q, W, X = 9 pts\n' 
                             '\tZ= 10 pts \n\n'
                             '>Cantidad de fichas: 122\n\n'
                             '>Duración de la partida: 25 minutos\n\n'
                             '>Tipos de casilleros especiales: Suma y resta\n\n'
                             '>Oportunidades para cambiar las fichas de la PC: 1\n\n'
                             '>Tipos de palabras permitidas: Sustantivos, adjetivos y verbos\n\n'
                             '>Tras el cambio de fichas: Continúa el turno del JUGADOR\n\n'
                             '>Dificultad de la PC: Busca la primer palabra posible y la inserta en el primer lugar disponible\n',
                             font=('Arial, 12'), text_color='black',disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Facil', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='left',  key='contenedor_facil'),],
        [sg.Frame(
            layout=[[sg.Multiline('Tamaño del tablero 15*15. \n'
                             '>Puntajes de las fichas: \n'
                             '\tVocales y L, N, S, T, R = 1 pts\n'
                             '\tC, D, G = 2 pts\n'
                             '\tM, B, P = 3 pts\n'
                             '\tF, H, V, Y = 4 pts\n'
                             '\tJ = 6 pts\n'
                             '\tK, Ñ, Q, W, X = 8 pts\n'
                             '\tZ= 10 pts\n\n'
                             '>Cantidad de fichas: 122\n\n'
                             '>Duración de la partida: 20 minutos\n\n'
                             '>Tipos de casilleros especiales: Suma, resta, multiplica x 2, divide x2.\n\n'
                             '>Oportunidades para cambiar las fichas de la PC: 1\n\n'
                             '>Tras el cambio de fichas: Le toca el turno a la COMPUTADORA\n\n'
                             '>Tipos de palabras permitidas: Adjetivos y verbos\n\n'
                             '>Dificultad de la PC: Evalúa la primer palabra que puede formar y analiza en el tablero cuál es la mejor posición\n',
                             font=('Arial, 12'), text_color='black',disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Medio', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='center', key='contenedor_medio'), ],
        [sg.Frame(
            layout=[[sg.Multiline('Tamaño tablero: 10*10\n'
                             '>Puntaje de Fichas: \n'
                             '\tVocales y L, N, S, T, R = 1 pts\n'
                             '\tC, D, G = 1 pts \n'
                             '\tM, B, P = 3 pts\n'
                             '\tF, H, V, Y = 4 pts\n'
                             '\tJ = 6 pts\n'
                             '\tK, Ñ, Q, W, X = 8 pts\n'
                             '\tZ= 10 pts\n\n'
                             '>Cantidad de fichas: 122\n\n'
                             '>Duración de la partida: 15 minutos\n\n'
                             '>Tipo de casilleros especiales: Suma, resta, multiplica x 2, divide x2, anula valor de la palabra\n\n'
                             '>Oportunidades para cambiar las fichas de la PC: 1\n\n'
                             '>Tras el cambio de fichas: Le toca el turno a la COMPUTADORA\n\n'
                             '>Tipos de palabras permitidas: Adejtivos y verbos\n\n'
                             '>Dificultad de la PC: Prueba todas las palabras posibles a fin de encontrar la mejor combinación palabra-espacio\n',
                             font=('Arial, 12'), text_color='black', disabled=True, size=(45,8),background_color='#afad71')]],
            title='Nivel Dificil', title_color='white' , relief=sg.RELIEF_SUNKEN, font=('Impact 24'),
            element_justification='center' , key='contenedor_dificil'), ],
        ]
    layout = [sg.Column(col,scrollable=True,background_color='#4f280a', vertical_scroll_only=True,size=(700,470))]
    return layout



def ayuda() :
    '''Esta función es la encargada de motrar la interfaz
    que brinda ayuda a los/as jugadores/as. Da información de cómo se juega,
    detalle sobre las ventanas y los popUps que utiliza la aplicación '''

    dirAyuda = os.path.join('media','ayuda','')

    tabGeneral = [general(dirAyuda)]
    tabJuego = [juego(dirAyuda)]
    tabReglas = [reglas()]
    tabNiveles = [niveles(dirAyuda)]
    tabIconCas = [iconCas(dirAyuda)]

    tabOtros = [otros(dirAyuda)]    # Agregar solapa o boton que te de un poco de info del proyecto, un link a Git y que diga que en el informe ocmpleto hay mas info



    layout = [[sg.TabGroup([[sg.Tab('General', tabGeneral,background_color='#4f280a',  key='pGeneral'),
                          sg.Tab('Instrucciónes de Juego', tabJuego ,background_color='#4f280a',),
                          sg.Tab('Íconos y casilleros', tabIconCas,background_color='#4f280a',),
                          sg.Tab('Reglas', tabReglas, background_color='#4f280a', element_justification='center'),
                          sg.Tab('Niveles', tabNiveles, background_color='#4f280a',element_justification='center' ),
                          sg.Tab('Más', tabOtros,background_color='#4f280a',)]],
                           font=('Arial', 14),
                          key='pestanas', title_color='red',
                          selected_title_color='white', tab_location='top',theme=mi_tema())],
              [sg.Button('Cerrar',button_color=('black','#f75404'), font=('Arial', 16),size=(20,10),key='cerrar')]]

    mi_tema()
    ventana = sg.Window('Ayuda', layout=layout,element_justification='center',grab_anywhere=True,no_titlebar=True,
                      keep_on_top=True,border_depth=5,background_color='#afad71',  size=(780,580)).Finalize()
    while True:

        eventos, valor = ventana.read()
        if eventos in (None, 'cerrar'):
            break
    ventana.close()






if __name__ == '__main__':
    ayuda()
    popReglas()
