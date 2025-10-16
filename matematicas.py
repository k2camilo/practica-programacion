class Matematicas:
    """
        clase apra realizar operaciones basicas de matematicas
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB
    
matematicas1 = Matematicas(7,6)
print(f'la suma es: {matematicas1.sumar()}')
print(f'la resta es: {matematicas1.restar()}')
print(f'la multiplicación es: {matematicas1.multiplicar()}')
print(f'la división es: {matematicas1.dividir():.2f}') #con (:.2f) iondicamos que muestre solo dos decimales