
#EJERCICIO 3 HOJA 2.4.2

n=int(input("Escribe un número: "))
i=n
contador = 0
suma = 0;

while i >=0:
    suma = suma + i
    contador = contador + 1
    i=int(input("Escribe un número: "))

media = suma/contador
print("La media aritmética es: ", media)
