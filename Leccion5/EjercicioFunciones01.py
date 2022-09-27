# Ejercicio 1: crear una funcion para sumar los valores 
# recibidos de tipo numericos, utilizando argumentos 
# variables *args como parametros de la funcion y agregar 
# como resultado la suma de todos los valores pasados 
# como argumentos
#Definimos una funcion
def sumar_valor(*args): # recibimos una cantidad de parametros indefinidos
    resultado = 0
    # iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado
# llamamos a la funcion
print(sumar_valor(3,5,9,2,1,5,6,9,8,4,2,3,4,5))

