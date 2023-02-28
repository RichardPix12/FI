
#EJERCICIO 7 HOJA 2.4.2

a=int(input("Escribe un número: "))

n=a

contador = 0
numero = 0
contadorfinal = 0


while n!=0:
    if n>0:
        if(n>numero):
            numero = n
            contador = contador+1
            contadorfinal = contador
            n=int(input("Escribe un número: "))
        else:
            contador = contador+1
            n=int(input("Escribe un número: "))
    else:
        n=int(input("Escribe un número: "))

print("El mator número es ", numero, " y se proporcionó en la posicion",
contadorfinal)




