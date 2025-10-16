class Persona:
    #Atributos de clase
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    #getters
    @property #unicamente se puede acceder por el metodo
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @property
    def edad(self):
        return self._edad
        
    #setters
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    #metodos de clase
    def mostrarDetalle(self,    ):
        print(f'nomnre: {self._nombre} apellido: {self._apellido} edad: {self._edad}')

    def __del__(self):
        print(f'Objeto: {self._nombre} {self._apellido}')

#utilizar objetos de esta clase
if __name__ == "__main__":  #solo se ejecuta si se trabaja desde esata clase
    persona1 = Persona('Camilo',"Gutierrez",33)
    persona1.mostrarDetalle()
    persona1.nombre = "Cristian"
    persona1.apellido = "Calderon"
    persona1.edad = 34
    persona1.mostrarDetalle()

    print(__name__) #imprime etiqueta del modulo donde se ejecuta



