print("-------- 🧑‍🤝‍🧑 Registro De Amigos --------")

amigos = []

while True:
    print("\n📋 Menú de Opciones")
    print("------------------------------")
    print("1. Registrar Amigo")
    print("2. Buscar amigo por Nombre")
    print("3. Buscar amigo por Ciudad")
    print("4. Mostrar Todos los amigos")
    print("5. Editar registro de amigo")
    print("6. Eliminar registro de amigo")
    print("7. Salir")
    print("------------------------------")

    opcion = input("Ingrese la opción: ")

    if opcion == "1":
        print("\n📝 Ingrese los datos de su amigo:")
        nombre = input("Nombre: ").strip()
        edad = input("Edad: ").strip()
        ciudad = input("Ciudad: ").strip()

        persona = {"nombre": nombre, "edad": edad, "ciudad": ciudad}
        amigos.append(persona)

        print("✅ Amigo agregado correctamente.\n")

    elif opcion == "2":
        busca_nombre = input("Ingrese el nombre a buscar: ").strip()
        encontrado = False

        for amigo in amigos:
            if amigo["nombre"].lower() == busca_nombre.lower():
                print(f"\n✅ Amigo encontrado:")
                print(f"👤 Nombre: {amigo['nombre']}")
                print(f"🎂 Edad: {amigo['edad']}")
                print(f"🏙️ Ciudad: {amigo['ciudad']}")
                encontrado = True
                break

        if not encontrado:
            print("❌ Amigo no encontrado.")

    elif opcion == "3":
        busca_ciudad = input("Ingrese la ciudad para buscar amigos: ").strip()
        encontrados = [a for a in amigos if a["ciudad"].lower() == busca_ciudad.lower()]

        if encontrados:
            print(f"\n✅ Amigos que viven en {busca_ciudad.capitalize()}:")
            for a in encontrados:
                print(f"- {a['nombre']} ({a['edad']} años)")
        else:
            print("❌ No hay amigos registrados en esa ciudad.")

    elif opcion == "4":
        if amigos:
            print("\n--- 📜 Lista de Amigos ---")
            for i, amigo in enumerate(amigos, start=1):
                print(f"{i}. 👤 {amigo['nombre']} | 🎂 {amigo['edad']} años | 🏙️ {amigo['ciudad']}")
        else:
            print("📭 No hay amigos registrados aún.")

    elif opcion == "5":
        busca_nombre = input("Ingrese el nombre del amigo para editar: ").strip()
        encontrado = False

        for amigo in amigos:
            if amigo["nombre"].lower() == busca_nombre.lower():
                print(f"\n✏️ Editando el registro de {amigo['nombre']}:")
                nueva_edad = input("Nueva edad: ").strip()
                nueva_ciudad = input("Nueva ciudad: ").strip()

                amigo["edad"] = nueva_edad
                amigo["ciudad"] = nueva_ciudad

                print("✅ Registro modificado correctamente.")
                encontrado = True
                break

        if not encontrado:
            print("❌ Amigo no encontrado.")

    elif opcion == "6":
        busca_nombre = input("Ingrese el nombre del amigo para eliminar: ").strip()
        encontrado = False

        for amigo in amigos:
            if amigo["nombre"].lower() == busca_nombre.lower():
                confirmacion = input(f"¿Está seguro de eliminar a {amigo['nombre']}? (s/n): ").lower()
                if confirmacion == "s":
                    amigos.remove(amigo)
                    print("🗑️ Registro eliminado correctamente.")
                else:
                    print("❎ Eliminación cancelada.")
                encontrado = True
                break

        if not encontrado:
            print("❌ Amigo no encontrado.")

    elif opcion == "7":
        print("\n👋 Saliendo del registro de amigos...")
        break

    else:
        print(f"⚠️ La opción ingresada '{opcion}' no existe. Intente nuevamente.")

print("\n✅ Registro finalizado correctamente.")




