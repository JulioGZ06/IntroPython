import  math ,os 

os.system("cls")

num=0


while num < 1 or num > 100 :
    num=int(input("Escribir un numero entre 1 - 100: "))
    
    if num < 1 or num > 100:
        print("Numero Invalido")

binario=0
potencia=1

while num > 0:
    resto=num % 2
    binario=binario + resto * potencia
    potencia=potencia * 10 
    num=num // 2
print("Numero binario es: ", binario)
    
    