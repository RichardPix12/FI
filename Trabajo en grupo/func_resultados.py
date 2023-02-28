##Este módulo contiene las funciones que calculan los resultados, dependiendo del modo
##y el resultado del jugador hara una cosa u otra
##Si el jugador gana el juego se imprime un mensaje de enhorabuena y se modifica
##el fichero añadiendo el nombre del jugador, sus puntos y la fecha y hora del juego
##Si el jugador pierde se imprime un mensaje diciendole que no ha acertado y se
##modifica el fichero añadiendo el nombre del jugador, una frase diciendo que no ha
##acertado y la fecha del juego

from datetime import datetime
import func_listas
import func_modos
import func_fichero
import func_datos


def resultado(modo,cant,nombre_player,lista):
    '''Esta función crea una lista en la que el jugador introduce los números que cree correctos,
    comprueba si las listas son iguales, y si lo son añade en el fichero el nombre introducido por la persona, sus puntos
    y la fecha del juego'''

    list_player = []
    while len(list_player) != cant:
        number = int(input("Introducza los números uno a uno que cree que estaban en la lista uno por uno (en orden) -> "))
        list_player.append(number)

    #Si el modo es básico
    if modo == "basic":
     puntos=20
     resultado_basic(list_player,puntos,nombre_player,lista)

    #Si el modo es intermedio
    if modo == "medium":
     puntos=50
     resultado_medio(list_player,puntos,nombre_player,lista)

     #Si el modo es experto
    if modo == "expert":
     puntos=100
     resultado_expert(list_player,puntos,nombre_player,lista)

def resultado_basic(list_player,puntos,nombre_player,lista):
    '''Esta función comprueba si el resultado de la comparación de las lista en el
    modo básico es correcto o no'''
    aciertos= func_listas.aciertos_listas(list_player,lista)
    if aciertos == 0:
        resultado_basic_bad(nombre_player)
    else:
        resultado_basic_good(list_player,puntos,nombre_player,aciertos,lista)

def resultado_basic_good(list_player,puntos,nombre_player,aciertos,lista):
    '''Esta función imprime por pantalla un mensaje diciendo al jugador que ha
    acertado y las listas, añade los puntos del usuario e imprime por pantalla
    los puntos del jugador. También modifica el fichero en el cuál se añade el
    nombre del jugador, su puntuación y el fecha y hora del juego '''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Has acertado", aciertos )
    print(list_player,lista)
    puntos = puntos * aciertos
    print("Tu resultado final es:",puntos,"puntos")
    write_1 = str("\n\nLa puntuación de " + nombre_player + " es ")
    write_2 = str(puntos) + " puntos.\n"
    write_3 = "El día y la hora del juego -> " + dt_string + "."
    write = write_1 + write_2 + write_3
    func_fichero.modificar_fichero("Puntuaciones.txt",write)

def resultado_basic_bad(nombre_player):
    ''' Esta función imprime por pantalla un mensaje diciendo al jugador que no ha acertado
    y modifica el fichero con la información de que el jugador no ha acertado y
    la fecha del juego'''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Parece que no has acertado")
    write_1 = "\n\nParece que el jugador " + nombre_player + " no ha acertado. "
    write_2 = "\n"
    write_3 = "El día y la hora del juego -> " + dt_string + "."
    write = write_1 + write_2 + write_3
    func_fichero.modificar_fichero("Puntuaciones.txt",write)

def resultado_medio(list_player,puntos,nombre_player,lista):
    '''Esta función comprueba si el resultado de la comparación de las lista en el
    modo intermedio es correcto o no'''
    aciertos= func_listas.aciertos_listas(list_player,lista)
    if aciertos == 0:
        resultado_medio_bad(nombre_player)
    else:
        resultado_medio_good(list_player,puntos,nombre_player,aciertos,lista)

def resultado_medio_good(list_player,puntos,nombre_player,aciertos,lista):
    '''Esta función imprime por pantalla un mensaje diciendo al jugador que ha
    acertado y las listas, añade los puntos del usuario e imprime por pantalla
    los puntos del jugador. También modifica el fichero en el cuál se añade el
    nombre del jugador, su puntuación y el fecha y hora del juego '''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Has acertado",aciertos)
    print(list_player,lista)
    puntos = puntos * aciertos
    print("Tu resultado final es:",puntos,"puntos")
    write_1 = str("\n\nLa puntuación de " + nombre_player + " es ")
    write_2 = str(puntos) + " puntos\n"
    write_3 = "El día y la hora del juego -> " + dt_string + "."
    write = write_1 + write_2 + write_3
    func_fichero.modificar_fichero("Puntuaciones.txt",write)

def resultado_medio_bad(nombre_player):
    ''' Esta función imprime por pantalla un mensaje diciendo al jugador que no ha acertado
    y modifica el fichero con la información de que el jugador no ha acertado y
    la fecha del juego'''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Parece que no has acertado")
    write_1 = "\n\nParece que el jugador " + nombre_player + " no ha acertado. "
    write_2 = "\n"
    write_3 = "El día y la hora del juego -> " + dt_string + "."
    write = write_1 + write_2 + write_3
    func_fichero.modificar_fichero("Puntuaciones.txt",write)

def resultado_expert(list_player,puntos,nombre_player,lista):
    '''Esta función comprueba si el resultado de la comparación de las lista en el
    modo experto es correcto o no'''
    aciertos= func_listas.aciertos_listas(list_player,lista)
    if aciertos == 0:
        resultado_expert_bad(nombre_player)
    else:
        resultado_basic_good(list_player,puntos,nombre_player,aciertos,lista)

def resultado_expert_good(list_player,puntos,nombre_player,aciertos,lista):
    '''Esta función imprime por pantalla un mensaje diciendo al jugador que ha
    acertado y las listas, añade los puntos del usuario e imprime por pantalla
    los puntos del jugador. También modifica el fichero en el cuál se añade el
    nombre del jugador, su puntuación y el fecha y hora del juego '''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Has acertado",aciertos)
    print(list_player,lista)
    puntos = puntos * aciertos
    print("Tu resultado final es:",puntos,"puntos")
    write_1 = str("\n\nLa puntuación de " + nombre_player + " es ")
    write_2 = str(puntos) + " puntos\n"
    write_3 = "El día y la hora del juego -> " + dt_string + "."
    write = write_1 + write_2 + write_3
    func_fichero.modificar_fichero("Puntuaciones.txt",write)

def resultado_expert_bad(nombre_player):
    ''' Esta función imprime por pantalla un mensaje diciendo al jugador que no ha acertado
    y modifica el fichero con la información de que el jugador no ha acertado y
    la fecha del juego'''
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Parece que no has acertado")
    write_1 = "\n\nParece que el jugador " + nombre_player + " no ha acertado. "
    write_2 = "\n"
    write_3 = "El día y la hora del juego -> " + dt_string + "."
    write = write_1 + write_2 + write_3
    func_fichero.modificar_fichero("Puntuaciones.txt",write)