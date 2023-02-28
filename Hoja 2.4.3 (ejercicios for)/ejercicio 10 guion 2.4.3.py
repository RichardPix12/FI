
#EJERCICIO 10 HOJA 2.4.3


a=-1
while a<0:
    a=int(input("Primer factor: "))

b=-1
while b<0:
    b=int(input("Segundo factor: "))

p1=a*b
print(p1)

total = 0

for i in range(b):
    total = total + a

print ("El resultado de la multiplicacion es",total)
