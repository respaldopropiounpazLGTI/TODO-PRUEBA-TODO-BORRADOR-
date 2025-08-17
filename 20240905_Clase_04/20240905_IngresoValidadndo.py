'''

while True:
    edad=int(input("Ingrese la edad: "))
    if edad>0 and edad<100:
        break
    else:
        print("Error, la edad debe ser mayor a 0")
        continue
'''

while True:
    edad=int(input("Ingrese la edad: "))
    if edad<0 or edad>100:
        print("Error, la edad debe ser mayor a 0 y menor a 100")
        continue
    else:
        break

apellido=input("Ingrese el apellido: ")