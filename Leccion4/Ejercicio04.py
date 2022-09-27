# Ejercicio 4: Sumar números pares dentro de un rango
# hacer un programa para sumar números pares dentro
# de un rango, por ej:
#                       suma de num pares del 2 al 30
#                       suma = 240

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde va a llegar a sumar: "))
suma = 0
for  i in range(a,b+1):
    if i % 2 == 0: # esto es si el numero es par
        suma += i
print(f"\nLa suma de numeros pares dentro del rango es: {suma}")
