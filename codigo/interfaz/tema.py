dimport PySimpleGUI as sg

def mi_tema():
    '''
    Configuración genérica del diseño de las interfaces que facilita el diseño. 
    Después se adapta a la especificidad de cada pestaña.
    '''
    sg.LOOK_AND_FEEL_TABLE['scrabble'] = {'BACKGROUND': '#4f280a', ##133d51',
                                            'TEXT': '#fff4c9',
                                            'INPUT': '#c7e78b',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL': '#c7e78b',
                                            'BUTTON': ('black', '#4f280a'),
                                            'PROGRESS': ('#01826B', '#D0D0D0'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                            }
    sg.theme('scrabble')

def aviso(mensaje = 'Este es un mensaje estandar', botones = ['Entendido']):
    '''Genera un PopUp personalizado en función de dos parámetros:
    :mensaje : Es la información que se imprimirá en la ventana.
    :botones: Lista con las etiquetas de los botones (formato string). Las KEY
    se componen de un '_' y el nombre recibido por parametro.
    Retorna el evento seleccionado (boton clickeado).'''

    layout = [[sg.Text(mensaje, font=('Arial', 12), text_color='black', background_color='white')],]

    botonLis = []
    for b in botones:
        botonLis.extend([sg.Button(button_text=b, border_width=1, button_color=('black', '#f75404'), font=('Arial', 12), key=f'_{b}')])

    layout.append(botonLis)
    popup = sg.Window('AVISO', layout, background_color='white', no_titlebar=True, keep_on_top=True,grab_anywhere=True, element_justification='center').Finalize()

    while True:
        evento = popup.read()
        if evento:
            break
    popup.Close()

    return evento[0]

if __name__ == '__main__':
   evento =  aviso('Hola mundo' , ['Salir', 'OK', 'Jugar'])
   print(evento)