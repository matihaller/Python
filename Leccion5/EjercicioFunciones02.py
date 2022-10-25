# Ejercicio 2:Función * con args para multiplicar.
# Crear una funcion para multiplicar los valores
# recibidos de tipo numerico, utilizando argumentos 
# variables *args como parámetro de la funcion y 
# regresar como resultado la multiplicación de todos 
# los valores pasados como argumento.

def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado
print(multiplicar(2,5,6))
