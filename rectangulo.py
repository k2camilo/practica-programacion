class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura
    

base = int(input('Ingrese  la base: '))
altura = int(input('Ingresa la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcularArea()}')