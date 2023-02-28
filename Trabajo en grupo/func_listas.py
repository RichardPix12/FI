##Este módulo contiene la función que crea la lista correspondiente y otra función
##que comprueba si las listas son iguales

import random

def lista_numeros(lista,cantidad,max):
    '''Esta función crea una lista de números random en el rango indicado y su longitud
    sera la indicada por el parámetro'''
    lista = []*cantidad
    while cantidad > 0:
        lista.append(random.randint(0,max))
        cantidad = cantidad - 1
    return lista

def aciertos_listas(lista_a, lista_b):
    '''Esta función comprueba si las listas pasadas como parámetros son iguales
    elemento a elemento'''
    aciertos=0
    if len(lista_a) != len(lista_b):
        return False

    for i in range(0,len(lista_a)):
        if(lista_a[i]  == lista_b[i]):
            aciertos=aciertos+1
    return aciertos
