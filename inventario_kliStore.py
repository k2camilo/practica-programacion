print("---------- Sistema de Inventarios Klik Store ----------")

inventario = []

def solicitar_entero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Por favor ingresa un número entero válido.")

def solicitar_entero_positvo(prompt):
    while True:
        n = solicitar_entero(prompt)
        if n >= 0:
            return n
        print("⚠️ Ingresa un valor mayor o igual a 0.")

while True:
    print("\n📋 Menú de Opciones")
    print("------------------------------")
    print("1. Registrar Producto y Cantidad")
    print("2. Consultar Inventario")
    print("3. Buscar Producto")
    print("4. Editar Producto")
    print("5. Eliminar Producto")
    print("6. Mostrar Resumen General de Inventario")
    print("7. Salir")

    opcion = input("Ingresa la opción: ").strip()

    # === 1. Registrar producto ===
    if opcion == "1":
        print("\n📝 Ingrese datos del producto:")
        nombre = input("Ingrese nombre del producto: ").strip()
        cantidad = solicitar_entero_positvo("Ingrese cantidad: ")
        precio_unit = solicitar_entero_positvo("Ingrese el precio unitario (sin separadores): ")
        encontrado = False

        for item in inventario:
            if item["nombre"].lower() == nombre.lower():
                item["cantidad"] += cantidad
                # Actualizamos también el precio si el usuario así lo desea (opcional)
                actualizar_precio = input("¿Desea actualizar el precio unitario? (s/n): ").lower()
                if actualizar_precio == "s":
                    item["precio"] = precio_unit
                print(f"✅ Cantidad del producto '{item['nombre']}' actualizada. Cantidad actual: {item['cantidad']}")
                encontrado = True
                break

        if not encontrado:
            producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio_unit}
            inventario.append(producto)
            print("✅ Producto agregado correctamente.")

    # === 2. Consultar inventario ===
    elif opcion == "2":
        if inventario:
            print("\n📦 Inventario actual:\n")
            for i, item in enumerate(inventario, start=1):
                valor_item = item["cantidad"] * item["precio"]
                print(f"{i}. Producto: {item['nombre']} | Cantidad: {item['cantidad']} | "
                        f"Precio unitario: ${item['precio']:,} | Valor total: ${valor_item:,}")
        else:
            print("📭 El inventario está vacío, no hay productos registrados.")

    # === 3. Buscar producto ===
    elif opcion == "3":
        if inventario:
            buscar = input("Ingrese el producto a buscar: ").strip()
            encontrado = False
            for item in inventario:
                if item["nombre"].lower() == buscar.lower():
                    valor_item = item["cantidad"] * item["precio"]
                    print(f"\n🔎 Producto encontrado:\n- Producto: {item['nombre']}\n"
                        f"- Cantidad: {item['cantidad']}\n- Precio unitario: ${item['precio']:,}\n"
                        f"- Valor total: ${valor_item:,}")
                    encontrado = True
                    break
            if not encontrado:
                print("❌ Producto no encontrado.")
        else:
            print("📭 Inventario vacío, no hay productos registrados.")

    # === 4. Editar producto ===
    elif opcion == "4":
        if inventario:
            buscar = input("Ingrese el producto a editar: ").strip()
            for item in inventario:
                if item["nombre"].lower() == buscar.lower():
                    print(f"\n🛠 Producto encontrado: {item['nombre']} | Cantidad: {item['cantidad']} | Precio: ${item['precio']:,}")
                    nuevo_nombre = input("Nuevo nombre (deje vacío si no desea cambiarlo): ").strip()
                    nueva_cantidad = input("Nueva cantidad (deje vacío si no desea cambiarla): ").strip()
                    nuevo_precio = input("Nuevo precio (deje vacío si no desea cambiarlo): ").strip()

                    if nuevo_nombre:
                        item["nombre"] = nuevo_nombre
                    if nueva_cantidad:
                        try:
                            item["cantidad"] = int(nueva_cantidad)
                        except ValueError:
                            print("⚠️ Valor inválido. No se actualizó la cantidad.")
                    if nuevo_precio:
                        try:
                            item["precio"] = int(nuevo_precio)
                        except ValueError:
                            print("⚠️ Valor inválido. No se actualizó el precio.")

                    print(f"✅ Producto '{item['nombre']}' actualizado correctamente.")
                    break
            else:
                print("❌ Producto no encontrado.")
        else:
            print("📭 Inventario vacío, no hay productos para editar.")

    # === 5. Eliminar producto ===
    elif opcion == "5":
        if inventario:
            buscar = input("Ingrese el producto a eliminar: ").strip()
            encontrado = False
            for item in inventario:
                if item["nombre"].lower() == buscar.lower():
                    confirmacion = input(f"¿Seguro que deseas eliminar '{item['nombre']}'? (s/n): ").lower()
                    if confirmacion == "s":
                        inventario.remove(item)
                        print(f"🗑 Producto '{item['nombre']}' eliminado correctamente.")
                    else:
                        print("❎ Operación cancelada.")
                    encontrado = True
                    break
            if not encontrado:
                print("❌ Producto no encontrado.")
        else:
            print("📭 No hay productos para eliminar.")

    # === 6. Resumen general ===
    elif opcion == "6":
        if inventario:
            productos = len(inventario)
            unidades_totales = sum(item["cantidad"] for item in inventario)
            valor_total = sum(item["cantidad"] * item["precio"] for item in inventario)

            print("\n📊 Resumen general:")
            print(f"- Total de productos distintos: {productos}")
            print(f"- Total de unidades: {unidades_totales}")
            print(f"- Valor total del inventario: ${valor_total:,}")
        else:
            print("📭 Inventario vacío, no hay productos.")

    # === 7. Salir ===
    elif opcion == "7":
        print("👋 Saliendo del sistema de inventarios, ¡vuelva pronto!")
        break

    else:
        print(f"⚠️ Opción '{opcion}' incorrecta, ingrese una opción válida.")
