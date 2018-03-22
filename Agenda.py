print("Agenda electrónica",end='\n')

# solicitud de datos
nombre = input("Por favor digite su primer nombre: ")
direccion = input("Por favor digite su dirección: ")
telefono = input("Por favor digite su número de teléfono: ")

# inclusion en la lista
datos=[nombre, direccion, telefono]

# impresion de los datos
print ("Sus datos personales son:", end='\n' + "Nombre: " + datos[0] + " Dirección: " + datos[1] + " Teléfono: " + datos[2] + ".")
