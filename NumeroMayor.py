# encabezado
print("Buscando el número mayor")

# solicitud de numeros a evaluar
numero_a = int(input("Digite el número A: "))
numero_b = int(input("Digite el número B: "))

# comparacion de numeros
def calculo_numero_mayor (n_a, n_b):
    # si "a" y "b" son iguales
    if (n_a == n_b):
        print("Los números son iguales, valor de los números: ", n_a)
    # si "a" es mayor a "b"
    elif (n_a > n_b):
        print("El numero mayor es el numero A: ", n_a)
    # si "b" es mayor a "a"
    else:
        print("El numero mayor es el numero B: ", n_b)

# llamada a la funcion que hace el calculo
calculo_numero_mayor(numero_a, numero_b)

# fin del programa
print("Fin del programa")
