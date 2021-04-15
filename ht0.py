'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el 
índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase Tu 
índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado
con dos decimales
'''


Peso = input("¿Cual es su peso en kg?")
Estatura = input("¿Cual es su estatura en m?")

imc = round(float(Peso) / float(Estatura)**2, 2)

print("Su indice de masa corportal es: ", imc)