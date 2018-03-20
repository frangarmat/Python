# encabezado
print("Buscando el número mayor")

# solicitud de numeros a evaluar
numero_a = int(input("Digite el número A: "))
numero_b = int(input("Digite el número B: "))

# comparacion de numeros
# si "a" y "b" son iguales
if (numero_a == numero_b):
    print("Los números son iguales, valor de los números: ", numero_a)
# si "a" es mayor a "b"
elif (numero_a > numero_b):
    print("El numero mayor es el numero A: ", numero_a)
# si "b" es mayor a "a"
else:
    print("El numero mayor es el numero B: ", numero_b)

# fin del programa
print("Fin del programa")
