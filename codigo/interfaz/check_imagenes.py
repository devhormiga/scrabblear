from PIL import Image,ImageDraw,ImageFont
import PySimpleGUI as sg
import time
from codigo.interfaz.tema import*
import os
import errno

def crear_ficha (ficha,directorio):
    '''
    Recibe una ficha y el directorio donde debe estar almacenada y crea la imagen de reemplazo
    '''
    font = ImageFont.truetype("impact.ttf", 20)
    img = Image.new('RGBA', (29,31), (128,64,0,255))
    dibujo = ImageDraw.Draw(img)
    dibujo.text((10, 5), ficha.upper(), 'white', font)
    img.save(f'{directorio}ficha {ficha}.png')
    return img

def crear_especial(esp,directorio):
    '''
    Recibe un casillero y el directorio donde debe estar almacenado y crea la imagen de reemplazo
    '''
    font = ImageFont.truetype("impact.ttf", 20)
    img = Image.new('RGBA', (29,31), (255,128,0,255))
    dibujo = ImageDraw.Draw(img)
    if esp == 'sum':
        dibujo.text((10, 5), '+', 'white', font)
    elif esp == 'rest':
        dibujo.text((10, 5), '-', 'white', font)
    elif esp == 'mult':
        dibujo.text((10, 5), '*2', 'white', font)
    elif esp == 'div':
        dibujo.text((10, 5), '/', 'white', font)
    elif esp == '0':
        img = Image.new('RGBA', (29,31), (255,255,255,0))
        dibujo = ImageDraw.Draw(img)
        dibujo.text((10, 5), '0', 'black', font)
    elif esp == 'orientacionAbajo':
        img = Image.new('RGBA', (29,31), (125,125,125,0))
        dibujo = ImageDraw.Draw(img)
        dibujo.text((10, 5), '=>', 'black', font)
        img = img.rotate (270)
    elif esp == 'orientacionDerecha':
        img = Image.new('RGBA', (29,31), (255,0,255,0))
        dibujo = ImageDraw.Draw(img)
        dibujo.text((10, 5), '=>', 'black', font)
    elif esp == 'orientacion': 
        img = Image.new('RGBA',(29,31),(100,100,100,255))
        dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
        dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
    img.save(f'{directorio}{esp}.png')
    return img

def crear_avatar(av,directorio):
    '''
    Recibe un avatar y el directorio donde debe estar almacenado y crea la imagen de reemplazo
    '''
    img = Image.new('RGBA',(200,200),(100,100,100,255))
    dibujo = ImageDraw.Draw(img)
    dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
    dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
    img.save(f'{directorio}{av}.png')
    return img

def crear_varios(varios,directorio):
    '''
    Recibe una imagen y el directorio donde debe estar almacenado y crea el reemplazo
    '''
    if varios == 'botonlargo':
        img = Image.new('RGBA',(300,100),(100,100,100,255))
    elif varios == 'botonMadera':
        img = Image.new('RGBA',(216,216),(100,100,100,255))
    elif varios == 'logo':
        img = Image.new('RGBA',(780,250),(100,100,100,255))
    elif varios == 'scrabbleArLogo':
        img = Image.new('RGBA',(300,850),(100,100,100,255))
    elif varios == 'puntuaciones2':
        img = Image.new('RGBA',(349,120),(100,100,100,255))
    elif varios == 'pausa':
        img = Image.new('RGBA',(230,70),(100,100,100,255))
    elif varios == 'bolsafichasvacia':
        img = Image.new('RGBA',(100,105),(100,100,100,255))
    elif varios == 'bolsallenaP':
        img = Image.new('RGBA',(100,107),(100,100,100,255))
    elif varios == 'validar':
        img = Image.new('RGBA',(100,100),(100,100,100,255))
    elif varios == 'ayuda':
        img = Image.new('RGBA',(64,80),(100,100,100,255))
    elif varios == 'deshacer':
        img = Image.new('RGBA',(100,107),(100,100,100,255))
    elif varios == 'fullscreen':
        img = Image.new('RGBA', (54,54),(100,100,100,255))
    dibujo = ImageDraw.Draw(img)
    dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
    dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
    img.save(f'{directorio}{varios}.png')
    return img

def crear_ayuda (ay,directorio):
    '''
    Recibe una imagen de ayuda y el directorio donde debe almacenarse y crea una imagen nueva
    '''
    img = Image.new('RGBA', (50,50), (100,100,100,255))
    dibujo = ImageDraw.Draw(img)
    dibujo.line((0, 0) + img.size, fill=(255,0,0,255),width=3)
    dibujo.line((0, img.size[1], img.size[0], 0), fill=(255,0,0,255),width=3)
    img.save(f'{directorio}ayuda {ay}.png')
    return img

def crear_error ():
    '''
    Es invocado si alguna imagen falta para crear una señal que permita saber que hubo problemas en la carga
    '''
    directorio = os.path.join('media', 'media_ii','')
    try:
        img = Image.open(f'{directorio}imagenError.png')
    except:
        img = Image.new('RGBA',(400,20),(79,40,10,255))
        font = ImageFont.truetype("arial.ttf", 12)
        dibujo = ImageDraw.Draw(img)
        dibujo.text((12, 5), 'ALERTA, ALGÚN ARCHIVO DE IMAGEN ESTA DAÑADO O FALTA', 'white', font,align='center')
        img.save(f'{directorio}imagenError.png')
    return img

def check_fichas ():
    fichas=[chr(i) for i in range(ord('a'),ord('z')+1)]
    directorio = os.path.join('media', 'Fichas y espacios', '')
    errores = 0
    for i in range(len(fichas)):
        try:
            img = Image.open (f'{directorio}ficha {fichas[i]}.png')
        except:
            img = crear_ficha(fichas[i],directorio)
            errores += 1
    return errores

def check_ayuda ():
    ayuda = [a for a in range(0,41)]
    directorio = os.path.join ('media','ayuda','')
    errores = 0
    for i in range (len(ayuda)):
        try:
            img = Image.open (f'{directorio}ayuda {ayuda[i]}.png')
        except:
            img = crear_ayuda (ayuda[i],directorio)
            errores += 1
    return errores

def check_especiales ():
    especiales = ['sum','rest','0','div','mult','azul','orientacion','orientacionAbajo','orientacionDerecha']
    directorio = os.path.join('media', 'Fichas y espacios', '')
    errores = 0
    for i in range(len(especiales)):
        try:
            img = Image.open (f'{directorio}{especiales[i]}.png')
        except:
            img = crear_especial(especiales[i],directorio)
            errores += 1
    return errores

def check_avatares():
    avatar = ['avatar1','avatar2','avatar3','avatar4','avatar7','avatar6']
    directorio = os.path.join('media', 'media_ii', 'avatars', '')
    errores = 0
    for i in range (len(avatar)):
        try:
            img = Image.open (f'{directorio}{avatar[i]}.png')
        except:
            img = crear_avatar(avatar[i],directorio)
            errores +=1
    return errores

def check_varios ():
    varios = ['botonlargo','botonMadera','logo','scrabbleArLogo','puntuaciones2','pausa','validar','bolsallenaP','bolsafichasvacia','AYUDA', 'deshacer', 'fullscreen']
    directorio = os.path.join('media', 'media_ii', '')
    errores = 0
    for i in range(len(varios)):
        try:
            img = Image.open (f'{directorio}{varios[i]}.png')
        except:
            img = crear_varios(varios[i], directorio)
            errores += 1
    return errores

def check_directorios():
    '''
    Controla que los directorios de las imágenes sean correctos. En caso negativo, los crea
    '''
    ok = 4
    try:
        os.mkdir('media')
    except OSError as e: #captura el error por si ya está creada la carpeta
        ok -=1
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.makedirs('media/media_ii/avatars')
    except OSError as e: #captura el error por si ya está creada la carpeta
        ok -=1
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.makedirs('media/ayuda')
    except OSError as e:
        ok -=1
        if e.errno != errno.EEXIST:
            raise
    try:    
        os.makedirs('media/Fichas y espacios')
    except OSError as e:
        ok -=1
        if e.errno != errno.EEXIST:
            raise
    return ok

def loading():
    '''
    Este módulo verifica que todas las imágenes, y sus directorios correspondientes, sean correctos.
    En caso negativo, construye reemplazos para evitar el fallo de la app.
    Invoca a los modulos de control (checks) que verifican imagen por imagen si estáne en el directorio
    correspondiente. Retornan o 0 o > 0. Si es 0, no hay errores, si es mayor hay errores.
    '''
    mi_tema()
    img_logo = os.path.join('media', 'media_ii', 'scrabbleArLogo.png')
    contenido = [[sg.Image(img_logo)],
                [sg.Text(font=('Arial',12),size=(20,12),justification='center',key='texto')],
                [sg.Text(font=('Arial',12),size=(15,5),justification='center',key='ok')]
                ]
    v = sg.Window('Loading',layout=contenido,size=(400,400), background_color='#4f280a',element_justification='center', keep_on_top=True, grab_anywhere=True)
    texto = ['Chequeando directorios de imágenes','Chequeando imágenes de fichas','Chequeando imágenes de casilleros especiales',
    'Chequeando imágenes de avatares','Chequeando la ayuda','Chequeando logos y botones','LISTO PARA JUGAR']
    #arma una lista con todos los resultados de los controles para construir los textos que se visualizaran en la interfaz
    chequeos=[]
    dirs, fichas, especiales, avatares,ayuda, varios = check_directorios(), check_fichas(), check_especiales(),check_avatares(),check_ayuda(),check_varios()
    chequeos.append(dirs)
    chequeos.append(fichas)
    chequeos.append(especiales)
    chequeos.append(avatares)
    chequeos.append(ayuda)
    chequeos.append(varios)
    i=0
    while True:
        event, values = v.read(timeout=10)
        if i < 7:
            v['texto'].update('{}'.format(texto[i]))
            try:
                if str(chequeos[i]) > '0':
                    if i == 0:
                        v['ok'].update('Cuidado, tienes algún directorio dañado')
                    else:
                        v['ok'].update('Cuidado, tienes imágenes dañadas')
                    img2 = crear_error()
                else:
                    v['ok'].update('Correctas')
            except:
                pass
            i += 1
            time.sleep(0.5)
        else:
            v['texto'].update('{}'.format(texto[-1]))
            time.sleep(0.5)
            break
    v.close()
if __name__ == '__main__':
    loading()
