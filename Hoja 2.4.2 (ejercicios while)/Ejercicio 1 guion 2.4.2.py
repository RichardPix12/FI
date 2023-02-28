#EJERCICIO 1, HOJA 2.4.2

n=(input("Introduce los caracteres: "))
i = n
contador = 0
while i != '.':
    if i == "a":
        contador = contador +1
    i=(input("Introduce los caracteres: "))

print("Se ha introducido el caracter 'a' durante: ", contador ," veces")