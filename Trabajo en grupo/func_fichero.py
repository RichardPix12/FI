##Este módulo contiene la función que modifica el fichero

def modificar_fichero(nombre,escritura):
    '''Esta función modifica el fichero'''
    f = open(nombre,"a")
    f.write(escritura)
    f.close()
