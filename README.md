![Logo](https://raw.githubusercontent.com/enzodiaz25/Scrabble/master/media/media_ii/logo.png)

ScrabbleAR es un proyecto realizado para el Seminario de Lenguaje Python.

Fue realizado por:

Diego Vilardebó (quien además diseñó las imagenes para el proyecto) - https://github.com/elrecursante -

Enzo Diaz - https://github.com/enzodiaz25 -

Ivan Knopoff - https://github.com/Ivanknop - ivan.knopoff@gmail.com

--------------------------------
:video_game: Sobre la Licencia  de ScrabbleAR (Open Source)

Para el proyecto hemos analizado los tipos de licencia que ofrecen la Free Sofware Foundation (FSF) y la Open Source Initiative (OSI). Hemos erradicado la idea de licencias con copyright ya que estamos en un contexto académico, por lo tanto consideramos que en dicho contexto toda investigación y desarrollo de proyectos debería ser de libre acceso y distribución, para fomentar y aportar dicho conocimiento a la comunidad por más infimo que este sea.

Si bien la licencia propuesta por la FSF es una definición filosofica, etica y moral atractiva y tentadora sobre las libertades del software para el usuario y la comunidad, hemos tenido que inclinarnos a la propuesta por la OSI.

El motivo de este es uno solo: 

Las pautas del trabajo final, propuestas por la cátedra de Seminario de Lenguaje en Python, plantean como requisito obligatorio que ScrableAR funcione tanto en Linux como en Winows (entendiendo que apunta a que nuestro proyecto sea ejecutado sin ningun problema no importando la plataforma), pero tratándose de Winows (un sistema operativo comercial y privativo) estaríamos contradiciendo las bases de la FSF.

Es por este motivo que ScrabbleAR es OPEN SOURCE  


Sobre las imagenes utilizadas en el proyecto 

En cambio, al momento de hablar de las imagenes utilizadas para el proyecto (exceptuando los avatares) éstas han sido creadas por Diego Vilardebó especificamente para ScrabbleAR. Con el objetivo de seguir en la logica del Open Source el autor a decidido protegerlas meiante la licencia:

Creatives Commons  en calidad : Reconocimiento – NoComercial – CompartirIgual (by-nc-sa)

Reconocimiento – NoComercial – CompartirIgual (by-nc-sa): No se permite el uso comercial de la obra original ni obras derivadas. Estas obras derivadas deben distribuirse con una licencia igual que la que tiene la original.
--------------------------------

![Intefaz de juego - Modo fácil](https://raw.githubusercontent.com/enzodiaz25/Scrabble/master/media/ayuda/ayuda%2014.png)

:video_game: ScrabbleAR simula una aplicación donde el usuario/jugador debe enfrentarse a la computadora. El objetivo del juego es obtener la mayor cantidad de puntos posibles colocando las palabras en horizontal o vertical; pero sin cruzarse ninguna palabra entre sí. Pueden escogerse entre tres dificultades -Fácil, Medio, Difícil- o configurar directamente la partida y la dificultad.

Se requiere de las librerías:

PySIMPLEGUI 4.18.2

Pillow 7.1.2

Pattern 3.6


Se recomienda ejecutar en Python 3.6.10 o anterior por un problema entre el mismo y la librería Pattern.


Dinámica del juego:
1) Se determina al azar quién empieza.
2) El jugador selecciona la mejor combinación de palabras posibles y la inserta en el tablero. En este hay casilleros ordinarios y otros especiales que alteran el puntaje final de la palabra insertada. En el caso del computador, la selección de la palabra y del lugar del tablero está determinado por el algoritmo de dificultad.
3) Una vez seleccionadas las letras se corrobora que sea una palabra válida.
4) En caso afirmativo, se decide dónde insertar y la orientación. Si hay lugar -es decir que la palabra no termina fuera del tablero ni se cruza con alguna letra de otra palabra-, se inserta y se incrementa el puntaje total.
5) En caso negativo, se debe seleccionar otra combinación de letras.
6) El Usuario/Jugador dispone de 3 (tres) cambios de sus fichas antes de tener que dar por terminada la partida.
