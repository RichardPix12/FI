

#EJERCICIO 13 HOJA 2.4.3

n=2
while n<3:
    n=int(input("Hasta que orden quieres calcular >=3 "))
x=3
y=0
z=2

print (x,y,z,sep="*",end="*")

for i in range(3,n+1):
    per = x+y
    print(per,end="*")
    x=y
    y=z
    z=per

