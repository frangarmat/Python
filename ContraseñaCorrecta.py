# Crea un programa que pida por teclado introducir una contraseña. La contraseña no
# podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
# el programa imprime “Contraseña OK”
# En caso contrario imprime “Contraseña errónea”


contrasena = input ("Por favor digite su contraseña: ")
blanca = 0

for i in range (len (contrasena)):
    if contrasena[i] == " ":
        blanca = 1

if len(contrasena) < 8 or blanca > 0:
    print ("Contraseña erronea")
else:
    print("Contraseña correcta")
