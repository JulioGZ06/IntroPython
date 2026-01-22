import math, os 


os.system("cls")


sueldo = int(input("Ingrese el sueldo de la persona: "))

if sueldo < 1000:
    impuesto = 0
    print("No paga impuesto")

else:
    if sueldo >= 1000 and sueldo <= 2000:
        impuesto = sueldo * 0.10
        print("Paga el 10% de impuesto")

    else:
        if sueldo > 2000:
            impuesto = sueldo * 0.20
            print("Paga el 20% de impuesto")

sueldo_neto = sueldo - impuesto

print("Impuesto a pagar:", impuesto)
print("Sueldo neto:", sueldo_neto)
