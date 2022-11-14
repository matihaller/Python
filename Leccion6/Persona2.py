class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')
    
    @property # decorador
    def nombre(self): #metodo getter
        print('Estamoms usando el metodo get')
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        print('Estamos usando el método set')
        self._nombre = nombre
    
    @property # decorador
    def apellido(self): #metodo getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido    

    @property # decorador
    def edad(self): #metodo getter 
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad   

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2("Matías", "Haller", 21)
    #print(persona1._nombre) aunque se puede, no se debe hacer
    print(persona1.nombre) #llamamos al método getter
    persona1.nombre = 'Itachi' #llamamos al metodo setter
    print(persona1.nombre) #otra vez el metodo get
    print(persona1.mostrar_detalles)
    #atributo read only seria la edad porque no tiene el metodo set
    print(persona1.edad)

    #objeto 1
    persona2 = Persona2('Itachi', 'Uchiha', 21)
    persona2.nombre = 'Itachi'
    persona2.apellido = 'Uchiha'
    persona2.edad = 21
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    print(persona2.mostrar_detalles())

    #objeto 2
    persona3 = Persona2('Emi', 'Haller', 22)
    persona3.nombre = 'Emiliano'
    persona3.apellido = 'Haller'
    persona3.edad = 22
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    print(persona3.mostrar_detalles())

    #objeto 3
    persona4 = Persona2('Lolsito', 'Riot', 12)
    persona4.nombre = 'LoL'
    persona4.apellido = 'Pro'
    persona4.edad = 12
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    print(persona4.mostrar_detalles())


    print(__name__) #muestra que clase se está ejecutando y hasta donde