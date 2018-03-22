# Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función de si tiene “@” o “.”
# Hay que tener en cuenta que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”


correo = input("Escriba su correo electrónico: ")
arroba = False
punto = 0

for i in range (len(correo)):

    if correo[i] == "@":
         arroba = True

    if correo [i] == ".":
        punto = punto + 1

if arroba and punto > 0:
    print ("El correo electrónico es correcto")
else:
    print ("El correo electrónico es incorrecto")
