print("------- Sistema de Inventarios -------")

inventario = []

def solicitar_entero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Por favor ingresa un número entero válido.")

while True:
    print("\n📋 Menú de Opciones")
    print("------------------------------")
    print("1. Registrar Producto y cantidad")
    print("2. Consultar Inventario")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Ingrese la opción: ").strip()

    if opcion == "1":
        print("\n📝 Ingrese datos del producto")
        nombre = input("Ingrese nombre de producto: ").strip()
        cantidad = solicitar_entero("Ingrese la cantidad de ese producto: ")

        # Si el producto ya existe, aumentamos la cantidad; si no, lo agregamos
        encontrado = False
        for item in inventario:
            if item["nombre"].lower() == nombre.lower():
                item["cantidad"] += cantidad
                encontrado = True
                print(f"✅ Cantidad actualizada: {item['nombre']} ahora tiene {item['cantidad']} unidades.")
                break

        if not encontrado:
            producto = {"nombre": nombre, "cantidad": cantidad}
            inventario.append(producto)
            print("✅ Producto agregado correctamente.")

    elif opcion == "2":
        if inventario:
            print("\n📦 Inventario actual:")
            for i, item in enumerate(inventario, start=1):
                print(f"{i}. Producto: {item['nombre']} | Cantidad: {item['cantidad']}")
        else:
            print("📭 El inventario está vacío, no hay productos registrados.")

    elif opcion == "3":
        if inventario:
            buscar = input("Ingrese el producto a buscar: ").strip()
            encontrado = False
            for item in inventario:
                if item["nombre"].lower() == buscar.lower():
                    print(f"\n🔎 Producto encontrado:\n- Producto: {item['nombre']}\n- Cantidad: {item['cantidad']}")
                    encontrado = True
                    break
            if not encontrado:
                print("❌ Producto no encontrado.")
        else:
            print("📭 Inventario vacío, no hay productos registrados.")

    elif opcion == "4":
        print("👋 Saliendo del sistema de inventarios, ¡vuelva pronto!")
        break

    else:
        print(f"⚠️ Opción '{opcion}' incorrecta, ingrese una opción válida.")
