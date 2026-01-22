'''
Crear un programa que permita comparar las edades de las personas
las edades se deben pedir al usuario
Si la primera persona es mayor que la segunda , imprimir "La primera persona es mayor"
Si la segunda persona es mayor que la primera , imprimir "La segunda persona es mayor"
Si las edades son iguales , imprimir "La dos personas tienen la misma edad"
'''
edad1=int(input("Ingrese la edad de la primera persona: "))
edad2=int(input("Ingrese la edad de la segunda persona: "))
if edad1>edad2:
    print("La primera persona es mayor")
elif edad2>edad1:
    print("La segunda persona es mayor")
else:
    print("Las dos persona tienen la misma edad")

