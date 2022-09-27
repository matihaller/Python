# Ejercicio 10: No repetir caracteres.
# Hacer un programa que pida una cadena por teclado, luego
# meter los caracteres en una lista sin repetir caracteres 

cadena = input("Digite su cadena: ")
lista = []
for i in cadena:
    if i not in lista: # Si el caracter aun no está en la lista
        lista.append(i) # los agregamos a la lista
print(f'\nLista sin repetir ninguno: \n{lista}')

