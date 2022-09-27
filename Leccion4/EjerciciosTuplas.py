import math
#Dada la siguiente tupla
#Crear una lista que solo incluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)

lista = [] # defino la lista

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Ejercicio matematicas
#sacar raiz cuadrada
numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error, numero negativo')
    numero =int(input('Digite un numero positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f} ')