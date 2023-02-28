##Este módulo contiene las funciones que contienen información, como pueden ser
##las reglas, lo que se imprime por pantalla antes de que el juego comience e
##información básica como los creadores del juego

import time

def reglas():
    '''Esta función guarda las reglas del juego en varias variables y luego las
    imprime por pantalla junto con la información básica y el inicio de juego'''
    regla_1 = "El juego consiste en memorizar los números de la lista que sale por pantalla y luego introducirlos en el orden mostrado y correctamente para obtener la puntuación\n"
    regla_2 = "El jugador podra elegir la cantidad de números que van a salir por pantalla, pero como mínimo tienen que ser 6\n"
    regla_3 = "En este juego hay tres modos a elegir, el básico, el intermedio y el experto\n"
    regla_4 = "En el modo básico los números están en el rango [0,10] y la puntuación será de 20 puntos por cada acierto\n"
    regla_5 = "En el modo intermedio los números están en el rango [0,100] la puntuación será de 50 puntos por cada acierto\n"
    regla_6 = "En el modo experto los números están en el rango [0,1000] y la puntuación será de 100 puntos por cada acierto\n"
    print_informacion()
    time.sleep(1)
    print(regla_1)
    time.sleep(1)
    print(regla_2)
    time.sleep(1)
    print(regla_3)
    time.sleep(1)
    print(regla_4)
    time.sleep(1)
    print(regla_5)
    time.sleep(1)
    print(regla_6)
    time.sleep(1)
    print_inicio()

def print_inicio():
    '''Esta función imprime por pantalla el inicio del juego'''
    print("Dicho esto\n")
    time.sleep(1)
    print("¡Empecemos!\n")

def print_informacion():
    '''Esta función imprime por pantalla  los nombres de
    los creadores del juego y el inicio de las reglas '''
    print("Juego de memoria\n")
    time.sleep(2)
    print("Este juego ha sido creado por Ricardo Marques Garay, Drisse Bouregaa Fuertes y Sonia Moro Lauda\n")
    time.sleep(5)
    print("A continuación le vamos a explicar en que consiste el juego y sus reglas\n")