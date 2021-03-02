import PySimpleGUI as sg
from codigo.interfaz.tema import *

def listado_palabras (jugador,pc):
    '''
    Lista en pantalla las palabras que se utilizaron en la partida. Cada 4 palabras hace un salto de línea.
    '''

    def listar (jugador,pc):
        #Lista con las palabras del jugador
        j_pal = []
        #Lista con los puntajes de esas palabras
        j_pun =[]
        for p in range (len(jugador)):
            j_pal = j_pal + list(jugador[p].keys())
            j_pun = j_pun + list(jugador[p].values())
        pal_jug = ''
        insertar_salto = 4
        for pal in range(len(jugador)):
            pal_jug = pal_jug + str(j_pal[pal].upper()) + ': ' + str(j_pun[pal]) + ' | '
            insertar_salto = insertar_salto - 1
            if (insertar_salto == 0):
                pal_jug = pal_jug + '\n'
                insertar_salto = 4
        pc_pal = []
        pc_pun = []
        pal_pc = ''
        for p in range (len(pc)):
            pc_pal = pc_pal + list(pc[p].keys())
            pc_pun = pc_pun + list(pc[p].values())
        insertar_salto = 4
        for pal in range(len(pc)):
            pal_pc = pal_pc + str(pc_pal[pal].upper()) + ': ' + str(pc_pun[pal]) + ' | '
            insertar_salto = insertar_salto - 1
            if (insertar_salto == 0):
                pal_pc = pal_pc + '\n'
                insertar_salto = 4
        ven['pal_jugador'].update(value=pal_jug)
        ven['pal_pc'].update(value=pal_pc)


    contenido = [
        [sg.Text('Palabras utilizadas por el Jugador',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_jug')],
        [sg.Text(key='pal_jugador',size=(200,14),justification='center',font=('Arial',10),background_color='Black',text_color='white')],
        [sg.Text('Palabras utilizadas por la PC',size=(40,1),font=('Impact',14),justification='center',text_color=('#D09F61'),key='_pc')],
        [sg.Text(key='pal_pc',size=(200,14),justification='center',font=('Arial',10),background_color='Black',text_color='white')],
        [sg.Button('Salir', font=('Arial', 16), size=(10, 1),button_color=('black', '#f75404'), key='salir') ]

        ]
    mi_tema()
    ven = sg.Window ('Listado de Palabras',layout=contenido,size= (400,600), no_titlebar=True,grab_anywhere=True,keep_on_top=True)
    ven.finalize()

    while True:
        listar (jugador,pc)
        event, values = ven.read()
        if event in (None,'salir'):
            break
    ven.close()

if __name__ == '__main__':
    listado_palabras()
