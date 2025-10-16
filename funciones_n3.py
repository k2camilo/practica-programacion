def saludar(nombre="Invitado"):
    print(f"hola {nombre}, bienvenido")

#saludar("Camilo")
#saludar()

def calculadora(a = 1,b = 5):
    suma = a + b
    resta = a - b
    multi = a * b
    if b != 0:
        div = a / b
    else:
        div = "Error: división entre cero"
    return suma, resta, multi, div

#s, r, m, d = calculadora()

#print("Resultado de las operaciones: \n")
#print(f"La suma  = {s}")
#print(f"La resta  = {r}")
#print(f"La multiplicación  = {m}")
#print(f"La división entre  = {d}")

def crear_usuario(nombre="Usuario desconocido", edad=18, ciudad="Bogotá"):
    print(f"Usuario creado: {nombre}, {edad} años, vive en {ciudad}.")

#crear_usuario("Camilo", 25, "Bogotá")
#crear_usuario()

