def sumar_todos(*numeros):
    total = sum(numeros)
    return total

#resultado = sumar_todos(1, 2, 3, 4, 5, 6)
#print(f"La suma total es: {resultado}")

def mostrar_info(**persona):
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

#mostrar_info(nombre="Camilo", edad = 26, ciudad = "Bogotá", profesion = "Ingeniero de Software")

def resumen_compra(*productos, **cliente):
    total = sum(productos)
    print("---- Resumen de Compra ----")
    for clave, valor in cliente.items():
        print(f"{clave}: {valor}")
    print(f"Productos comprados: {len(productos)}")
    print(f"Valor de la compra: ${total}")

#resumen_compra(30000, 10000, 5000, Cliente = "Camilo", edad = 33, ciudad = "Bogotá")

def resumen_compra(*productos, **cliente):
    print("----- Resumen de Compra -----")
    
    # Validar si hay datos del cliente
    if not cliente:
        print("⚠️ No se ingresaron datos del cliente.")
    else:
        for clave, valor in cliente.items():
            print(f"{clave.title()}: {valor}")
    
    # Validar si se ingresaron productos
    if not productos:
        print("\n❌ No se agregaron productos a la compra.")
        print("-----------------------------\n")
        return  # Detiene la función aquí
    
    # Calcular total y mostrar resumen
    total = sum(productos)
    print(f"\nProductos comprados: {len(productos)}")
    print(f"Total a pagar: ${total:,}")
    
    # Mensaje condicional según el total
    if total > 100000:
        print("🎉 ¡Gracias por tu gran compra! Obtienes un descuento especial.")
    elif total < 10000:
        print("🛒 Compra pequeña, ¡esperamos verte de nuevo pronto!")
    
    print("-----------------------------\n")

# Ejemplos de uso:

# ✅ Caso 1: compra normal
resumen_compra(30000, 10000, 5000, Cliente="Camilo", Edad=33, Ciudad="Bogotá")

# ⚠️ Caso 2: sin productos
resumen_compra(Cliente="Laura", Ciudad="Medellín")

# ⚠️ Caso 3: compra muy grande
resumen_compra(50000, 70000, 25000, Cliente="Andrés", Ciudad="Cali")
