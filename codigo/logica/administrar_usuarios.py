import os
import json
from codigo.interfaz import configuracion_personalizada

def cargar_usuarios():
    '''
    Retorna una lista de usuarios, con los datos de un archivo JSON o vacía.
    '''
    try:
        directorio_usuarios = os.path.join('guardados', 'usuarios.json')
        with open(directorio_usuarios, 'r') as archivo:
            usuarios = json.load(archivo)
    except:
        usuarios = []
    return usuarios

def guardar_usuarios(usuarios):
    '''
    Almacena en un JSON la lista de usuarios
    '''
    directorio_usuarios = os.path.join('guardados', 'usuarios.json')
    with open(directorio_usuarios, 'w') as archivo:
        json.dump(usuarios, archivo)

def eliminar_partida(partida, usuarios):
    '''
    Recibe como parámetro una partida seleccionada y los usuarios y elimina la partida de dicha lista.
    Luego invoca a guardar_usuarios()
    '''
    usuarios.remove(partida)
    guardar_usuarios(usuarios)
    filename_partida = os.path.join('guardados', f'partida_{partida}')
    if (os.path.isfile(filename_partida)):
        os.remove(filename_partida)
    configuracion_personalizada.eliminar_configuracion(partida)
