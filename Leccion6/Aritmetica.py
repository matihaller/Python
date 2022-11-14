class Aritmetica:
    """
    el nombre de este tipo de comentario es: DocString
    esto es documentacion de la clase en Python
    vamos a hacer en esta clase alguna operaciones de suma,
    resta y más.
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    #metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB
        #metodo para restar
    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7,30) #le pasamos argumentos para los operando
print(aritmetica1.sumar())
print(f'la resta es: {aritmetica1.restar()}')
print(f'la multiplicación es: {aritmetica1.multiplicar()}')
print(f'la división es: {aritmetica1.dividir():.2f}')