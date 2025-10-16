print("------- Sistema de Inventarios -------")

inventario = []

def solicitar_entero(prompt):
    """Solicita un número entero y valida que sea correcto."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Por favor ingresa un número entero válido.")

while True:
    print("\n📋 Menú de Opciones")
    print("------------------------------")
    print("1. Registrar Producto y Cantidad")
    print("2. Consultar Inventario")
    print("3. Buscar Producto")
    print("4. Editar Producto")
    print("5. Eliminar Producto")
    print("6. Salir")

    opcion = input("Ingrese la opción: ").strip()

    # === 1. Registrar producto ===
    if opcion == "1":
        print("\n📝 Ingrese datos del producto")
        nombre = input("Ingrese nombre del producto: ").strip()
        cantidad = solicitar_entero("Ingrese la cantidad: ")

        # Si el producto ya existe, sumamos cantidad
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

    # === 2. Mostrar inventario completo ===
    elif opcion == "2":
        if inventario:
            print("\n📦 Inventario actual:")
            for i, item in enumerate(inventario, start=1):
                print(f"{i}. Producto: {item['nombre']} | Cantidad: {item['cantidad']}")
        else:
            print("📭 El inventario está vacío, no hay productos registrados.")

    # === 3. Buscar producto ===
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

    # === 4. Editar producto ===
    elif opcion == "4":
        if inventario:
            buscar = input("Ingrese el nombre del producto a editar: ").strip()
            for item in inventario:
                if item["nombre"].lower() == buscar.lower():
                    print(f"\n🛠 Producto encontrado: {item['nombre']} ({item['cantidad']} unidades)")
                    nuevo_nombre = input("Nuevo nombre (deje vacío si no desea cambiarlo): ").strip()
                    nueva_cantidad = input("Nueva cantidad (deje vacío si no desea cambiarla): ").strip()

                    if nuevo_nombre:
                        item["nombre"] = nuevo_nombre
                    if nueva_cantidad:
                        try:
                            item["cantidad"] = int(nueva_cantidad)
                        except ValueError:
                            print("⚠️ Valor inválido, no se actualizó la cantidad.")
                    
                    print("✅ Producto actualizado correctamente.")
                    break
            else:
                print("❌ Producto no encontrado.")
        else:
            print("📭 No hay productos para editar.")

    # === 5. Eliminar producto ===
    elif opcion == "5":
        if inventario:
            buscar = input("Ingrese el nombre del producto a eliminar: ").strip()
            for item in inventario:
                if item["nombre"].lower() == buscar.lower():
                    confirmacion = input(f"¿Seguro que deseas eliminar '{item['nombre']}'? (s/n): ").lower()
                    if confirmacion == "s":
                        inventario.remove(item)
                        print(f"🗑 Producto '{item['nombre']}' eliminado correctamente.")
                    else:
                        print("❎ Operación cancelada.")
                    break
            else:
                print("❌ Producto no encontrado.")
        else:
            print("📭 No hay productos para eliminar.")

    # === 6. Salir ===
    elif opcion == "6":
        print("👋 Saliendo del sistema de inventarios, ¡vuelva pronto!")
        break

    else:
        print(f"⚠️ Opción '{opcion}' incorrecta, ingrese una opción válida.")
