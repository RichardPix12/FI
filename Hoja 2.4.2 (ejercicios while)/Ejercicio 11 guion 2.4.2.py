
#EJERCICIO 11 HOJA 2.4.2

# Pasar base 10 a base 2

# 18 en base 10 es 10010 en base 2

n=-1

while n<=-1:
    n=int(input("entero >=0: "))

if n==0:
    res = 0

m=n
res=""
while n>0:
    if n%2 ==0:
        res = "0"+res
    else:
        res = "1"+res
    n=n//2

print(m,"es en base 2", res)


