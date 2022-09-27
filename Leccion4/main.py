# Colecciones
# lista = nombres (string) se puede tener cualquier elemento
'''
nombres = ['Mati', 'Messi', 'CR7']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
'''
from traceback import print_tb


nombres = ['Mati', 'Messi', 'CR7', 'Ney']
print(nombres)
print(nombres[0:2]) # solo muestra el indice 0 y 1
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])
#desde el indice indicado hasta el final
print(nombres[1: ]) 
#modificamos un valor
nombres[3] = 'Neymar'
nombres[0] = 'Matias'
print(nombres)
#iterar una lista
for nombre in nombres: #nombre singular, lista plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')

#preguntamos cuantos elementos tiene una lista
print(len(nombres))

#agregamos un elemento
nombres.append('Naruto')
print(nombres)

#insertar un elemento en un indice especifico
nombres.insert(0, 'Goku')
print(nombres)
nombres.insert(3, 'matipro')
print(nombres)
'''
nombres[2] = 'tango'
print(nombres)
'''
#eliminamos un elemento
nombres.remove('matipro')
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar indice especifico
del nombres[2]
print(nombres)

#eliminar todos los elementos
nombres.clear()
print(nombres)

#eliminar la lista
del nombres
#print(nombres)

#Tuplas
#Definimos una tupla
cocina = ('cuchara', 'tenedor', 'cuchillo') # en las tuplas no se usan corchetes como en las listas
print(len(cocina)) #nos muestra la cantidad de elementos que hay

#   Acceder a un elemento, para esto utilizamos corchetes
print(cocina[1])
#manera inversa
print(cocina[-1])

# acceder a un rango
print(cocina[0:2])
#ejemplo
verduras = ('papa',) #necesita la coma para que sea una tupla y no una cadena

#elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') #print sta usando \n para saltos de linea, puse end para que no haga saltos de linea

cocinalista = list(cocina)
cocinalista[0] = 'plato'
cocina = tuple(cocinalista)
print('\n', cocina)
#no es recomendable hacer esto
#si necesitamos modificar nuestro programa lo pasamos a lista
#pero evitamos esto

#del cocina esto es para eliminar una tupla

#TIPO SET
#Set no mantiene indice, es decir el orden es aleatorio
#sin orden ni indices
planetas = {'Marte', 'Jupiter', 'Tierra'}
print(len(planetas))

#Revisar si un elemento existe dentro de set
print('Marte' in planetas) #Devuelve un bool

#Agregar un elemento
planetas.add('La Rioja') #no se puede agregar elementos repetidos
print(planetas)
# set nos ayuda a que no se agreguen elementos duplicados a una lista

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Tierra') #cuando se escribe mal tira error
print(planetas)
planetas.discard('La Rioja') #si se escribe mal no se borra ni tira error
print(planetas)

#Limpiar Set
planetas.clear()
print(planetas)

#Eliminar Set
del planetas
#print(planetas)

# 'Messi':10 un diccionario esta compuesto por 2 elementos
# una llave y un valor
# dict(key,value)
diccionario = {
    'IDE':'Integrated Developed Enviroment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
#Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con la llave (key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# como recorrer los elementos
for termino in diccionario: #muestra solo las llaves
    print(termino)

#Necesitamos una funcion para acceder al diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

#otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #muestra solo las llaves

for valor in diccionario.values(): #muestra solo el valor
    print(valor)

#comprobar la existencia de un elemento
print('IDE' in diccionario) #bool

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('PK')
print(diccionario)

#vaciar diccionario
diccionario.clear
print(diccionario)

#eliminar diccionario
del diccionario

#Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1])
print(lista3)

print(lista3.index(9)) #funcion para ubicar el valor

# saber valores repetidos
print(lista3.count(1))

#poner lista al reves
lista3.reverse()
print(lista3)

#multiplicar lista repitiendo los elementos
lista = lista3 * 3
print(lista)

#metodos de ordenamiento
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

#repaso de tuplas
tupla = (4, 'holis', 6.16, [1, 2, 10], 4, 'holis')
print(tupla)

print(4 in tupla)

#Repaso de set o conjunto
#para definir un conjunto
conjunto = set()
conjunto1 = {'cr7', }
conjunto.add(7)
conjunto.add('Messi')
print(conjunto)
# conjunto1.add(9) figura error porque un conjunto con {} sola no se le puede agregar nada
#siempre tiene que tener un elemento dentro para poder agregar
conjunto1.add(7)
print(3 not in conjunto1)

# hacer igualdad de dos conjuntos
print(conjunto1 == conjunto)

#operaciones en conjuntos
conjunto2 = conjunto | conjunto1 #la linea une los conjuntos
print(conjunto2)

conjunto2 = conjunto1 & conjunto #elemento en comun
print(conjunto2)

conjunto2 = conjunto1 - conjunto #valor que esta en el conjunto1 y no en el conjunto
print(conjunto2)
conjunto2 = conjunto - conjunto1
print(conjunto2)

conjunto2 = conjunto1 ^ conjunto #elementos que no comparte o son diferentes
print(conjunto)

conjunto2 = conjunto | conjunto1
print(conjunto.issubset(conjunto2))
print(conjunto1.issubset(conjunto2))
print(conjunto2.issubset(conjunto))
print(conjunto2.issubset(conjunto1))

print(conjunto2.issuperset(conjunto))
print(conjunto2.issuperset(conjunto1))
print(conjunto.issuperset(conjunto2))
print(conjunto1.issuperset(conjunto2))

#como saber si son disconexos (no comparten elementos en comun)
print(conjunto.isdisjoint(conjunto1)) #falso porque si hay cosas en comun

#convertir un conjunto totalmente en inmutable
conjunto = frozenset
# no se puede agregar, modificar, ni eliminar elementos del conjunto

#Repaso diccionarios
diccionarioNew = {'Azul': 'Blue', 'Rojo': 'Red', 'Amarillo': 'Yellow', 'Verde': 'Green',}
print(diccionarioNew)

# los diccionarios pueden almacenar diferentes tipos de datos
#diccionario2 = {'Mati': {'edad:' 40, 'Altura': 1.77}, 'Messi': [35, 1.69], 'Cristiano': [37, 1.87]}
#print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.69, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho', 'Equipo': 'Paris Saint Germain'},
    9: {'Nombre': 'Julian Alvarez', 'Edad': 22, 'Altura': 1.70, 'Precio': '25 Millones', 'Posicion': 'Delantero Centro', 'Equipo': 'Manchester City'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho', 'Equipo': 'Juventus'},
    21: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '30 Millones', 'Posicion': 'Media Punta', 'Equipo': 'Roma'},  
    23: {'Nombre': 'Emiliano Martinez', 'Edad': 30, 'Altura': 1.95, 'Precio': '28 Millones', 'Posicion': 'Arquero', 'Equipo': 'Aston Villa'},
    13: {'Nombre': 'Cristian Romero', 'Edad': 24, 'Altura': 1.85, 'Precio': '48 Millones', 'Posicion': 'Defensa Central', 'Equipo': 'Tottenhan Hotspur'},
    16: {'Nombre': 'Lisandro Martinez', 'Edad': 24, 'Altura': 1.75, 'Precio': '32 Millones', 'Posicion': 'Defensa Central', 'Equipo': 'Manchester United'},
    25: {'Nombre': 'Enzo Fernandez', 'Edad': 21, 'Altura': 1.78, 'Precio': '15 Millones', 'Posicion': 'Mediocentro', 'Equipo': 'Benfica'},
    4: {'Nombre': 'Gonzalo Montiel', 'Edad': 25, 'Altura': 1.76, 'Precio': '14 Millones', 'Posicion': 'Lateral Derecho', 'Equipo': 'Sevilla'}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print('Futbolistas seleccion Argentina cargados:', end=' ')
print(len(seleccionArgentina))

#pilas usando listas
pila = [1, 2, 3]

#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#sacar elementos por el final
elementoBorrado = pila.pop() #quita el ultimo elemento y lo asigna en esta variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'PILA: {pila}')

#COLAS CON LISTAS
#estrucura de datos de tipo FIFO(first input/first output)
cola = ['Matias', 'Nicolas', 'Haller', 'Pellerite']

#agregamos un elemento al final de la cola
cola.append('Pro')
cola.append('xd')
print(cola)

#sacamos elementos
seVa = cola.pop(0)
print(f'Se retira: {seVa}')
print(cola)

seVa = cola.pop(0)
print(f'Se retira: {seVa}')
print(cola)

seVa = cola.pop(0)
print(f'Se retira: {seVa}')
print(cola)

seVa = cola.pop(0)
print(f'Se retira: {seVa}')
print(cola)

seVa = cola.pop(0)
print(f'Se retira: {seVa}')
print(cola)

#ver diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')