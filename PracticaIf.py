
print("Programa para evaluar notas")
nota_alumno = int (input("Digite la nota del alumno: "))

print("La nota es: ", nota_alumno)


#funcion evaluadora
def evaluacion (nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print("Su condición es:", evaluacion(nota_alumno))
