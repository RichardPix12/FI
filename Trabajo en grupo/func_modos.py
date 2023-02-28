##Este módulo contiene las funciones de los modos, creando una lista con los números
##aleatorios en el rango específico dependiendo del modo elegido por el jugador
##e imprime por pantalla la lista creada

import os
import time
import func_listas

def modo(modo_introducido,cant):
    '''Esta función comprueba si el modo introducido por el jugador es básico,
    intermedio o experto y depende del modo que sea crea una lista con números
    aleatorios en el rango especifico'''
    list = []
    #Si el modo elegido es básico
    #El número aleatorio esta en el rango [0,10]
    if modo_introducido == "basic":
        list=modo_basic(cant)

    #Si el modo elegido es intermedio
    #El número aleatorio esta en el rango [0,100]
    if modo_introducido == "medium":
        list=modo_medium(cant)

    #Si el modo elegido es intermedio
    #El número aleatorio esta en el rango [0,1000]
    if modo_introducido == "expert":
        list=modo_expert(cant)

    return(list)

def modo_basic(cant):
    '''Esta función crea una lista con la números aleatorios en el rango [0,10]
    y de longitud indicada por el jugador'''
    list_basic = func_listas.lista_numeros(list,cant,10)
    print(list_basic)
    time.sleep(cant)
    os.system('cls')
    return(list_basic)

def modo_medium(cant):
    '''Esta función crea una lista con la números aleatorios en el rango [0,100]
    y de longitud indicada por el jugador'''
    list_medium = func_listas.lista_numeros(list,cant,100)
    print(list_medium)
    time.sleep(cant)
    os.system('cls')
    return(list_medium)


def modo_expert(cant):
    '''Esta función crea una lista con la números aleatorios en el rango [0,1000]
    y de longitud indicada por el jugador'''
    list_expert = func_listas.lista_numeros(list,cant,1000)
    print(list_expert)
    time.sleep(cant)
    os.system('cls')
    return(list_expert)
