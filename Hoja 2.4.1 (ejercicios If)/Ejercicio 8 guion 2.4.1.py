#Ejercicio 8 hoja IF

año = int(input("Elige un año: "))
mes = int(input("Elige un mes (1-12): "))



#Año bisiesto
if año%4==0 and año%100==0 and año%400==0 and mes==2:
    print("El año ",año, " es bisiesto ya que es divisible por 4 por 100 y por 400")
    print("El mes tiene 29 dias")
elif año%4==0 and año%100==0 and año%400==0 and mes!=2:
    print("El año ",año, " es bisiesto ya que es divisible por 4 por 100 y por 400")
    print("El mes tiene 30 dias")

#Año no bisiesto
elif año%4==0 and año%100==0 and año%400!=0 and mes==2:
    print("El año ",año, " no es bisiesto ya que es divisible por 4 por 100 y no por 400")
    print("El mes tiene 28 dias")
elif año%4==0 and año%100==0 and año%400!=0 and mes!=2:
    print("El año ",año, " no es bisiesto ya que es divisible por 4 por 100 y no por 400")
    print("El mes tiene 30 dias")

#Año bisiesto
elif año%4==0 and año%100!=0 and mes==2 :
    print("El año ",año, " es bisiesto ya que es divisible por 4 y no divisible por 100")
    print("El mes tiene 29 dias")
elif año%4==0 and año%100!=0 and mes!=2 :
    print("El año ",año, " es bisiesto ya que es divisible por 4 y no divisible por 100")
    print("El mes tiene 30 dias")

#Año bisiesto
elif año%4==0 and mes==2:
    print("El año ",año, " es bisiesto ya que es divisible por 4")
    print("El mes tiene 29 dias")
elif año%4==0 and mes!=2:
    print("El año ",año, " es bisiesto ya que es divisible por 4")
    print("El mes tiene 29 dias")

#Año no bisiesto
elif año%4==0 and mes==2:
    print("El año ",año, " no es bisiesto ya que es divisible por 4")
    print("El mes tiene 28 dias")
else:
    print("El año ",año, " no es bisiesto ya que no es divisible por 4")
    print("El mes tiene 30 dias")