'''
Ejercicio1
Escribir un programa que almacene una cadena de caracteres de  contraseña en una variable,
ingresada por el usuario, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin tener en 
cuenta mayúsculas y minúsculas.

'''


print("Binevenido este es el primer ejercicio")
x= str(input("Ingrese su contraseña: "))
y= str(input("Ingrese de nuevo su contraseña: "))

if x == y:
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")



'''
Ejercicio2
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


'''

print("")
print("")
print("Bienvenido este es el segundo ejercico")
x = str(input("Ingresa tu nombre: "))
y = str(input("Sexo H o M: ")) 
if y == "M" or y == "m":
        if x.lower() < "m":
            print("Usted se encuentra en el grupo A")
        else:
            print("Usted se encuentra en el grupo B")
else:
    if y == "H" or y == "h":
        if x.lower() >"n":
            print("Usted se encuentra en el grupo A")
        else:
            print("Usted se encuentra en el grupo B")