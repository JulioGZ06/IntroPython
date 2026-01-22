
import os
os.system("cls")

print("------ CALIFICACIONES ------")

contador = 1
suma = 0

while contador <= 5:
    calificacion = int(input("Ingrese la calificación: "))
    suma = suma + calificacion
    contador = contador + 1

promedio = suma / 5
print("Promedio:", promedio)