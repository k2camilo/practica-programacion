print("------ SISTEMA DE INVENTARIO V2 ------")

# 🧩 Función para registrar un nuevo producto
def registrar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio unitario: "))

    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(producto)
    print(f"✅ Producto '{nombre}' agregado correctamente.\n")

# 🧩 Función para consultar todo el inventario
def consultar_inventario(inventario):
    if not inventario:
        print("⚠️ El inventario está vacío.\n")
        return
    print("\n📦 Inventario actual:")
    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. {producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: ${producto['precio']}")
    print()

# 🧩 Función para buscar un producto por nombre
def buscar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a buscar: ")
    encontrados = [p for p in inventario if p["nombre"].lower() == nombre.lower()]

    if encontrados:
        for p in encontrados:
            print(f"🔍 Encontrado: {p['nombre']} - Cantidad: {p['cantidad']} - Precio: ${p['precio']}")
    else:
        print("❌ Producto no encontrado.\n")

# 🧩 Función para editar un producto existente
def editar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a editar: ")
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {p['nombre']}")
            p["cantidad"] = int(input("Nueva cantidad: "))
            p["precio"] = float(input("Nuevo precio: "))
            print("✅ Producto actualizado correctamente.\n")
            return
    print("❌ Producto no encontrado.\n")

# 🧩 Función para eliminar un producto
def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print(f"🗑️ Producto '{nombre}' eliminado correctamente.\n")
            return
    print("❌ Producto no encontrado.\n")

# 🧩 Función para mostrar un resumen general
def mostrar_resumen(inventario):
    if not inventario:
        print("⚠️ No hay productos registrados.\n")
        return
    total_items = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["cantidad"] * p["precio"] for p in inventario)
    print(f"📊 Total de productos: {len(inventario)}")
    print(f"📦 Total de unidades: {total_items}")
    print(f"💰 Valor total estimado: ${valor_total:,.2f}\n")

# 🧩 Función principal que controla el flujo del sistema
def menu_principal():
    inventario = []
    while True:
        print("Menú Principal:")
        print("1. Registrar producto")
        print("2. Consultar inventario")
        print("3. Buscar producto")
        print("4. Editar producto")
        print("5. Eliminar producto")
        print("6. Mostrar resumen")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(inventario)
        elif opcion == "2":
            consultar_inventario(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            editar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            mostrar_resumen(inventario)
        elif opcion == "7":
            print("👋 Saliendo del sistema. Hasta pronto!")
            break
        else:
            print("❌ Opción no válida, intente de nuevo.\n")

# 🚀 Iniciar el sistema
menu_principal()
