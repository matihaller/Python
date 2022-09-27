# Eiercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga 2 listas y que a continuación 
# cree las siguientes listas (en las que no deben haber repetición)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas.


lista1 = [1, 2, 3, 4, 5, 4, 3, 2, 2, 1, 5]
lista2 = [4, 5, 6, 7, 8, 4, 5, 6, 7, 7, 8]
print(f"Lista de palabras que aparecen en las listas {lista1 + lista2}")

conj1 = set(lista1)
conj2 = set(lista2)

punto2 = list(conj1 - conj2)
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda {punto2}")

punto3 = list(conj2 - conj1)
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera {punto3}")

punto4 = (conj2 & conj1)
print(f"lista de palabras que aparecen en ambas listas. {punto4}")