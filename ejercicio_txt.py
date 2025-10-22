print("📝 --- Editor de Notas Avanzado ---")

nombre_archivo = "notas.txt"

def leer_lineas():
    """Lee todas las líneas y las retorna como lista"""
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return archivo.readlines()

def guardar_lineas(lineas):
    """Guarda una lista de líneas en el archivo"""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

# Crea el archivo si no existe
open(nombre_archivo, "a").close()

while True:
    print("\n📋 Menú de Opciones")
    print("------------------------------")
    print("1. Agregar nueva línea")
    print("2. Leer todo el contenido")
    print("3. Editar línea específica")
    print("4. Eliminar línea específica")
    print("5. Mostrar posición del puntero")
    print("6. Salir")
    print("------------------------------")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        texto = input("Escribe una línea nueva: ")
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
        print("✅ Línea agregada correctamente.")

    elif opcion == "2":
        lineas = leer_lineas()
        if not lineas:
            print("📭 El archivo está vacío.")
        else:
            print("\n📄 Contenido del archivo:")
            print("------------------------------")
            for i, linea in enumerate(lineas, start=1):
                print(f"{i}. {linea.strip()}")
            print("------------------------------")

    elif opcion == "3":
        lineas = leer_lineas()
        if not lineas:
            print("📭 No hay líneas para editar.")
            continue

        for i, linea in enumerate(lineas, start=1):
            print(f"{i}. {linea.strip()}")

        try:
            num = int(input("Número de línea a editar: "))
            if 1 <= num <= len(lineas):
                nuevo_texto = input("Escribe el nuevo contenido: ")
                lineas[num - 1] = nuevo_texto + "\n"
                guardar_lineas(lineas)
                print("✏️ Línea actualizada correctamente.")
            else:
                print("❌ Número de línea inválido.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")

    elif opcion == "4":
        lineas = leer_lineas()
        if not lineas:
            print("📭 No hay líneas para eliminar.")
            continue

        for i, linea in enumerate(lineas, start=1):
            print(f"{i}. {linea.strip()}")

        try:
            num = int(input("Número de línea a eliminar: "))
            if 1 <= num <= len(lineas):
                eliminado = lineas.pop(num - 1)
                guardar_lineas(lineas)
                print(f"🗑️ Línea eliminada: {eliminado.strip()}")
            else:
                print("❌ Número de línea inválido.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")

    elif opcion == "5":
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            archivo.seek(0, 2)  # Mueve puntero al final
            pos = archivo.tell()
            print(f"📍 El puntero está en la posición: {pos} bytes (final del archivo).")

    elif opcion == "6":
        print("👋 Saliendo del editor de notas avanzado. ¡Hasta pronto!")
        break

    else:
        print("❌ Opción no válida. Intenta nuevamente.")
