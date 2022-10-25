# Ejercicio 1: crear una funcion para sumar los valores 
# recibidos de tipo numericos, utilizando argumentos 
# variables *args como parametros de la funcion y agregar 
# como resultado la suma de todos los valores pasados 
# como argumentos
#Definimos una funcion
'''
def sumar_valor(*args):
    resultado = 0
    
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3,5,6,9))
'''
