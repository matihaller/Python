class Rectangulo:
    """
    Crear una clase llamada rectangulo, debe tener 2
    atributos: altura y base
    el nombre del método será calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura
    deben ser ingresadas por el usuario y los
    objetos deben ser tres.
    """
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base
    
    def calcular_area(self):
        return self.base * self.altura

base = int(input("Digite la base: "))
altura = int(input("Digite la altura: "))
rectangulo1 = Rectangulo(base, altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")