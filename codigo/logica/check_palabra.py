'''
Versión de check_palabra según última modificación propuesta por la Cátedra.
Se mantiene la valuación de palabras con tilde, puesto que es una mejora en las posibilidades del usuario.
'''

import pattern.es as pes
from pattern.es import verbs, tag, spelling, lexicon
import itertools as it

def posibles_palabras (palabra):
    '''
    Por cada vocal que tenga la palabra seleccionada se genera una posibilidad con Tilde.
    Esto permite resolver el problema que, mientras pattern posee palabras con tilde,
    nuestra aplicación utiliza todas letras sin acentuación. 
    Se genera una lista con posible opciones con tilde para que pattern 
    las encuentre en sus diccionario de palabras.
    '''

    lisPal = []
    #siempre la primer palabra será la ingresada por el jugador
    lisPal.append(palabra)
    vocales = {'a':'á', 'e':'é', 'i':'í', 'o':'ó', 'u':'ú'}
    pos = [idx for idx, x in enumerate(palabra) if x in vocales.keys()]
     #le pongo tilde a esas vocales, y agrego la palabra
    for it in range(len(pos)):
        pal_temp = ''
        for it2 in range(len(palabra)):
            if it2 != pos[it]:
                pal_temp += palabra[it2]
            else:
                pal_temp += vocales[palabra[pos[it]]]
        lisPal.append(pal_temp)
    return lisPal

def clasificar(palabra):
    print(tag(palabra, tokenize=True, encoding='utf-8', tagset='UNIVERSAL'))
    print()

def es_palabra(palabra):
    '''
    Evalua si la palabra recibida existe en los diccionarios de PATTERN.ES
    '''
    ok = True
    if palabra:
        if not palabra.lower() in verbs:
            if not palabra.lower() in spelling:
                if (not (palabra.lower() in lexicon) and not (palabra.upper() in lexicon) and not (
                        palabra.capitalize() in lexicon)):
                        ok = False
                else:
                    print('La encontró en lexicon')
                    clasificar(palabra)
            else:
                print('La encontró en spelling')
                clasificar(palabra)
        else:
            print('La encontró en verbs')
            clasificar(palabra)
    return ok


def check_jugador(palabra, preferencias):
    '''
    Recibe una palabra y verifica que sea un verbo, adjetivo o sustantivo,
    retorna True si es asi, o False en caso contrario.
    Este módulo asignará por defecto la dificultad en FÁCIL si no es indicada
    '''
    
    dificultad = preferencias.getNivel()
    if len(palabra) >= 2:
        global TIPO
        posibles = posibles_palabras(palabra)
        ok = False
        cont = 0
        #en cuanto encuentre una opcion que de 'True' dejara de comprobar e insertará esa
        while (not ok) and (cont < len(posibles)):
            pal = ''
            #La condición debe mantener este orden porque, de otro modo, es_palabra podría ejecutarse
            #en el nivel incorrecto. Si el nivel es difícil, es_palabra imprimirá la misma información 3 veces
            if (dificultad == 'facil') and es_palabra(posibles[cont]):
                pal = pes.parse(posibles[cont]).split('/')
                if pal[1] in TIPO['adj']:
                    ok =True
                elif pal[1] in TIPO['sus']:
                    ok= True
                elif pal[1] in TIPO['verb']:
                   ok= True
            elif (dificultad == 'medio' or  dificultad == 'dificil') and es_palabra(posibles[cont]):
                pal = pes.parse(posibles[cont]).split('/')
                if pal[1] in TIPO['adj']:
                    ok =True
                elif pal[1] in TIPO['verb']:
                   ok= True
            elif (dificultad == 'personalizado') and es_palabra(posibles[cont]):
                pal = pes.parse(posibles[cont]).split('/')
                for tipo_palabra in preferencias.getCategoriasPersonalizadas():
                    if pal[1] in TIPO[tipo_palabra]:
                        ok =True
                        break
            else:
                ok = False
#            print("se chequeo {} el contador es {} y ok esta en {}".format(pal,cont,ok))
            cont += 1
    else:
        return False
    return ok

def check_compu(atril_pc, tablero, preferencias):
    dificultad = preferencias.getNivel()
    fichas_pc = atril_pc.ver_atril()
    letras = ''
    for ficha in fichas_pc:
        letras += list(ficha.keys())[0]
    palabras = set()
    for i in range(2, len(letras)+1):
        palabras.update(map(''.join, it.permutations(letras, i)))
    posibilidades = {}
    for pal in palabras:
        if check_jugador(pal, preferencias):
            fichas_pal = []
            for letra in pal:
                for ficha in fichas_pc:
                    if list(ficha.keys())[0] == letra:
                        #Notar algo importante: A la primera aparición de una ficha que coincida con la letra que busca,
                        #agrega la ficha a la lista. Esto es correcto; sin embargo es conveniente no olvidar que,
                        #si una letra se repitiese y la bolsa contuviese referencias repetidas, se estaría agregando dos veces
                        #la misma ficha a la lista (el mismo diccionario). En usos futuros, si se modificase una, también cambiaría la otra. 
                        #No sucede en la implementación actual, pero es importante tenerlo en cuenta.
                        fichas_pal.append(ficha)
                        break
            busqueda = tablero.buscarEspacio(fichas_pal, preferencias)
            if busqueda['coordenada'] != -1:
                busqueda['fichas'] = fichas_pal
                posibilidades[pal] = busqueda
                #En el modo "facil" y "medio", retorna la primer palabra que pueda validar y encontrarle un espacio.
                #En el modo "personalizado", dependerá de la configuración seleccionada por el usuario.
                if (dificultad == 'facil') or (dificultad == 'medio') or ((dificultad == 'personalizado') and not (preferencias.getIA()['palabra_inteligente'])):
                    return posibilidades[pal], pal
    for clave, valor in posibilidades.items():
        print(clave, ':', valor['interes'])
    print('')
    if len(posibilidades) > 0:
        mejor_opcion = max(posibilidades, key = lambda d: posibilidades[d]['interes'])
        print('La mejor opcion es: ' + mejor_opcion + '. En la coordenada ' + str(posibilidades[mejor_opcion]['coordenada'][0]) + ', ' + str(posibilidades[mejor_opcion]['coordenada'][1]))
        return posibilidades[mejor_opcion], mejor_opcion
    return posibilidades, letras

'''TIPO sera una varible global que nos permite chequear que la palabra a ingresar, este dentro
de las clasificaciones permitidas en el juego adj = adjetivo, sus= sustantivo, verb = verbos.
Las clasificiaciones estan tomadas del modulo pattern, pero la construcción de este modulo facilita su comprobación.
'''
TIPO= {'adj':["AO", "JJ","AQ","DI","DT"],
         'sus':["NC", "NN", "NCS","NCP", "NNS","NP", "NNP","W"],
          'verb':[ "VAG", "VBG", "VAI","VAN", "MD", "VAS" , "VMG" , "VMI", "VB", "VMM" ,"VMN" , "VMP", "VBN","VMS","VSG",  "VSI","VSN", "VSP","VSS"  ]
          }
