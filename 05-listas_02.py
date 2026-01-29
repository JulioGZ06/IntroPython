import os 


os.system("cls")  

sueldos=[]

cont=0

while cont <= 4:
    tem=float(input("dame el sueldo"+str({cont+1})))
    sueldos.append(tem)
    cont+=1
    
print("los sueldos son: ", sueldos)

prom=sum(sueldos)/len(sueldos)
mayor=max(sueldos)
menor=min(sueldos)
print("el promedio de los sueldos es: ",prom)
print("el sueldo mas alto es: ",mayor)
print("el sueldo menor es: ",menor)