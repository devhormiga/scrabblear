import PySimpleGUI as sg
from codigo.logica.puntuaciones_maximas import *
from codigo.interfaz.tema import *
import os
def actualizar_puntaje (puntaje,ventana):
    '''
    Lista en pantalla los puntajes almacenados
    '''
    listado_puntos =''
    for p in range(len(puntaje.puntajes)):
        listado_puntos = listado_puntos + str(puntaje.puntajes[p].infoJugador().upper() ) + '\n'
        ventana['puntos'].update(value=listado_puntos)

def blanquear (puntaje):
    '''
    Vuelve a 0 todos los puntajes, nombres y dificultades
    '''
    puntaje._vaciar_puntajes()
    puntaje.guardar()
    actualizar_puntaje(puntaje)

def puntajes():

    imgPuntos = os.path.join('media','media_ii', 'puntuaciones2.png')
    contenido = [
        #[sg.Text('Puntuaciones máximas',size=(20,1),font=('Impact',18),text_color=('black'),key='_puntos')],
        [sg.Image(filename=imgPuntos, )],
        [sg.Text(key='puntos',size=(200,10),justification='center',font=('Impact',16),background_color='#afad71',text_color='Black')],
        [sg.Button('Borrar puntuación',font=('Arial',16),size=(10,3),button_color=('black', '#f75404'),key='reestablecer'),
         sg.Button('volver', font=('Arial', 16), size=(14, 3),button_color=('black', '#f75404'), key='volver') ]

        ]
    mi_tema()
    ventana = sg.Window ('Puntaje Máximo',layout=contenido,size= (420,500),element_justification='center', no_titlebar=True,grab_anywhere=True, keep_on_top=True)
    ventana.finalize()

    puntuaciones = Puntuacion_Maxima()
    puntuaciones.cargar()
    actualizar_puntaje(puntuaciones,ventana)
    while True:
        event, values = ventana.read()
        if event in ( None,'volver'):
            break
        elif event == 'reestablecer':
            decision = aviso('¿Realmente desea borrar los puntajes?', ['Sí', 'No'])
            if decision == '_Sí':
                puntuaciones._vaciar_puntajes()
                actualizar_puntaje(puntuaciones,ventana)
    ventana.close()


if __name__ == '__main__':
    puntajes()
