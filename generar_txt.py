# 🛒 Sistema de registro de compras (Klik Store)

historial_compras = []


def resumen_compra(*productos, **cliente):
    total = sum(productos)
    registro = {
        "cliente": cliente.get("Cliente", "Desconocido"),
        "edad": cliente.get("edad", "N/A"),
        "ciudad": cliente.get("ciudad", "Sin registrar"),
        "cantidad_productos": len(productos),
        "total_compra": total
    }

    historial_compras.append(registro)
    print("\n✅ Compra registrada correctamente.")
    mostrar_resumen(registro)


def mostrar_resumen(registro):
    print("\n---- 🧾 Resumen de Compra ----")
    for clave, valor in registro.items():
        print(f"{clave}: {valor}")
    print("-------------------------------")


def guardar_en_archivo():
    """Guarda el historial completo en un archivo .txt"""
    with open("historial_compras.txt", "w", encoding="utf-8") as archivo:
        for i, compra in enumerate(historial_compras, start=1):
            archivo.write(f"\nCompra {i}:\n")
            for clave, valor in compra.items():
                archivo.write(f"{clave}: {valor}\n")
            archivo.write("-------------------------------\n")
    print("💾 Historial guardado correctamente en 'historial_compras.txt'")


def leer_archivo():
    """Lee y muestra el historial guardado desde el archivo .txt"""
    try:
        with open("historial_compras.txt", "r", encoding="utf-8") as archivo:
            print("\n📜 HISTORIAL DE COMPRAS GUARDADO:")
            print(archivo.read())
    except FileNotFoundError:
        print("⚠️ No existe ningún archivo de historial guardado aún.")


# 🧍 Ejemplo de uso:
resumen_compra(30000, 15000, 12000, Cliente="Camilo", edad=33, ciudad="Bogotá")
resumen_compra(25000, 20000, Cliente="Laura", edad=28, ciudad="Medellín")

guardar_en_archivo()
leer_archivo()

