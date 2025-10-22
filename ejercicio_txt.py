from datetime import datetime

print("📝 --- Editor de Notas con Registro de Fecha y Hora ---")

nombre_archivo = "notas_bitacora.txt"

def leer_lineas():
    """Lee todas las líneas del archivo y las retorna como lista"""
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return archivo.readlines()

def guardar_lineas(lineas):
    """Guarda una lista de líneas en el archivo"""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

# Crear el archivo si no existe
open(nombre_archivo, "a").close()

while True:
    print("\n📋 Menú de Opciones")
    print("------------------------------")
    print("1. Agregar nueva nota")
    print("2. Leer todas las notas")
    print("3. Editar nota existente")
    print("4. Eliminar nota")
    print("5. Ver posición del puntero")
    print("6. Salir")
    print("------------------------------")

    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        texto = input("✏️ Escribe tu nueva nota: ").strip()
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{fecha}] {texto}\n"
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(linea)
        print("✅ Nota guardada correctamente.")

    elif opcion == "2":
        lineas = leer_lineas()
        if not lineas:
            print("📭 No hay notas registradas.")
        else:
            print("\n📄 Contenido de tus notas:")
            print("------------------------------")
            for i, linea in enumerate(lineas, start=1):
                print(f"{i}. {linea.strip()}")
            print("------------------------------")

    elif opcion == "3":
        lineas = leer_lineas()
        if not lineas:
            print("📭 No hay notas para editar.")
            continue

        for i, linea in enumerate(lineas, start=1):
            print(f"{i}. {linea.strip()}")

        try:
            num = int(input("Número de nota a editar: "))
            if 1 <= num <= len(lineas):
                nuevo_texto = input("Escribe el nuevo contenido: ").strip()
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                lineas[num - 1] = f"[{fecha}] {nuevo_texto}\n"
                guardar_lineas(lineas)
                print("✏️ Nota actualizada correctamente.")
            else:
                print("❌ Número de nota inválido.")
        except ValueError:
            print("⚠️ Debes ingresar un número válido.")

    elif opcion == "4":
        lineas = leer_lineas()
        if not lineas:
            print("📭 No hay notas para eliminar.")
            continue

        for i, linea in enumerate(lineas, start=1):
            print(f"{i}. {linea.strip()}")

        try:
            num = int(input("Número de nota a eliminar: "))
            if 1 <= num <= len(lineas):
                eliminado = lineas.pop(num - 1)
                guardar_lineas(lineas)
                print(f"🗑️ Nota eliminada: {eliminado.strip()}")
            else:
                print("❌ Número de nota inválido.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")

    elif opcion == "5":
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            archivo.seek(0, 2)
            pos = archivo.tell()
            print(f"📍 El puntero está en la posición: {pos} bytes (final del archivo).")

    elif opcion == "6":
        print("👋 Saliendo del editor de notas. ¡Hasta pronto!")
        break

    else:
        print("❌ Opción no válida. Intenta nuevamente.")
