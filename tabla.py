import os
os.system("cls")

print("------------/TABLA\-------------")

num=int(input("Ingrese algun nuemero : "))

v=range(1 ,11)
for i in range (1 , 11): 
    tabla=num * i 
    print("{} * {} = {}".format(num,i,tabla))