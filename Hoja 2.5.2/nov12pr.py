from nov3 import *


#Ej.1 hoja 2.5.2

def fac(n):
    """Recibe un entero >=1(precondición) y retorna su factorial"""
    f=1
    for i in range (1,n//2+1):
        f=f*i
    return f

#Ej.2 y Ej.3 hoja 2.5.2

def sumaDiv(n):
    """Recibe un n>=2 y devuelve la suma
     de sus divisores en el rango [1.. n-1]"""
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i
    return s

def perfecto(m):
    return m==sumaDiv(m)

def listaPerfertos(u):
    """Recibe u>=2 e
    Imprime los perfectos que haya  en el rango [2..u]"""
    for i in range(2,u+1):
        if perfecto(i):
            print(i, end="/")

#Ej 4 hoja 2.5.2

def es_primo(n):
    """Recibe un número >=1 que devuelva True si el numero es primo o False
    si no lo es """
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
#lectura anticipada

def print_primo(x):
    while x>1:
        if es_primo(x):
            print("El numero",x,"ES PRIMO")
        else:
            print("El numero",x,"NO ES PRIMO")
        x= leerEntero1()

print_primo(leerEntero2(1))