# Practica If - Else

# encabezado
print("|---------------------------------|")
print ("Verificación de edad")
print("|---------------------------------|")

# pregunta la edad al usuario
edad_usuario = int (input("Digite su edad: "))

# hace el calculo sobre la edad
if edad_usuario < 18:
    print("No puedes ingresar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print ("Puedes pasar")

# final del Programa
print("Fin del Programa")
