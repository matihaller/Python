class Persona: #Creamos una clase
     #pass # no se procesa nada mas (no tiene contenido)
     #clase es la plantilla, atributos=caracteristicas, objetos=acciones
    def __init__(self, nombre, apellido, edad): #se lo llama metodo init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
#       atributo = variable
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')    




persona1 = Persona('Matías', 'Haller', 21) # necesitamos enviar argumentos
print(persona1.nombre, persona1.apellido) 
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, {persona1.edad}')
#segundo objeto
persona2 = Persona('Leo', 'Messi', 35)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, {persona2.edad}')
#se utiliza tipos dinamicos

persona1.nombre = 'Cristiano'
persona1.apellido = 'Ronaldo'
persona1.edad = 37
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, {persona1.edad}')

#los atributos son caracteristicas
# los metodos son el comportamiento que van a tener los objetos(acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()


