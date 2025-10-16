carrito = {
    "pantalla":150,
    "teclado":200,
    "mouse":50,
    "accesorios":"agotados"
}

print(carrito)
print(type(carrito))
#recorreor diccionario
for termino, valor in carrito.items():
    print(termino, valor)

#recorrer solo las llaves
for termino in carrito.keys():
    print(termino)
#recorrer solo los valores
for termino in carrito.values():
    print(termino)
#comprobar si existe una llave
print("pantalla" in carrito)
#agregar elementos en diccionario
carrito["cables"]=200
print(carrito)
#eliminar un elemento
carrito.pop("pantalla")
print(carrito)
carrito["mouse"]=120
print(carrito)