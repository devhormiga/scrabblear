import random
import PySimpleGUI as sg
from codigo.interfaz.tema import mi_tema

def infoConfiguracion(conf):
    '''
    Crea una ventana que muestra la configuración
    de la partida que se está jugando.
    '''
    columna = [
                [sg.Text('Nivel: '), sg.Text(f'{conf["nivel"].capitalize()}')],
                [sg.Text('Filas: '), sg.Text(f'{conf["filas"]}')],
                [sg.Text('Columnas: '), sg.Text(f'{conf["columnas"]}')],
                [sg.Text('Tiempo: '), sg.Text(f'{conf["tiempo"]} minutos')],
                [sg.Text('Cantidad de letras: ')]
                ]
    contador_salto = 6
    letras = []
    for clave, valor in sorted(conf['cant_fichas'].items()):
        letras.append(sg.Text(f'{clave}: {valor}'))
        contador_salto = contador_salto - 1
        if (contador_salto == 0):
            contador_salto = 6
            columna.append(letras)
            letras = []
    #Si quedaron letras por insertar luego de completar la última fila, las agrega
    if (len(letras) != 0):
        columna.append(letras)
    #Inserta los puntajes de las fichas
    columna.append([sg.Text('Puntajes de las fichas: ')])
    letras = []
    contador_salto = 6
    for puntaje, listado in sorted(conf['puntaje_ficha'].items()):
        for letra in listado:
            letras.append(sg.Text(f'{puntaje}: {letra}'))
            contador_salto = contador_salto - 1
            if (contador_salto == 0):
                contador_salto = 6
                columna.append(letras)
                letras = []
    if (len(letras) != 0):
        columna.append(letras)
        letras = []
    #Inserta los casilleros eseciales seleccionados
    columna.append([sg.Text('Casilleros especiales: ')])
    especiales = set(conf['especiales'].values())
    if (len(especiales) > 0):
        for especial in especiales:
            if (especial == '*sum'):
                columna.append([sg.Text('+: Obtienes 5 puntos adicionales.')])
            elif (especial == '*rest'):
                columna.append([sg.Text('-: Pierdes 5 puntos del total conseguido.')])
            elif (especial == '*mult'):
                columna.append([sg.Text('x2: Duplica el valor de la palabra')])
            elif (especial == '*div'):
                columna.append([sg.Text('%2: Divide a la mitad el total de la palabra')])
            elif (especial == '*0'):
                columna.append([sg.Text('0: Anula el valor de la palabra')])
    else:
        columna.append([sg.Text('No se seleccionaron casilleros especiales')])

    layout=[[sg.Column(columna,background_color='#4f280a', key='informacion')],[sg.Button('Volver',button_color=('black', '#f75404'),key='volverConf')]]
    mi_tema()

    ventana = sg.Window('configuracion',layout=layout,background_color= '#f39c12',
                        no_titlebar=True,grab_anywhere=True, keep_on_top=True)

    while True:
        event, value = ventana.read()
        if event == 'volverConf'  :
            break
        elif event == None:
            break
    ventana.close()

def especial(filas, columnas, nivel, esp_personalizados=[]):
    '''
    Genera casilleros especiales según el nivel,
    teniendo en cuenta la cantidad de columnas, filas y la dificultad.
    Además, controla que exista cierta cantidad de casilleros especiales
    '''
    especiales = {}
    if nivel == 'facil':
        esp = ['*rest', '*sum']
        minEsp= 10
    elif nivel == 'medio':
        esp = ['*rest', '*sum', '*mult', '*div' ]
        minEsp = 7
    elif nivel == 'dificil':
        esp = ['*rest', '*sum', '*mult', '*0', '*div']
        minEsp = 7
    else:
        esp = esp_personalizados
        if (len(esp) == 0):
            return especiales
    for fila in range(filas):
        for columna in range(columnas):
            probabilidad = random.randint(0, 100)
            if probabilidad < 25:
                #Crea el casillero especial
                coordenada = str(fila) + ', ' + str(columna)
                random.shuffle(esp)
                especiales[coordenada] = esp[0]
    return especiales

def nivel_facil():
    '''
    Mayor tiempo de juego y puntaje más alto en vocales y consonantes de mayor uso.
    Retorna una configuracion
    '''                                             
    conf = {
        'nivel':'facil',
        'filas':15,
        'columnas':15,
        'especiales':{},

        'tiempo': 25, #minutos
        'cant_fichas': {'A':15, 'E':15, 'O':15, 'S':7, 'I':10,'U': 10,'N': 5, 'L': 4, 'R': 4, 'T': 4,'C': 4,
                        'D': 4, 'G': 2, 'M': 3, 'B': 3,'P': 2, 'F': 2, 'H': 2,
                        'V': 2, 'Y': 1,'J': 2, 'K': 1, 'Ñ': 1, 'Q': 1, 'W': 1, 'X': 1, 'Z': 1 },

         #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
         'puntaje_ficha' : {
        5: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
        2: ['C', 'D', 'G'],
        8: ['M', 'B', 'P'],
        4: ['F', 'H', 'V', 'Y'],
        6: ['J'],
        9: ['K', 'Ñ', 'Q', 'W', 'X'],
        10: ['Z']
    }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf


def nivel_medio():
    '''
    En comparación con el nivel fácil:
    Configura un nivel con menor cantidad de vocales y de puntaje en estas letras y consonantes
    de mayor uso; tablero y tiempo más acotado.
    Retorna una configuracion
    '''                                              
    conf = {
        'nivel': 'medio',
        'filas':15,
        'columnas':15,
        'especiales': {},
        'tiempo': 20, #minutos
        # el indice es la letra y e lvalor la cantidad de fichas de esa letra

        'cant_fichas' : {
        'A':15, 'E':15, 'O':15, 'S':7, 'I':10,'U': 10,
            'N':5, 'L':4, 'R':4, 'T':4,
        'C':4, 'D':4, 'G' :2, 'M' :3, 'B' :3,
        'P' :2, 'F' :2, 'H' :2, 'V':2, 'Y' :1,
        'J':2, 'K' :1, 'Ñ' :1, 'Q' :1, 'W' :1, 'X' :1, 'Z' :1
    },

         #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
         'puntaje_ficha' : {
        1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
        2: ['C', 'D', 'G'],
        3: ['M', 'B', 'P'],
        4: ['F', 'H', 'V', 'Y'],
        6: ['J'],
        8: ['K', 'Ñ', 'Q', 'W', 'X'],
        10: ['Z']
    }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf


def nivel_dificil():
    '''
    En comparación con el nivel fácil:
    Configura un nivel con menor cantidad de vocales y de puntaje en estas letras y consonantes
    de mayor uso; tablero y tiempo más acotado.
    Con respecto a nivel medio es el mismo tipo de tablero.
    Incorpora casilleros con mayor tipo de descuento de puntuación
    Retorna una configuracion
    '''
    conf = {
        'nivel': 'dificil',
        'filas': 10,
        'columnas': 10,
        'especiales': {},  # ver de armarl ode forma random
        'tiempo': 15,  # minutos
        # el indice es la letra y e lvalor la cantidad de fichas de esa letra

        'cant_fichas': {
            'A':15, 'E':15, 'O':15, 'S':7, 'I':10,'U': 10,
        'N':5, 'L':4, 'R':4, 'T':4,
        'C':4, 'D':4, 'G' :2, 'M' :3, 'B' :3,
        'P' :2, 'F' :2, 'H' :2, 'V':2, 'Y' :1,
        'J':2, 'K' :1, 'Ñ' :1, 'Q' :1, 'W' :1, 'X' :1, 'Z' :1
        },

        #  dic el indice indica le puntaje y lo valores son las letras que itenen ese puntaje
        'puntaje_ficha': {
            1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T', 'C', 'D', 'G'],
            3: ['M', 'B', 'P'],
            4: ['F', 'H', 'V', 'Y'],
            6: ['J'],
            8: ['K', 'Ñ', 'Q', 'W', 'X'],
            10: ['Z']
        }
    }
    conf['especiales'] = especial(conf['filas'], conf['columnas'],conf['nivel'])
    return conf
