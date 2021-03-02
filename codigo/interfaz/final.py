import PySimpleGUI as sg
from codigo.logica.puntuaciones_maximas import*
from codigo.interfaz.interfaz_puntaje import*
from codigo.interfaz.tema import *
from codigo.interfaz.interfaz_palabras import*
from codigo.logica.jugador import*

def fichas_sobrantes(fichas):
    '''
    Establece los puntajes sobrantes. Utiliza un atril, del cual toma sus values
    '''
    puntaje = 0
    letras = ''
    lista_sobrantes = []
    for f in range(fichas.get_cant_fichas()):
        lista_sobrantes.append(fichas.get_ficha(f))
        puntaje += list(lista_sobrantes[f].values())[0]
        letras = letras + ' ' + list(lista_sobrantes[f].keys())[0]
    return puntaje, letras.upper()

def ver_ganador (jug,pc,ven,atril_jug,atril_pc):
    '''
    Primero actualiza la pantalla con los puntajes de ambos jugadores. Después define el vencedor.
    '''
    sobrante_jug, letras_jug  = fichas_sobrantes (atril_jug)
    sobrante_pc, letras_pc  = fichas_sobrantes (atril_pc)
    jug = jug - sobrante_jug
    if jug < 0:
        jug = 0
    pc = pc - sobrante_pc
    if pc < 0:
        pc = 0
    ven['pje_jug'].update(value=jug)
    ven['fichas_jug'].update(value=letras_jug)
    ven['fichas_pc'].update(value=letras_pc)
    ven['pje_pc'].update(value=pc)
    if int(jug) > int(pc):
        ven['ganador'].update(value='FELICIDADES, ¡¡GANASTE!!')
    elif int(jug) < int(pc):
        ven['ganador'].update(value='QUÉ LÁSTIMA.. PERDISTE')
    else:
        ven['ganador'].update(value='EMPATE SOBRE EL FINAL')
    #Retorna el puntaje del jugador actualizado
    return jug

def terminar(nombre, punt_jug,punt_pc,pal_jug,pal_pc,nivel,atril_jug,atril_pc):
    '''
    Construye una interfaz para determinar qué jugador salió vencedor. Permite acceder a las palabras que cada uno utilizó y
    a las puntuaciones máximas
    '''
    contenido = [
        [sg.Text('TU PUNTAJE FINAL',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'))],
        [sg.Text(key='pje_jug',size=(50,1),justification='center',font=('Arial',50),background_color='Black',text_color='white')],
        [sg.Text('Tus fichas sobrantes: ',size=(20,2),font=('Impact',12),text_color=('#D09F61')),
        sg.Text(key='fichas_jug',size=(20,1),justification='center',font=('Arial',10),background_color='Black',text_color='white')],
        [sg.Text('PUNTAJE DE LA PC',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_pc')],
        [sg.Text(key='pje_pc',size=(50,1),justification='center',font=('Arial',50),background_color='Black',text_color='white')],
        [sg.Text('Fichas sobrantes de la COMPUTADORA: ',size=(20,2),font=('Impact',12),text_color=('#D09F61')),
        sg.Text(key='fichas_pc',size=(20,1),justification='center',font=('Arial',10),background_color='Black',text_color='white')],
        [sg.Text(key='ganador',size=(50,1),justification='center',font=('Arial',20),background_color='Black',text_color='white')],
        [sg.Text('',size=(5,1)),
        sg.Button('Salir', font=('Arial', 10), size=(10, 2),button_color=('black', '#f75404'), key='salir'),
        sg.Button('Listado de palabras', font=('Arial', 10), size=(10, 2),button_color=('black', '#f75404'), key='list_pal'),
        sg.Button('Puntuaciones Máximas', font=('Arial', 10), size=(10, 2),button_color=('black', '#f75404'), key='puntajes')]

        ]
    mi_tema()
    ven = sg.Window('Ganador', layout=contenido, size=(400, 450), no_titlebar=False, keep_on_top=True)
    ven.finalize()
    #Actualiza la ventana para mostrar quién ganó
    punt_jug = ver_ganador(punt_jug, punt_pc, ven, atril_jug, atril_pc)
    puntaje = Puntuacion_Maxima()
    puntaje.agregar(Jugador(nombre, punt_jug, nivel))

    while True:
        event, values = ven.read()
        if event in (None, 'salir'):
            break
        if event == 'list_pal':
            # Abre la ventana de las palabras utilizadas
            listado_palabras(pal_jug, pal_pc)
        if event == 'puntajes':
            # Abre la ventana de puntuaciones máximas
            puntajes()
    ven.close()


if __name__ == '__main__':
    terminar()
