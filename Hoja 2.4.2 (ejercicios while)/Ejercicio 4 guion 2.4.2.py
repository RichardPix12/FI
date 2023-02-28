
#EJERCICIO 4 HOJA 2.4.2

n=int(input("Escribe un número: "))
i=n
contadorpar = 0
sumapar = 0;
contadorimpar = 0
sumaimpar = 0;

while i >=0:
    if i%2==0:
        sumapar = sumapar + i
        contadorpar = contadorpar + 1
    else:
        sumaimpar = sumaimpar + i
        contadorimpar = contadorimpar + 1
    i=int(input("Escribe un número: "))



mediapar = sumapar/contadorpar
mediaimpar = sumaimpar/contadorimpar
print("La media aritmética par es: ", mediapar)
print("La media aritmética impar es: ", mediaimpar)
