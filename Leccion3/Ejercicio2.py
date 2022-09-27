#Ejercicio 2

N = int(input("Introduce un número: "))
suma = 0
for i in range(1, N+1):
    suma += i
print("La suma de los números del 1 al {} es {}".format(N, suma))