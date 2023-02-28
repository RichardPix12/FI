##Este módulo inicializa el juego

import func_datos
import func_modos
import func_resultados
import func_informacion

def main():
    func_informacion.reglas()
    nombre_player = func_datos.recibe_nombre()
    modo_player = func_datos.recibe_modo()
    cant = func_datos.recibe_numeros()
    list=func_modos.modo(modo_player,cant)
    func_resultados.resultado(modo_player,cant,nombre_player,list)
main()