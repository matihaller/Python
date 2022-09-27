# Ejercicio 7: Juego adivina el número
# Realizar un juego para adivinar un número. Para ello 
# se debe generar un número aleatorio entre 1 - 100, 
# y luego ir pidiendo números indicando "es mayor" o 
# "es menor" según sea mayor o menor con respecto a N. 
# El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos.

import random
print("\t.:ADIVINA EL NÚMERO:.")
aleatorio = random.randint(0, 100) # toma de 0 a 100 un numero al azar
contador = 0
while True:
    numero = int(input("Digite un número de 0 a 100: "))
    contador += 1
    if numero > aleatorio:
        print("\tDigite un número más bajo: ")
    elif numero < aleatorio:
        print("\tDigite un numero más alto: ")
    else:
        print(f"¡FELICITACIONES! ADIVINASTE EL NÚMERO {numero}")
        break #rompemos el cicLO
print(f"\nNúmero de intentos: {contador}")
