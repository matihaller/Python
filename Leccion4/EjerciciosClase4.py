#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a 
#continuacion elimine los elementos repetidos, por ultimo
#mostrar la lista.

lista = [1, 2, 3, "Mati", 7, 7, 3, "Messi", 5, "Mati"]
#repes = set(lista)
# print(repes)
#lista = list(repes)
lista = list(set(lista)) #Conversion hecha en una linea full eficiente
print(lista)