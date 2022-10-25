
# Comenzamos con funciones

#mi_funcion() #no se puede llamar antes de def la funcion
# Definimos una funcion
'''
def mi_funcion(): # para identificar a la funcion usamos parentesis
    print('Hola Matu')

mi_funcion() # Estamos llamando a la funcion
mi_funcion()

# Desempaquetado de listas o list unpacking
def show(name, lastName):
    print(name+' '+lastName)
person = ["Matias", "Haller"]
show(person[0], person[1]) # pasamos 1x1 los datos de la lista a la funcion
show(*person) # esto es lo mismo que lo anterior pero se pasa todo junto
person2 = ("Leonel", "Messi")
show(*person2)
person3 = {"lastName" : "Ronaldo", "name": "Cristiano"}
show(**person3) #hay que poner 2 ** para que muestre lo de adentro

#repaso for else
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break #esta es la unica manera que no se ejecute el else.
else:
    print("Fin")

# list comprehension, lista de comprension
names = ["paulo", "leo", "cristiano", "matu"]
alongP = [p for p in names if p[0] == 'p'] #esto regresa una nueva lista
#la p es para cada elemento, pero en singular
print(alongP) #nos muestra kis nimbre que comienzan por p

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [q for q in bottleC if q["country"] == "Mx"] #esto hace que extraiga del diccionario solo lo que necesitamos
print(Arg) 
print(bottleC)

# paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("estoy re contra loco")
    print(f'Nombre: {name}, Apelliido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('mati', 'pro')
mi_funcion2('leo', 'messi')

#palabra return en funciones
#creamos una funcion para sumar
def sumar(a,b):
    return a+b
#resultado = sumar(78, 22)
#print(f'el resultado de la suma es: {resultado}')
print(f'el resultado de la suma es: {sumar(55, 45)}')

def sumar2(a=0, b=0) -> int:
    return a+b
resultado = sumar2()
print(f'resultado de la suma: {resultado}') 
print(f'resultado de la suma: {sumar2(22,66)}')

# argumentos, variables en funciones
def listarNombres(*nombres): # normalmente se utiliza: *args
    for nombre in nombres:  # se va a convertir en una tupla
        print(nombre)
listarNombres('mati', 'itachi', 'naruto', 'etc')
listarNombres('marcos', 'pepe', 'de pol')

def listarTerminos(**kwargs): #se puede poner cualquier nombre, pero es es el mas utlizado
    for llave, valor in kwargs.items(): #kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # no se muestra nada
listarTerminos(IDE ='Integrated Develoment Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leo Messi')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombres)
nombres2 = ['Tito', 'Pedro', 'Itachi']
desplegarNombres(nombres2)
desplegarNombres('Naruto')
#desplegarNombres('8') #nos da error porque es un entero (no es un objeto iterable)
desplegarNombres((10,)) #se convierte en tupla, no olvidar la coma
desplegarNombres([21, 6]) #se convierte en lista
'''
# Funciones Recursivas
def factorial(numero):
    if numero == 1: #caso base
        return 1
    else: 
        return numero * factorial(numero-1) # caso recursivo
numeroFactorial = int(input("Digite un numero para calcular el factorial: "))
resultado = factorial(numeroFactorial) # lo hacemos en codigo duro
print(f'El factorial del num. {numeroFactorial} es: {resultado}')



