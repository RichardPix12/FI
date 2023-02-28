

# EJERCICIO 12 HOJA 2.4.3

n=1
while n<2:
    n=int(input("Entero >=2? "))

s=0

for i in range(1,n):
    if n%i==0:
        s=s+i
        #print(i, end="*")

#print(" SUMA=",s)
print("El numero",n,"es",end=" ")
if s>n:
    print("abundante")
elif s==n:
    print("perfecto")
else:
    print("defectivo y", end=" ")
    if s==1:
        print("primo")
    else:
        print("no primo")