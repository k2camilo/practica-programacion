print("Bienvenido al Banco BBVA")
print("-------------------------\n")

usuario_1 = "Camilo"
contrasena_1 = "1234"
intentos = 0
saldo = 1000
acceso = False

while intentos <3:
    
    usuario = input("Ingrese su Usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    if usuario == usuario_1 and contrasena == contrasena_1:
        acceso = True
    elif usuario != usuario_1:
        print("Usuario no Registrado.")
        break
    else:
        print("Contraseña incorrecta, Intente de nuevo. \n")
        intentos +=1
        print(f"Numero de intentos: {intentos}")
    
    if intentos == 3:
        print("Usario y Acceso bloqueado por exceso de intentos.")
        print(f"Numero de intentos: {intentos}")

if acceso:
    print(f"Acceso consedido, Bienvenido. {usuario} \n")
    opcion = 0
    while opcion != 4:
        print("Que operación desea realizar: ")
        print("------------------------------\n")
        print("1. Consultar Saldo")
        print("2. Retiros")
        print("3. Ingreso de Dinero")
        print("4. Salir")
        print("------------------------------\n")
        opcion = int(input("Ingrese el numero de operación a realizar: "))
        if opcion == 1:
            print(f"Su saldo actual es: ${saldo}\n")
        elif opcion == 2:
            retiro = int(input("Ingrese el valor a retirar: $"))
            if retiro < saldo:
                saldo -= retiro
                print(f"Retiro existoso por valor de: ${retiro}\n")
                print(f"Saldo actual en tu cuenta: ${saldo}\n")
            else:
                print("Saldo insuficiente para esta operación.\n")
        elif opcion == 3:
            ingreso = int(input("ingrese el valor a depositar: $"))
            saldo += ingreso
            print(f"Deposito Exitoso por valor de: ${ingreso}\n")
        elif opcion == 4:
            print("Saliendo...\n")
        else:
            print("Opcion invalida, intente nuevamete")
    
print("Hasta Luego, vuelva Pronto")