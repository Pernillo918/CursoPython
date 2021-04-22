'''
Ejercicio1
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo, de altura el número introducido.
Ejemplo 
El usuario ingresa el numero 5
*
**
***
****
*****
'''

print("")
print("Bienvendio al programa, este es el Ejercicio 1")
print("")
numero = int(input("Digite un numero:"))

if (numero >=0):

    for i in range(numero):
        for j in range(i+1):
            print("*", end="")
        print()
else:
    print("El numero ingresado no es un numero entero positivo")



'''
Ejercicio2
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es
 un número primo o no.

'''
print("")
print("Bienvendio al programa, este es el Ejercicio2")
print("")
numero = int(input("Digite un numero:"))


validacion=0
if numero>1:
    for i in range(2, numero):

        calculo= numero
        calculo=calculo%i

        if calculo==0:

            validacion+=1

    if validacion== 0:

        print("El numero "+str(numero)+" es primo")

    else:

        print("El numero " +str(numero) + " no es primo")

else:

    print("El numero digitado no es entero positivo")
