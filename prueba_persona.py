from persona import Persona

print("Creacion de Objetos".center(50,".")) #crear formaato
persona1 = Persona("Angie","Penagos",29)
persona1.mostrarDetalle()

print("Eliminación de objetos".center(50,"."))
del persona1
print(__name__) #imprime etiqueta del modulo donde se ejecuta