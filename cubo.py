class Cubo:
    def __init__(self, ancho, largo, alto):
        self.ancho = ancho
        self.largo = largo
        self.alto = alto

    def calcularVolumen(self):
        return self.ancho * self.largo * self.alto

print('Ingrese las medidas del cubo para calcular su volumen: ')    
ancho = int(input('Ingrese el ancho del cubo: '))
largo = int(input('Ingrese el largo del cubo: '))
alto = int(input('Ingrese el alto del cubo: '))

cubo1 = Cubo(ancho, largo, alto)
print(f'El volumen del cubo es: {cubo1.calcularVolumen()}')