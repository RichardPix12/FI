##Este módulo contiene las funciones que son utilizadas para recibir los datos
##que se necesitan del jugador, como su nombre, el modo de juego que quiere
##jugar y la cantidad de números que quiere en la lista

def recibe_nombre():
    '''Esta función recibe el nombre del jugador y comprueba si es válido, si
    el nombre no es valido el jugador debera introducir otra vez un nombre '''
    valido = False
    nombre_player = input("Introduzca su nombre -> ")
    while not valido:
        if nombre_player != "":
            valido = True
        else:
            nombre_player = input("Introduzca su nombre -> ")
    return nombre_player

def recibe_modo():
    '''Esta función recibe el modo y comprueba si es correcto, si el modo no
    es correcto el jugador debera volver a introducir el modo que quiere jugar'''
    valido=False
    modo_player = input("Introduzca basic si quiere jugar el modo básico, medium si quiere jugar el modo intermedio o expert si quiere jugar el modo experto -> ")
    while not valido:
        if modo_player == "basic" or modo_player == "medium" or modo_player == "expert":
            valido = True
        else:
            modo_player = input("Introduzca basic si quiere jugar el modo básico, medium si quiere jugar el modo intermedio o expert si quiere jugar el modo experto -> ")
    return modo_player

def recibe_numeros():
    '''Esta función recibe la cantidad de números que quiere el jugador que
    tenga la lista, si el número no es correcto el jugador debera volver a introducir un número '''
    valido=False
    num_player = int(input("Introduzca la cantidad de números (mayor o igual a 6) -> "))
    while not valido:
        if num_player >= 6:
            valido = True
        else:
            num_player = int(input("Introduzca la cantidad de números (mayor o igual a 6) -> "))
    return(num_player)