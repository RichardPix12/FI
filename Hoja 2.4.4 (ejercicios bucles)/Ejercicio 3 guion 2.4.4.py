
#Ejercicio 3 hoja 2.4.4

m=0
while m<=0:
    m=int(input("Filas >=1? "))

n=0
while n<=0:
    n=int(input("columnas >=1? "))

for i in range(1,m+1):
    for j in range(1,n+1):
        print("A",i,j,sep="", end =" ")
    print()

