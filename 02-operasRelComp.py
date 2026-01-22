import math, os 


os.system("cls")

print("|---------Grupos ICO201-9,ICO201-14---------|")

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

suma=num1+num2
print("La suma de {} con {} es:{} ".format(num1,num2,suma))

resta = num1 - num2
print("La resta de {} con {} es:{} ".format(num1,num2,resta))
multiplicacion = num1 * num2
print("La multiplicacion de {} con {} es:{} ".format(num1,num2,multiplicacion))
division = num1 / num2
print("La division de {} con {} es:{} ".format(num1,num2,division))

potencia = num1 ** num2
print("La potencia de {} con {} es:{} ".format(num1,num2,potencia))


print("Operaciones basicas:\n1.- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n")

opcion=input("Ingrese la operacion a realizar (1/2/3/4): ")



val1=3
val2=5

temp=val1>val2#false
temp=val1==val2#false
temp=val1<val2#true
temp=val1>=val2#false
temp=val1<=val2#true
temp=val1!=val2#true
print("El valor de la comparacion es: ",temp)

tem2= not(val1>val2) and (val1<val2)
             #f               #t
print=("El valor de la comparacion con NOT es: ",tem2)