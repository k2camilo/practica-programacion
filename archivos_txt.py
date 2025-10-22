#modos de apertura:
"""
"r" : read(leer) - abre archivo para lectura, da error si no existe
"w" : write(escribir) - crea o sobre escribe archivo(borra lo anterior)
"a" : append(añadir) - agrega texto al final sin borrar el anterior
"r+" : read + write - permite leer y escribir, pero no crea el archivo si no existe
"a+" : apeend + read - permite leer y escribir, creando el archivo si no existe
"""

#crear y sobreescribir un archivo:
"""
with open("texto1.txt", "w", encoding="utf-8") as archivo:
    archivo.write("hola este es mi primer archivo \n")
    archivo.write("Estoy aprendiendo manejo de archivos en python")

"""
#leer un archivo y todo su contenido:
"""
with open("texto1.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

"""
#leer archivo por lineas
"""
with open("texto1.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

"""

#almacenar lineas de texto en una linea:
"""
with open("texto1.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(lineas[0].strip())
"""
#adicionar y leer un archivo
"""
with open("texto1.txt", "a+", encoding="utf-8") as archivo:
    archivo.write("\nEsta es una nueva liena de texto")
    archivo.seek(0) #vuelve al inicio del archivo
    for linea in archivo:
        print(linea)
"""
with open("texto1.txt", "r+", encoding="utf-8") as archivo:
    print(f"Posición iniciarl: {archivo.tell()}")

    linea1 = archivo.readline()
    print(f"Primera linea leida: {linea1.strip()}")

    print(f"Puntero despues de leer la linea: {archivo.tell()}")

    archivo.seek(0)

    print(f"Posición despues del seek: {archivo.tell()}")

    contenido = archivo.read()
    print(contenido)