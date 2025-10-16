#funciones de multiples parametros

def calcular_area(base,altura):
    area = base * altura
    return area

#resultado = calcular_area(4,2)
#print(f"el area es: {resultado}")

#funciona para calcular doble y triple de un numero

def dobre_y_triple(numero):
    doble = numero * 2
    triple = numero * 3
    return doble, triple

#d, t = dobre_y_triple(4)
#print(f"el dobre es: {d} y el triple es: {t}")

def calculadora(a,b):
    suma = a + b
    resta = a - b
    multi = a * b
    if b != 0:
        div = a / b
    else:
        div = "Error: división entre cero"
    return suma, resta, multi, div

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

s, r, m, d = calculadora(n1,n2)

print("Resultado de las operaciones: \n")
print(f"La suma entre {n1} + {n2} = {s}")
print(f"La resta entre {n1} - {n2} = {r}")
print(f"La multiplicación entre {n1} * {n2} = {m}")
print(f"La división entre {n1} / {n2} = {d}")