import math, os 


os.system("cls")


print("Operaciones basicas:\n1.- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n")

opcion=int(input("Ingrese la operacion a realizar (1/2/3/4): "))


if opcion==1:
    Num1=int(input("Ingrese el primer numero: "))
    Num2=int(input("Ingrese el segundo numero: "))
    resultado=Num1+Num2
    print("RESULTADO: ",resultado)
if opcion==2:
    Num1=int(input("Ingrese el primer numero: "))
    Num2=int(input("Ingrese el segundo numero: "))
    resultado=Num1-Num2
    print("RESULTADO: ",resultado)
if opcion==3:
    Num1=int(input("Ingrese el primer numero: "))
    Num2=int(input("Ingrese el segundo numero: "))
    resultado=Num1*Num2
    print("RESULTADO: ",resultado)
if opcion==4:
    Num1=int(input("Ingrese el primer numero: "))
    Num2=int(input("Ingrese el segundo numero: "))
    resultado=Num1/Num2
    print("RESULTADO: ",resultado)


if (opcion!=1 or opcion!=2 or opcion!=3 or opcion!=4):
    print("Operacion no invalida")