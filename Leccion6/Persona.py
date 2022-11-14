class Persona: #Creamos una clase
     #pass # no se procesa nada mas (no tiene contenido)
     #clase es la plantilla, atributos=caracteristicas, objetos=acciones
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
#       atributo = variable

    def mostrar_detalle(self): #mismo uso que this en java
        print(f'la clase Persona tiene los sig. datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs} ')    



persona1 = Persona('Matías', 'Haller', 43682199, 21) # necesitamos enviar argumentos
#print(persona1.nombre, persona1.apellido) 
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, {persona1.edad}')
#segundo objeto
persona2 = Persona('Leo', 'Messi', 5648498456, 35)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, {persona2.edad}')
#se utiliza tipos dinamicos

persona1.nombre = 'Cristiano'
persona1.apellido = 'Ronaldo'
persona1.edad = 37
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, {persona1.edad}')

#los atributos son caracteristicas
# los metodos son el comportamiento que van a tener los objetos(acciones)
#metodo=funcion solo que el metodo está asociado a una clase y la F no
persona1.mostrar_detalle() #la referencia en este caso se pasa de manera auto
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) debemos darle una referencia para el self o da error
persona1.celular = '2604051967'
print(f'telefono del bicho: {persona1.celular}')
#atributo solo agregado a persona 1

# print(persona2.celular) el objeto no tiene este atributo, da ERROR
persona3 = Persona('Matu', 'Haller', 4448956, 21, 'Telefono', '2604051966', 'Caller Cornú', 1022, 'Manzana', 14, 'Casa', 12, Altura=1.76, Peso=70, CFavorito='Verde', Auto='Mercedes Benz', Modelo=2022)
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar(está encapsulado), dice que desconocemos el lenguaje
#persona3.__nombre  está completamente encapsulado

