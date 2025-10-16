nombres = ["camilo", "Lina", "angie", "Willou", "Edgar"]
print(nombres)
#impromir rangos
print(nombres[0:2])
#imprimir sin un indice
print(nombres[:3])
#modificar un indice en especifico
nombres[1]="Maria"
print(nombres)
for nombre in nombres:
    print(nombre)
#cuantos elementos tiene una lista
print(len(nombres))
#agregar un nuevo elemento
nombres.append("Luis")
print(nombres)
#insertar un nombre en un indice especifico
nombres.insert(1,"Carlos")
print(nombres)
#remover elementos
nombres.remove("Carlos")
print(nombres)
#remover el ultimo elemento
nombres.pop()
print(nombres)
#eliminar un elemento en un indice especifico
del nombres[0]
print(nombres)
#borrar todos los elementos de la lista
nombres.clear()
print(nombres)
#eliminar la lista
#del nombres