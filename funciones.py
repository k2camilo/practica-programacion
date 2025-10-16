def miFuncion(nombre, apellido):
    print(f"saludos desde mi función para: {nombre} {apellido}")

miFuncion("Camilo","Gutierrez");

def sumar(a, b):
    return a + b

resultado = sumar(1,2)
print(resultado)
#funcion de tupla
def lisstaDeNombres(*nombres):
    for nombre in nombres:
        print(nombre)

lisstaDeNombres("Camilo","liss","angie","carlos")

#funcion de diccionario
def ListarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} {valor}')

ListarTerminos(nombre="camilo")

#funciones recursivas
    