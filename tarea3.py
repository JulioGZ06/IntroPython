import math, os 


os.system("cls")


print("----- MENU DE OPCIONES -----")
print("1. Triangulo")
print("2. Cuadrado")
print("3. Circulo")
print("4. Pentagono")
print("5. Salir")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    print("Usted selecciono TRIANGULO")
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print("El area del triangulo es:", area)

else:
    if opcion == 2:
        print("Usted selecciono CUADRADO")
        lado = int(input("Ingrese el lado: "))
        area = lado * lado
        print("El area del cuadrado es:", area)

    else:
        if opcion == 3:
            print("Usted selecciono CIRCULO")
            radio = int(input("Ingrese el radio: "))
            area = 3.1416 * radio * radio
            print("El area del circulo es:", area)

        else:
            if opcion == 4:
                print("Usted selecciono PENTAGONO")
                lado = int(input("Ingrese el lado: "))
                apotema = int(input("Ingrese el apotema: "))
                area = (5 * lado * apotema) / 2
                print("El area del pentagono es:", area)

            else:
                if opcion == 5:
                    print("Saliendo del programa...")

                else:
                    print("Opcion no valida")
