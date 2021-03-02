import PySimpleGUI as sg
import os

#evaluar si es un objeto menu

def menu_pausa():
    '''
    Menú pausa que permite acceder a guardar la partida o abandonar la misma. También volver a la pantalla del juego
    '''
    img_boton_largo = os.path.join('media', 'media_ii', 'botonlargo.png')
    img_logo = os.path.join('media','media_ii', 'scrabbleArLogo.png')
    layout = [[sg.Image(img_logo, background_color='#4f280a')],
              [sg.Button('Retomar', image_filename=img_boton_largo, button_color=('black', '#4f280a'), border_width=0, font=('Italic 24'),
                         size=(20, 3), key='retomar')],
              [sg.Button('Guardar', image_filename=img_boton_largo, border_width=0,button_color=('black', '#4f280a'), font=('Italic 24'),
                         size=(20, 3), key='guardar')],
              [sg.Button('Abandonar', image_filename=img_boton_largo, border_width=0,button_color=('black', '#4f280a'), font=('Italic 24'), size=(20, 3),
                         key='abandonar')],

              ]

    ventana = sg.Window('pausa',layout=layout, background_color='#4f280a', no_titlebar=True,element_justification='center',force_toplevel=True, keep_on_top=True).Finalize()
    while True:
        event, value= ventana.read()

        if event == None:
            break
        if (event == 'retomar') or (event == 'guardar') or (event == 'abandonar'):
            break
    ventana.close()

    return event

if __name__ == '__main__':
    menu_pausa()
