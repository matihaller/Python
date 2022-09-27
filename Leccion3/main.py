# Ciclo while (mientras o durante)
"""
contador = 0
while contador < 15:
    print('ejecutamos el ciclo while', contador)
    contador += 1
else:
    print('fin del ciclo while')
"""
# ejercicio 1: imprimir numeros del 0 al 5
"""
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1
"""
"""
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
"""
# ciclo for (para)
# iterar es recorrer un elemento de un conjunto de datos
# cadena es un arreglo de caracteres
"""
cadena = 'me gusta messi'
for letra in cadena:
    print(letra)
else:
    print('fin del ciclo for')
"""
# palabra break (sirve para romper todo tipo de estructur al encontrar el elemento que se estaba buscando)
"""
for letra in 'Alemania':
    if letra == 'a':
        print(f'letra encontrada: {letra}')
        break
else:
    print('fin del ciclo for')
"""
# palabra resevada continue

for i in range(8):
    if i % 2 == 0:
        print(f'valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'valor: {i}')

