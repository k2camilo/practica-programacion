def resumen_compra(*productos, **cliente):
    """Genera un resumen de compra y retorna un diccionario con los datos clave."""
    
    # Calcular total
    total = sum(productos)
    
    # Crear resumen en un dic
    # cionario
    resumen = {
        "cliente": cliente if cliente else {"Cliente": "Desconocido"},
        "total_compra": total,
        "cantidad_productos": len(productos),
        "estado": ""
    }
    
    # Determinar el estado de la compra según el total
    if total > 100000:
        resumen["estado"] = "Compra Grande - Descuento Especial 🎉"
    elif total == 0:
        resumen["estado"] = "Sin productos registrados ❌"
    else:
        resumen["estado"] = "Compra Normal 🛒"
    
    # Mostrar información en consola
    print("----- Resumen de Compra -----")
    for clave, valor in resumen["cliente"].items():
        print(f"{clave.title()}: {valor}")
    print(f"Productos comprados: {resumen['cantidad_productos']}")
    print(f"Total a pagar: ${resumen['total_compra']:,}")
    print(f"Estado: {resumen['estado']}")
    print("-----------------------------\n")
    
    # Retornar el resumen completo
    return resumen

# Caso 1
r1 = resumen_compra(20000, 50000, Cliente="Camilo", Ciudad="Bogotá")

# Caso 2
r2 = resumen_compra(Cliente="Laura", Ciudad="Medellín")

# Caso 3
r3 = resumen_compra(100000, 80000, Cliente="Andrés", Ciudad="Cali")

# Mostrar los datos retornados (por si los quieres usar en otro proceso)
print("Datos retornados:")
print(r1)
print(r2)
print(r3)
