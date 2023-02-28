#Ejercicio 6 hoja if

x1 = int(input("Primera nota (0-100): "))
x2 = int(input("Segunda nota (0-100): "))
x3 = int(input("Tercera nota (0-100): "))
x4 = int(input("Cuarta nota (0-100): "))

media = (x1+x2+x3+x4)/4

if media>=90 and media<=100:
    print("A")
if media>=80 and media<90:
    print("B")
if media>=70 and media<=80:
    print("C")
if media>=60 and media<=70:
    print("D")
if media>=0 and media<=60:
    print("E")






