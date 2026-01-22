import os 


os.system("cls")

num=int(input("Ingrse un numero(0 para terminar): "))
suma=0

while num!=0:
    suma = suma + num
    num=int(input("Ingrese un numero: (0 para terminar): "))
    
print("\nLa suma de los numeros ingresados es: ",suma)
    
    
