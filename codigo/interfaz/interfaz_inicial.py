import PySimpleGUI as sg
import os
import codigo.interfaz.visorAvatar as va
from codigo.logica.jugador import Jugador
import codigo.interfaz.interfaz_puntaje as pun
from codigo.interfaz.tema import *
from codigo.interfaz.ayuda import ayuda
from codigo.interfaz import configuracion_personalizada
from codigo.logica import administrar_usuarios

def check_apodo(apodo):
    '''Evalúa el campo APODO al momento de crear una partida. Los apodos deben tener
    mas de 3 caracteres, no poseer espacios en blanco, caracteres especiales ni
    ser solo números'''

    carEspecial = '!@#$%^&*()[]{};:,./<>?\|`~-=_+'
    if len(apodo) < 3 or len(apodo) > 10:
        return False
    elif (apodo == '') or  (apodo.isspace()== True) or (' ' in apodo):
        return False
    elif apodo.isdigit()==True:
        return False
    for c in apodo:
        if c in carEspecial:
            return False
    return True

def nivel(ventana):
    '''Devuelve el nivel elegido por el usuario según el
    el estado de los elementos "Radio", que se usan en el layout de nueva partida'''
    if ventana.FindElement('rFacil').Get() == True:
        n = "facil"
    elif ventana.FindElement('rMedio').Get() == True:
        n = 'medio'
    elif ventana.FindElement('rDificil').Get() == True:
        n = 'dificil'
    else:
        n = 'personalizado'
    return n

def jugar (avatar, value, ventana):
    '''Crea una instancia del objeto jugador y lo retorna'''
    jugador = Jugador(nombre=value['apodo'], dificultad=nivel(ventana), avatar=avatar)
    return jugador

def actualizar_columnas(ventana, *columna):
    '''Vuelve visible la columna que recibe como parámetro e invisible
    el resto de las columnas. Se utiliza para actualizar la interfaz principal
    según la opción elegida'''
    #Busca en la lista de elementos hasta encontrar una columna
    for e in ventana.element_list():
        if e.Type == 'column':
            #Si la columna está invisible y tiene la key que busco, la hace visible
            if e.Visible == False and e.Key in columna:
                ventana.FindElement(e.Key).update(visible=True)
            elif e.Key in columna:
                ventana.FindElement(e.Key).update(visible=True)
            #Si no, la oculta
            else:
                ventana.FindElement(e.Key).update(visible=False)

def cargando():
    layout=[
        [sg.popup_animated(image_source='blue_blocks.gif', message="Cargando...", alpha_channel=1,time_between_frames=2,no_titlebar=True)],
    ]
    return layout

def nueva_partida(avatar):
    layout = [
        [sg.Text('Apodo:', font=('Italic 24'),key='jugador')],
        [sg.InputText('',size=(20,20),font=('Italic 24'),background_color='#ece6eb',key='apodo')],
        [sg.Frame(
                  layout= [[sg.Radio('Fácil', "dificultad",font=('Italic 24'), default=True, size=(10,3), key='rFacil')],
                          [sg.Radio('Medio', "dificultad",font=('Italic 24'), default=False, size=(10,3), key='rMedio')],
                          [sg.Radio('Difícil', "dificultad",font=('Italic 24'), default=False, size=(10,3), key='rDificil')],
                          [sg.Radio('Personalizado', "dificultad",font=('Italic 24'), default=False, size=(11,3), key='rPersonalizado')]],

                  title='Dificultad' ,title_color='black', relief=sg.RELIEF_SUNKEN,font=('Italic 24'),
                        element_justification='left',key='contenedor'),
         sg.Column(avatar.getAvatarLayout(), visible=False,key='colAvatar')],
        [sg.Button('Jugar', size=(10, 2),button_color=('black','#afad71'),font=('Arial', 18),border_width=1, key='confirmar'),sg.Button('Cancelar', size=(10, 2),font=('Arial', 18),border_width=1,button_color=('black','#afad71'), key='cancelar')],
    ]
    return layout

def jugar_interfaz(img_boton_largo):
    layout = [
        [sg.Button('Nueva Partida',image_filename=img_boton_largo,  border_width=0,font=('Italic 24'),size = (20,3), key='nueva')],
        [sg.Button('Cargar Partida',image_filename=img_boton_largo,  border_width=0,font=('Italic 24'), size=(20,3), key='cargar')],
        [sg.Button('Volver',image_filename=img_boton_largo,  border_width=0,font=('Italic 24'), size=(20,3), key='volver')],
    ]
    return layout

def inicio(img_boton_madera):
    layout = [[sg.Button(image_filename=img_boton_madera, border_width=0,button_text='Ayuda', size=(200, 200), font=('Impact', 40), key='ayuda'),
               sg.Button(image_filename=img_boton_madera, border_width=0, button_text='Jugar', size=(200, 200), font=('Impact', 40),key='jugar'),
               sg.Button(image_filename=img_boton_madera,  border_width=0,button_text='Puntajes', size=(200, 200), font=('Impact', 30),key='puntajes')],
              [sg.Button('Salir', button_color=('black','#f75404'),size=(10, 2),font=('Arial Black', 20),border_width=1, key='salir')]]
    return layout

def interfaz_principal(img_logo, img_boton_largo, img_boton_madera, avatar):
    colInicial = inicio(img_boton_madera)
    columnaCen2 = jugar_interfaz(img_boton_largo)
    columnaNueva = nueva_partida(avatar)
    #Al ejecutarse, sólo será visible la columna inicial
    layout = [
        [sg.Image(filename=img_logo)],
        [sg.Column(colInicial,justification='center',element_justification='center',key= 'colInicial'),
         sg.Column(columnaCen2,visible=False,justification='cener',element_justification='center',key='colJugar2'),
         sg.Column(columnaNueva, visible=False,justification='cener',element_justification='center', key='colPartida'),
        ],
    ]

    return layout

def ventana_carga():
    usuarios = administrar_usuarios.cargar_usuarios()
    #Si canceló la carga o cerró la ventana, retorna un nombre de jugador vacío
    jugador_seleccionado = ''
    if (len(usuarios) == 0):
        aviso('¡No hay ninguna partida guardada!')
        return jugador_seleccionado
    layout = [[sg.Text('Por favor, seleccione la partida que desea cargar: ')],
                [sg.Listbox(usuarios, size=(40, 14), key='listado_partidas')],
                [sg.Button('Confirmar', button_color=('black', '#f75404'), key='confirmar'), sg.Button('Cancelar', button_color=('black', '#f75404'), key='cancelar'), sg.Button('Eliminar', button_color=('black', '#f75404'), key='eliminar')]]
    ventana_carga = sg.Window('Cargar partida', layout)
    ventana_carga.Finalize()
    while True:
        event, values = ventana_carga.read()
        if (event in (None, 'cancelar')):
            break
        if (event == 'confirmar'):
            if (len(values['listado_partidas']) != 0):
                jugador_seleccionado = values['listado_partidas'][0]
                partida_guardada = os.path.join('guardados', f'partida_{jugador_seleccionado}')
                if (os.path.isfile(partida_guardada)):
                    break
                else:
                    jugador_seleccionado = ''
                    aviso('¡La partida ya no existe!')
            else:
                aviso('No ha seleccionado ninguna partida para cargar')
        if (event == 'eliminar'):
            if (len(values['listado_partidas']) != 0):
                decision = aviso('¿Realmente desea eliminar la partida?', ['Sí', 'No'])
                if decision == '_Sí':
                    partida = values['listado_partidas'][0]
                    administrar_usuarios.eliminar_partida(partida, usuarios)
                    ventana_carga['listado_partidas'].Update(usuarios)
                    if ((len(usuarios) == 0)):
                        aviso('El registro de partidas está vacío')
                        break
    ventana_carga.Close()
    return jugador_seleccionado

def lazo_principal():
    #Asigno las rutas de las imagenes a usar.
    #-----------------------------------------------
    directorio_avatares = os.path.join('media','media_ii','avatars', '')
    img_boton_largo =  os.path.join('media','media_ii','botonlargo.png')
    img_boton_madera = os.path.join('media','media_ii','botonMadera.png')
    img_logo = os.path.join('media','media_ii','logo.png')
    #-----------------------------------------------

    #Crea un jugador vacío. Si se cierra la ventana sin comenzar una partida, se retorna al final
    jugador = Jugador('', -1, '')
    avatar = va.Visor(directorio_avatares)

    cargar_partida = False

    ANCHO = 900  # solo de prueba
    ALTO = 700  # solo de prueba
    mi_tema()
    ventana = sg.Window('ScrabbleAr', interfaz_principal(img_logo, img_boton_largo, img_boton_madera, avatar), size = (ANCHO,ALTO),resizable=True,element_justification='center',no_titlebar=False)
    ventana.Finalize()

    while True:
        event, value = ventana.read()

        if (event == None) or (event == 'salir'):
            break
        elif event == 'jugar':
            actualizar_columnas(ventana, 'colJugar2')
        elif event == 'cargar':
            jugador_seleccionado = ventana_carga()
            if (jugador_seleccionado != ''):
                jugador.setNombre(jugador_seleccionado)
                cargar_partida = True
                break
        elif event == 'volver':
            actualizar_columnas(ventana, 'colInicial')
        elif event == 'nueva':
            actualizar_columnas(ventana, 'colPartida','colAvatar')
        elif event == 'cancelar':
            actualizar_columnas(ventana, 'colJugar2')
        elif event == 'confirmar':
            if  check_apodo(ventana.FindElement('apodo').Get()):
                avatarSelec = avatar.getActualRuta()
                decision = aviso(f'¿Confirmar los datos?\nNombre: {value["apodo"]}\nDificultad: {nivel(ventana)}', ['Sí', 'No'])
                if decision == '_Sí':
                    jugador = jugar(avatarSelec, value, ventana)
                    if (jugador.getDificultad() == 'personalizado'):
                        configuracion = configuracion_personalizada.interfaz_personalizacion(jugador.getNombre())
                        if ((len(configuracion) != 0) and (len(configuracion['error']) == 0)):
                            jugador = jugar(avatarSelec, value, ventana)
                            break
                        else:
                            jugador.setNombre('')
                    else:
                        jugador = jugar(avatarSelec, value, ventana)
                        break
            else:
                aviso('Ingrese un apodo válido (debe tener entre 3 y 10 caracteres, puede\nser alfanumerico y no debe contener caracteres especiales)')
        elif event in ('<<<', '>>>'):
            avatarSelec = avatar.controles(event, ventana.FindElement('avatarVisor'))
        elif event == 'puntajes':
            pun.puntajes()
        elif event == 'ayuda':
            ayuda()

    ventana.Close()
    return jugador, cargar_partida

if __name__ == '__main__':
    lazo_principal()
