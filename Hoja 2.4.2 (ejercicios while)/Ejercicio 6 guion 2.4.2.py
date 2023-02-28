
#EJERCICIO 6, HOJA 2.4.2

a=int(input("Escribe el primer número >= 0"))
n1=a
while n1<0:
    n1=int(input("Escribe el primer número >= 0"))

b=int(input("Escribe el segundo número > 0"))
n2=b
while n2<=0:
    n2=int(input("Escribe el segundo número >= 0"))

cociente=n1//n2
resto=n1%n2

print("Cociente: ",n1, " // ",n2, " = ",cociente)
print("Resto: ",n1, " % ",n2, " = ",resto )




