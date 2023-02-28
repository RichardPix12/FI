
#EJERCICIO 5 GUIÓN IF

x=int(input("ENTERO?"))
print("Elija la opción deseada")
print("a si quieres cuadrado")
print("b si quieres el cubo")
print("c si quieres doble")
op=input("META LETRA SEGÚN MENU")
if op == "a" or op == "A":
    print("El cuadrado de ", x, " es ", x**2)
elif op == "b" or op == "B":
    print("El cubo de ", x, " es ", x**3)
elif op == "c" or op == "":
    print("El doble de ", x, " es ", x*2)
else:
    print("OPCIÓN NO VALIDA")